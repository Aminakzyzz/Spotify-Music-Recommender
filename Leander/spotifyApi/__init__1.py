import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem
from mySpotify import searchSong


class MyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Song Search App")
        self.setGeometry(400, 40, 600, 800)

        layout = QVBoxLayout()

        self.input_label = QLabel("Enter Song:")
        layout.addWidget(self.input_label)

        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)  # Assuming a key-value pair in the dictionary
        self.table_widget.setHorizontalHeaderLabels(["Key", "Value"])
        layout.addWidget(self.table_widget)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def on_submit(self):
        input_text = self.input_text.text()
        result_dict = searchSong(input_text)

        self.table_widget.setRowCount(len(result_dict))

        row = 0
        for key, value in result_dict.items():
            key_item = QTableWidgetItem(str(key))
            value_item = QTableWidgetItem(str(value))

            self.table_widget.setItem(row, 0, key_item)
            self.table_widget.setItem(row, 1, value_item)

            row += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    my_gui.show()
    sys.exit(app.exec())
