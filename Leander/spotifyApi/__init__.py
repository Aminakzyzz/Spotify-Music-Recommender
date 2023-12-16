import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from mySpotify import searchSong


class MyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Song Search App")
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.input_label = QLabel("Enter Song:")
        layout.addWidget(self.input_label)

        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        self.output_text = QTextEdit(self)
        layout.addWidget(self.output_text)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def on_submit(self):
        input_text = self.input_text.text()
        result = searchSong(input_text)

        # Add \n after each ,
        # result_with_newline = result
        result_with_newline = str(result).replace(",", "\n")

        self.output_text.setPlainText(result_with_newline)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    my_gui.show()
    sys.exit(app.exec())
