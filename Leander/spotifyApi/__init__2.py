import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, QSlider
from PyQt6.QtCore import Qt
from mySpotify import searchSong


class MyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Music Recommender")
        self.setGeometry(400, 40, 600, 800)

        layout = QVBoxLayout()

        self.input_label = QLabel("Enter Song:")
        layout.addWidget(self.input_label)

        self.input_text = QLineEdit(self)
        layout.addWidget(self.input_text)

        self.explicit_checkbox = QCheckBox("Explicit Songs", self)
        layout.addWidget(self.explicit_checkbox)

        self.danceability_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.danceability_slider.setRange(0, 100)
        self.danceability_slider.setValue(50)
        layout.addWidget(QLabel("Danceability", self))
        layout.addWidget(self.danceability_slider)

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(4)  # Columns: Song, Artist, Explicit, Danceability
        self.table_widget.setHorizontalHeaderLabels(["Song", "Artist", "Explicit", "Danceability"])
        layout.addWidget(self.table_widget)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def on_submit(self):
        input_text = self.input_text.text()
        explicit = self.explicit_checkbox.isChecked()
        danceability = self.danceability_slider.value() / 100.0  # Normalize to 0-1 range

        result_dict = searchSong(input_text)  # , explicit, danceability

        result_dictList = [result_dict]

        self.table_widget.setRowCount(len(result_dictList))

        row = 0
        for song_data in result_dictList:
            song_item = QTableWidgetItem(song_data["name"])
            artist_item = QTableWidgetItem(song_data["artist"])
            explicit_item = QTableWidgetItem("Yes" if song_data["explicit"] else "No")
            danceability_item = QTableWidgetItem(str(song_data["danceability"]))

            self.table_widget.setItem(row, 0, song_item)
            self.table_widget.setItem(row, 1, artist_item)
            self.table_widget.setItem(row, 2, explicit_item)
            self.table_widget.setItem(row, 3, danceability_item)

            # Add a button to open the link in the browser
            open_button = QPushButton("Open Link", self)
            open_button.clicked.connect(lambda _, link="https://developer.spotify.com/documentation/web-api/reference/search": self.open_link(link))
            self.table_widget.setCellWidget(row, 4, open_button)

            row += 1

    def open_link(self, link):
        # You should implement a function to open a link in the browser here.
        # This is just a placeholder example.
        print(f"Opening link: {link}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_gui = MyGUI()
    my_gui.show()
    sys.exit(app.exec())
