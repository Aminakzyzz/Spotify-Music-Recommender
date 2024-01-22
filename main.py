print("[Awaken]")

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QMessageBox, QTableWidgetItem
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QPixmap
import os

from PyQt6.QtCore import QTimer

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from mySpotify import searchSong
from recomendationskNrearest import getRecomendations

width = 1500
height = 850


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Spotify Music Recommender")
        self.searchedSongData = None

        self.setFixedSize(width, height)
        self.setWindowIcon(QIcon("images/logoSpotify.png"))  # provisional icon

        layout = QVBoxLayout(self)

        self.widgets_setup()

        self.load_png(default=True)

    def widgets_setup(self):
        self.setObjectName("self")
        self.resize(width, height)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        searchBar_width = 200
        searchBar_height = 31
        self.searchBar = QLineEdit(parent=self)
        self.searchBar.setGeometry(QtCore.QRect(int(width / 2) - searchBar_width - 50, 90, 571, searchBar_height))
        self.searchBar.setObjectName("searchBar")

        imagelabel_width = int(width / 2) + 10
        imagelabel_height = 450
        self.image = QtWidgets.QLabel(parent=self)
        self.image.setGeometry(QtCore.QRect(750, 270, imagelabel_width, imagelabel_height))
        self.image.setObjectName("image")

        Title_width = 100
        Title_height = 41
        self.Title = QtWidgets.QLabel(parent=self)
        self.Title.setGeometry(QtCore.QRect(int(width / 2) - (Title_width + 90), 30, 500, Title_height))
        self.Title.setStyleSheet('font: 75 18pt "MS Shell Dlg 2"; color: #1DB954; font-weight: bold;')
        self.Title.setObjectName("Title")

        label_width = 91
        label_height = 28
        self.lable1 = QtWidgets.QLabel(parent=self)
        self.lable1.setGeometry(QtCore.QRect(400, 90, label_width, label_height))
        self.lable1.setObjectName("label1")

        BUTTON_WIDTH = 150

        search_width = 171
        search_height = 31
        self.buttonSearch = QtWidgets.QPushButton(parent=self)
        self.buttonSearch.setGeometry(QtCore.QRect(int(width / 2) + searchBar_width + search_width - 50, 90, BUTTON_WIDTH, search_height))
        self.buttonSearch.setObjectName("buttonSearch")
        self.buttonSearch.setStyleSheet("color: #1DB954; font-weight: bold;")

        self.buttonSearch.clicked.connect(self.onClickedSearch)

        self.recommendButton = QtWidgets.QPushButton(parent=self)
        self.recommendButton.setGeometry(QtCore.QRect(int(width / 2) + searchBar_width + search_width + 170, 200, BUTTON_WIDTH, search_height))
        self.recommendButton.setObjectName("buttonRecommend")
        self.recommendButton.setStyleSheet("color: #1DB954; font-weight: bold;")

        self.recommendButton.clicked.connect(self.triggerRecomendation)

        self.settings = QtWidgets.QLabel(parent=self)
        self.settings.setGeometry(QtCore.QRect(80, 140, 67, 17))
        self.settings.setObjectName("settings")
        self.settings.setStyleSheet("font-weight: bold;")

        self.slider_danceability = QtWidgets.QSlider(parent=self)
        self.slider_danceability.setGeometry(QtCore.QRect(180, 220, 160, 16))
        self.slider_danceability.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_danceability.setObjectName("slider_danceability")
        self.danceability_value = QtWidgets.QLabel(parent=self)
        self.slider_danceability.valueChanged.connect(self.updateDanceablitiy)
        self.slider_danceability.setValue(50)
        self.slider_danceability.setStyleSheet("QSlider::handle:horizontal { background: #1DB954; }")

        self.danceability = QtWidgets.QLabel(parent=self)
        self.danceability.setGeometry(QtCore.QRect(180, 190, 100, 17))
        self.danceability.setObjectName("danceability")

        self.tempo = QtWidgets.QLabel(parent=self)
        self.tempo.setGeometry(QtCore.QRect(480, 190, 67, 17))
        self.tempo.setObjectName("tempo")

        self.slider_tempo = QtWidgets.QSlider(parent=self)
        self.slider_tempo.setGeometry(QtCore.QRect(480, 220, 160, 16))
        self.slider_tempo.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_tempo.setObjectName("slider_tempo")
        self.tempo_value = QtWidgets.QLabel(parent=self)
        self.slider_tempo.valueChanged.connect(self.updateTempo)
        self.slider_tempo.setValue(50)
        self.slider_tempo.setStyleSheet("QSlider::handle:horizontal { background: #1DB954; }")

        self.popularity = QtWidgets.QLabel(parent=self)
        self.popularity.setGeometry(QtCore.QRect(780, 190, 81, 17))
        self.popularity.setObjectName("popularity")

        self.slider_popularity = QtWidgets.QSlider(parent=self)
        self.slider_popularity.setGeometry(QtCore.QRect(780, 220, 160, 16))
        self.slider_popularity.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_popularity.setObjectName("slider_popularity")
        self.popularity_value = QtWidgets.QLabel(parent=self)
        self.slider_popularity.valueChanged.connect(self.updatePopularity)
        self.slider_popularity.setValue(50)
        self.slider_popularity.setStyleSheet("QSlider::handle:horizontal { background: #1DB954; }")

        self.energy = QtWidgets.QLabel(parent=self)
        self.energy.setGeometry(QtCore.QRect(1080, 190, 67, 17))
        self.energy.setObjectName("energy")

        self.slider_energy = QtWidgets.QSlider(parent=self)
        self.slider_energy.setGeometry(QtCore.QRect(1080, 220, 160, 16))
        self.slider_energy.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_energy.setObjectName("slider_energy")
        self.energy_value = QtWidgets.QLabel(parent=self)
        self.slider_energy.valueChanged.connect(self.updateEnergy)
        self.slider_energy.setValue(50)
        self.slider_energy.setStyleSheet("QSlider::handle:horizontal { background: #1DB954; }")
        table_width = int(width / 2)
        table_height = 500
        self.tableWidget = QtWidgets.QTableWidget(parent=self)
        self.tableWidget.setGeometry(QtCore.QRect(20, 300, table_width, table_height))
        self.tableWidget.setObjectName("tableWidget")

        self.headers = ["Song", "Artist", "Explicit", "Speechiness", "Loudness (db)", "Duration (min)", "Distance"]

        self.tableWidget.setColumnCount(len(self.headers))
        self.tableWidget.setRowCount(10)

        self.tableWidget.setHorizontalHeaderLabels(self.headers)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.Title.setText("SPOTIFY MUSIC RECOMMENDER")
        self.lable1.setText("Enter a Song:")
        self.settings.setText("Settings:")
        self.danceability.setText("Danceability")
        self.buttonSearch.setText("Get Song Data")
        self.recommendButton.setText("Recommend")
        self.tempo.setText("Tempo")
        self.popularity.setText("Popularity")
        self.energy.setText("Energy")

    def load_png(self, default=False):
        if default:
            self.loadPngFromName("images/defaultPlot.png")
        else:
            self.loadPngFromName("plot.png")

    def loadPngFromName(self, imageName):
        pixmap = QPixmap(imageName)
        if pixmap.isNull():
            print("Error: Unable to load image.")
        else:
            self.image.setPixmap(pixmap)
            self.image.setScaledContents(True)

    def updateDanceablitiy(self, value):
        self.danceability_value.setText(f"{value}")

        label_width = 91  # Adjust this value based on your label's width
        self.danceability_value.setGeometry(QtCore.QRect(230 + label_width, 190, 50, 17))

        self.danceability_value_value = value  # Update the variable name if needed

    def updateTempo(self, value):
        self.tempo_value.setText(f"{value}")
        label_width = 91

        self.tempo_value.setGeometry(QtCore.QRect(530 + label_width, 190, 50, 17))

        self.tempo_value_value = value

    def updatePopularity(self, value):
        self.popularity_value.setText(f"{value}")
        label_width = 91

        self.popularity_value.setGeometry(QtCore.QRect(830 + label_width, 190, 50, 17))
        self.popularity_value_value = value

    def updateEnergy(self, value):
        self.energy_value.setText(f"{value}")
        label_width = 91

        self.energy_value.setGeometry(QtCore.QRect(1130 + label_width, 190, 50, 17))
        self.energy_value_value = value

    def fill_table(self, dictDatas, hasDistance=False):
        lables = ["name", "artists", "explicit", "speechiness", "loudness", "duration_ms"]

        for dictCount, dictData in enumerate(dictDatas):
            dictData = dict(dictData)

            for index, key in enumerate(lables):
                data = dictData[key]

                if key == "duration_ms":
                    data = round((data) / 60000, 2)
                elif key == "explicit":
                    data = "Yes" if data == "1" else "No"
                elif key == "artists":
                    data = data.replace("[", "").replace("]", "").replace("'", "")
                elif key == "loudness":
                    data = round((data), 2)
                elif key == "speechiness":
                    data = round((data), 2)

                widgetItem = QTableWidgetItem(str(data))

                self.tableWidget.setItem(dictCount, index, widgetItem)
            distance = 0
            if hasDistance:
                print(dictData)
                distance = round(dictData["distance"], 2)
            self.tableWidget.setItem(dictCount, len(self.headers) - 1, QTableWidgetItem(str(distance)))

    def onClickedSearch(self):
        inputText = self.searchBar.text()
        if inputText == "":
            QMessageBox.information(self, "ALERT", "You must enter a song name!", QMessageBox.StandardButton.Ok)
            return

        self.searchedSongData = searchSong(inputText)
        tableSearchedSongData = self.searchedSongData
        tableSearchedSongData["artists"] = tableSearchedSongData["artist"]
        recomendations = [tableSearchedSongData]
        self.fill_table(recomendations, False)
        danceabilityPercent = self.searchedSongData["danceability"] * 100
        tempoPercent = self.searchedSongData["tempo"] / 245 * 100
        popularityPercent = self.searchedSongData["popularity"]
        energyPercent = self.searchedSongData["energy"] * 100

        danceabilityPercent = int(danceabilityPercent)
        tempoPercent = int(tempoPercent)
        popularityPercent = int(popularityPercent)
        energyPercent = int(energyPercent)

        self.slider_danceability.setValue(danceabilityPercent)
        self.slider_tempo.setValue(tempoPercent)
        self.slider_popularity.setValue(popularityPercent)
        self.slider_energy.setValue(energyPercent)

        self.recommendButton.setStyleSheet("background-color: #1DB954; color: #F0FFFF; font-weight: bold;")

    def onClickRecommend(self):
        if self.searchedSongData == None:
            QMessageBox.information(self, "ALERT", "You must get the get the song data first!", QMessageBox.StandardButton.Ok)
            return

        danceibilityValue = self.slider_danceability.value() / 100
        tempoValue = self.slider_tempo.value() / 100 * 245
        popularityValue = self.slider_popularity.value()
        energyValue = self.slider_energy.value() / 100

        songData = self.searchedSongData
        songData["danceability"] = danceibilityValue
        songData["tempo"] = tempoValue
        songData["popularity"] = popularityValue
        songData["energy"] = energyValue

        recomendations = getRecomendations(songData)
        songData["distance"] = 0
        recomendations = [songData] + recomendations
        recomendations.pop(-1)
        self.fill_table(recomendations, True)
        self.load_png()

    def triggerRecomendation(self):
        self.loadPngFromName("images/generatingInfo.png")
        # print("LOAD generatingInfo IMAGE")
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.onClickRecommend)
        timer.start(5)  # Immediate timeout

        # self.update()
        # input("+++++++++++++++++++")
        # self.onClickRecommend()


if __name__ == "__main__":
    print("[Started]")
    app = QApplication(sys.argv)
    window = mainWindow()
    window.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)
    window.show()
    window.activateWindow()
    sys.exit(app.exec())
