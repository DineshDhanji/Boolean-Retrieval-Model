import pathlib
import re
from typing import Tuple, Set, List, Dict
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import pickle
import time

from ordered_set import OrderedSet
from collections import defaultdict


class BooleanRetrieval:
    def __init__(
        self,
        documents_path: str = None,
        stop_words_file_path: str = None,
        inverted_index_path: str = "inverted_index.pkl",
        positional_index_path: str = "positional_index.pkl",
    ) -> None:
        self.documents_path = documents_path
        self.stop_words_file_path = stop_words_file_path
        self.stop_words = OrderedSet()
        self.inverted_index = defaultdict(list)
        self.positional_index = defaultdict(dict)
        self.universal_set = OrderedSet()
        self.stemmer = PorterStemmer()
        self.inverted_index_path = inverted_index_path
        self.positional_index_path = positional_index_path
        self.load_database_time = 0

    def initiate(self) -> int:
        inverted_index_path = pathlib.Path(self.inverted_index_path)
        positional_index_path = pathlib.Path(self.positional_index_path)
        if inverted_index_path.exists() and positional_index_path.exists():
            print(
                "Preprocessed data was found. The system is going to use the provided indexes."
            )
            start_time = time.time()
            self.load_indexes(inverted_index_path, positional_index_path)
            self.load_database_time = time.time() - start_time
            print(f"Total entires in the collection\t{len(self.inverted_index)}")
            return 1
        else:
            print(
                "Preprocessed data not found. The system is going to make new indexes."
            )
            if not self.documents_path:
                print("No document path was given to the boolean model.")
                return -1
            if not self.stop_words_file_path:
                print("No stop words file path was given to the boolean model.")
                return -1

            try:
                folder_path = pathlib.Path(self.documents_path)
                stop_words_file_path = pathlib.Path(self.stop_words_file_path)

                if not folder_path.exists():
                    print(f"Document path '{self.documents_path}' does not exist.")
                    return -1
                if not stop_words_file_path.exists():
                    print(
                        f"Stop words file path '{self.stop_words_file_path}' does not exist."
                    )
                    return -2

                self.load_stop_words(stop_words_file_path)
                start_time = time.time()
                try:
                    for file_path in folder_path.iterdir():
                        print(f"Parsing\t{file_path}")
                        self.parse_document(file_path)
                except Exception as e:
                    print(f"Error occurred during parse_document: {e}")
                self.save_indexes()
                self.load_database_time = time.time() - start_time
                print("\nSaving all computed indexes on the drive.")
                print(f"Total entires in the collection\t{len(self.inverted_index)}")

                return 1

            except Exception as e:
                print(f"Error occurred while initiating the model: {e}")
                return -1

    def load_stop_words(self, file_path: pathlib.Path):
        try:
            with open(file_path, "r") as stop_words_file:
                for stop_word in stop_words_file:
                    self.stop_words.add(stop_word.strip())
            print("Stop words loaded successfully.")
        except Exception as e:
            print(f"Error occurred while loading stop words: {e}")

    def parse_document(self, file_path: pathlib.Path) -> int:
        """
        Parses the document and updates both inverted and positional indexes.
        """
        file_name = file_path.stem
        self.universal_set.add(file_name)
        file_contents = file_path.read_text()
        pattern = r"\b(?![a-zA-Z]+://)[A-Za-z]+\b"

        words = re.findall(pattern, file_contents.lower())
        for position, token in enumerate(words):
            # Don't include a single character token or stop words
            if len(token) < 2 or token in self.stop_words or len(token) >= 27:
                continue

            stemmed_token = self.stemmer.stem(token)
            try:
                a = self.inverted_index[stemmed_token]
                if file_name not in a:
                    self.inverted_index[stemmed_token].append(file_name)
            except:
                self.inverted_index[stemmed_token].append(file_name)

            if stemmed_token not in self.positional_index:
                self.positional_index[stemmed_token] = {}

            if file_name not in self.positional_index[stemmed_token]:
                self.positional_index[stemmed_token][file_name] = []

            self.positional_index[stemmed_token][file_name].append(position)
        return 1

    def save_indexes(
        self,
        inverted_index_path: str = "inverted_index.pkl",
        positional_index_path: str = "positional_index.pkl",
    ) -> None:
        """
        Save both inverted index and positional index to disk.
        """
        with open(inverted_index_path, "wb") as inverted_index_file:
            pickle.dump(self.inverted_index, inverted_index_file)

        with open(positional_index_path, "wb") as positional_index_file:
            pickle.dump(self.positional_index, positional_index_file)

    def load_indexes(
        self,
        inverted_index_path: str,
        positional_index_path: str,
    ) -> None:
        """
        Load both inverted index and positional index from disk.
        """
        try:
            with open(inverted_index_path, "rb") as inverted_index_file:
                self.inverted_index = pickle.load(inverted_index_file)

            with open(positional_index_path, "rb") as positional_index_file:
                self.positional_index = pickle.load(positional_index_file)

            # Create the universal set of all documents
            folder_path = pathlib.Path(self.documents_path)
            try:
                for file_path in folder_path.iterdir():
                    self.universal_set.add(file_path.stem)
            except Exception as e:
                print(f"Error occurred during creating universal doc set: {e}")

            print("Indexes loaded successfully.")
        except Exception as e:
            print(f"Error occurred while loading indexes: {e}")

    def validate_query_invert_index(self, user_query: str) -> Tuple[int, str]:
        """
        Check and validate the user query format.
        """
        # Tokenize the user query
        query_tokens = user_query.lower().split()

        if not query_tokens:
            return -1, "Kindly provide a query to proceed"

        # Check if the query contains only valid operators and terms
        valid_operators = {"and", "or", "not"}
        for token in query_tokens:
            if token not in valid_operators and not token.isalpha():
                return (
                    -1,
                    f"Invalid token in query: {token}. Only alphanumeric characters and valid operators (AND, OR, NOT) are allowed.",
                )

        # Apply stemming to the query tokens
        stemmed_tokens = [self.stemmer.stem(token) for token in query_tokens]

        # Check if the query format is valid
        for i, token in enumerate(stemmed_tokens):
            if i == 0 and token in {"and", "or"}:
                return -1, "AND / OR operator must not initiate the query"

            if token == "not":
                if (
                    i + 1 >= len(stemmed_tokens)
                    or stemmed_tokens[i + 1] in valid_operators
                ):
                    return -1, "NOT operator must be followed by a term"
            elif token == "or" or token == "and":
                if i + 1 >= len(stemmed_tokens) or stemmed_tokens[i + 1] in {
                    "and",
                    "or",
                }:
                    return -1, "AND / OR  operator must be followed by a term"
            else:
                if i != len(stemmed_tokens) - 1 and (
                    i + 1 >= len(stemmed_tokens)
                    or stemmed_tokens[i + 1] not in {"and", "or"}
                ):
                    return -1, "Word must be followed by AND / OR"

        # If the query format is valid, return the stemmed query
        return 0, " ".join(stemmed_tokens)

    def validate_query_posit_index(self, user_query: str) -> Tuple[int, str]:
        pattern = r"^\w+\s\w+\s/\s[1-9]$|^10$"
        # Validate the user query format using regex
        if re.match(pattern, user_query):
            query_tokens = user_query.lower().split()
            stemmed_tokens = [self.stemmer.stem(token) for token in query_tokens]
            # If the query format is valid, return the stemmed query
            return 0, " ".join(stemmed_tokens)
        else:
            return (
                -1,
                "Invalid query format. Please use the format 'X Y / k' where X and Y are terms and k is a positive integer less than 10. Kindly remove extra spaces.",
            )

    def retrieve_from_inverted_index(
        self, user_query: str
    ) -> Tuple[str, Set[str], float]:
        """
        Retrieve documents based on the user query.
        """
        start_time = time.time()
        # Validate the user query
        validation_result, validated_query = self.validate_query_invert_index(
            user_query
        )
        if validation_result != 0:
            return validated_query, set(), -1

        def retrieve_documents_for_term(term: str) -> set:
            if term in self.inverted_index:
                return set(self.inverted_index[term])
            return set()

        operator = []
        terms = []

        validate_operator = ["and", "or", "not"]
        query_tokens = validated_query.split()

        q = 0
        while q < len(query_tokens):

            if query_tokens[q] not in validate_operator:
                terms.append(retrieve_documents_for_term(query_tokens[q]))
            else:
                if query_tokens[q] == "not":
                    terms.append(
                        set(self.universal_set).difference(
                            retrieve_documents_for_term(query_tokens[q + 1])
                        )
                    )
                    q += 1
                else:
                    operator.append(query_tokens[q])
            q += 1

        while len(terms) > 1:
            op = operator.pop()
            b = terms.pop()
            a = terms.pop()

            if op == "and":
                a = a.intersection(b)
                terms.append(a)
            elif op == "or":
                a = a.union(b)
                terms.append(a)

        return "Result", terms[0], time.time() - start_time

    def retrieve_from_positional_index(
        self, user_query: str
    ) -> Tuple[str, Set[str], float]:
        def retrieve_documents_with_distance(
            term1: str, term2: str, k: int
        ) -> List[str]:
            """
            Retrieve documents containing both term1 and term2 with a distance of k between them.
            """
            if term1 not in self.positional_index or term2 not in self.positional_index:
                return []

            documents_for_k = []
            for document in self.universal_set:
                if (
                    document in self.positional_index[term1]
                    and document in self.positional_index[term2]
                ):
                    positions1 = self.positional_index[term1][document]
                    positions2 = self.positional_index[term2][document]
                    for pos1 in positions1:
                        for pos2 in positions2:
                            if abs(pos1 - pos2) == k:
                                documents_for_k.append(document)
                                break
            return documents_for_k

        start_time = time.time()
        # Validate the user query
        validation_result, validated_query = self.validate_query_posit_index(user_query)
        if validation_result != 0:
            print(f"Invalid query: {validated_query}")
            return validated_query, set(), -1
        query_tokens = validated_query.split()
        # Extract terms and k value from the validated query
        term1, term2, k = query_tokens[0], query_tokens[1], int(query_tokens[3])

        # Retrieve documents for each value of k from 0 to the given k
        retrieved_documents = set()
        for i in range(k + 1):
            documents_for_k = retrieve_documents_with_distance(term1, term2, i)
            for i in documents_for_k:
                retrieved_documents.add(i)

        return "Result", retrieved_documents, time.time() - start_time

    def dummy(self):
        print("DUMMY")
        return "DUMMY"
