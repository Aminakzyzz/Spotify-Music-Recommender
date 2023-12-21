'''
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = QDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication([])

# Create a message box
message_box = QMessageBox()

# Set the message box properties
message_box.setIcon(QMessageBox.Icon.Information)
message_box.setText("This is a message box alert.")
message_box.setWindowTitle("Alert")

# Add buttons to the message box
message_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

# Executing the message box
result = message_box.exec()

# Check the result and perform actions accordingly
if result == QMessageBox.StandardButton.Ok:
    print("OK button clicked")
elif result == QMessageBox.StandardButton.Cancel:
    print("Cancel button clicked")

app.exec()
