from PySide6 import QtWidgets
from ui import main, inverted_index, positional_index
from boolean_retrieval import (
    BooleanRetrieval,
)


class BooleanRetrievalApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(BooleanRetrievalApp, self).__init__()
        self.setupUi(self)
        # Connect the Inverted Index button click event to the show_inverted_index_window function
        self.inverted_index_btn.clicked.connect(self.show_inverted_index_window)
        self.positional_index_btn.clicked.connect(self.show_positional_index_window)

        # Create an instance of the BooleanRetrieval class
        self.boolean_retrieval = BooleanRetrieval(
            documents_path="ResearchPapers", stop_words_file_path="Stopword-List.txt"
        )
        # Initiate the BooleanRetrieval instance
        return_status = self.boolean_retrieval.initiate()
        if return_status != 1:
            exit()

        system_log = f"{len(self.boolean_retrieval.inverted_index)}\n{len(self.boolean_retrieval.positional_index)}\n{self.boolean_retrieval.load_database_time}s"
        self.label_3.setText(system_log)

    def show_inverted_index_window(self):
        # Create an instance of the Inverted Index window
        self.inverted_index_window = InvertedIndex()
        self.inverted_index_window.previous_window = self
        self.inverted_index_window.show()

        # Hide the main window
        self.hide()

    def show_positional_index_window(self):
        # Create an instance of the Inverted Index window
        self.inverted_index_window = PositionalIndex()
        self.inverted_index_window.previous_window = self
        self.inverted_index_window.show()

        # Hide the main window
        self.hide()


class InvertedIndex(inverted_index.Ui_Inverted_index, QtWidgets.QMainWindow):
    def __init__(self):
        super(InvertedIndex, self).__init__()
        self.setupUi(self)

        # Connect the Back button click event to the show_previous_window function
        self.back_btn.clicked.connect(self.show_previous_window)
        self.previous_window = None

        # Connect the Search button click event to the boolean_retrieval.dummy function
        self.search_btn.clicked.connect(self.search_button_clicked)

    def show_previous_window(self):
        if self.previous_window:
            # Show the previous window
            self.previous_window.show()
            # Close the current window
            self.close()

    def search_button_clicked(self):

        if self.previous_window and self.previous_window.boolean_retrieval:
            # Retrieve the user query from the input box
            user_query = self.user_query.text()

            result, output, query_processing_time = (
                self.previous_window.boolean_retrieval.retrieve_from_inverted_index(
                    user_query
                )
            )

            # Copy the user query to the output box
            self.output_box.setText(f"{result}\n{output}")
            self.query_processing_time.setText(f"{query_processing_time}s")



class PositionalIndex(positional_index.Ui_PositionalIndex, QtWidgets.QMainWindow):
    def __init__(self):
        super(PositionalIndex, self).__init__()
        self.setupUi(self)

        # Connect the Back button click event to the show_previous_window function
        self.back_btn.clicked.connect(self.show_previous_window)
        self.previous_window = None

        # Connect the Search button click event to the boolean_retrieval.dummy function
        self.search_btn.clicked.connect(self.search_button_clicked)

    def show_previous_window(self):
        if self.previous_window:
            # Show the previous window
            self.previous_window.show()
            # Close the current window
            self.close()

    def search_button_clicked(self):

        if self.previous_window and self.previous_window.boolean_retrieval:
            # Retrieve the user query from the input box
            user_query = self.user_query.text()

            result, output, query_processing_time = (
                self.previous_window.boolean_retrieval.retrieve_from_positional_index(
                    user_query
                )
            )

            # Copy the user query to the output box
            self.output_box.setText(f"{result}\n{output}")
            self.query_processing_time.setText(f"{query_processing_time}s")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    boolean_retrieval_app = BooleanRetrievalApp()
    boolean_retrieval_app.show()
    app.exec()
