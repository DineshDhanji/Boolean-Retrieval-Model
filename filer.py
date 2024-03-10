""""
    Use these function to generate file
    to see all of the terms and posting.
"""

def save_inverted_index_to_txt(inverted_index, output_file):
    try:
        with open(output_file, "w") as file:
            for term, document in inverted_index.items():
                file.write(f"{term}\t")
                file.write(f"{document}\n")
    except Exception as e:
        print(f"Error occurred while saving positional index to file: {e}")


def save_positional_index_to_txt(positional_index, output_file):
    try:
        with open(output_file, "w") as file:
            for term, document in positional_index.items():
                file.write(f"{term}\t")
                file.write(f"{document}\n")
    except Exception as e:
        print(f"Error occurred while saving positional index to file: {e}")


output_file1 = "inverted_index.txt"
output_file2 = "positional_index.txt"
# save_inverted_index_to_txt(br.inverted_index, output_file1)
# save_positional_index_to_txt(br.positional_index, output_file2)
