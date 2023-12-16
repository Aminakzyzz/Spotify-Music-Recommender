import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSlider
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


class MusicRecommenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Music Recommender System")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input Widgets
        self.slider1 = QSlider()
        self.slider2 = QSlider()
        self.slider3 = QSlider()

        self.slider1.valueChanged.connect(self.update_recommendation)
        self.slider2.valueChanged.connect(self.update_recommendation)
        self.slider3.valueChanged.connect(self.update_recommendation)

        layout.addWidget(QLabel("Feature 1"))
        layout.addWidget(self.slider1)
        layout.addWidget(QLabel("Feature 2"))
        layout.addWidget(self.slider2)
        layout.addWidget(QLabel("Feature 3"))
        layout.addWidget(self.slider3)

        # Output Canvas
        self.fig, self.ax = plt.subplots()
        # self.canvas = self.addCanvas(self.fig)

        # layout.addWidget(self.canvas)

        # Metrics
        self.metrics_label = QLabel()
        layout.addWidget(self.metrics_label)

        self.central_widget.setLayout(layout)

        # Initial recommendation
        self.update_recommendation()

    # def addCanvas(self, figure):
    #     from matplotlib.backends.backend_qt6agg import FigureCanvasQTAgg as FigureCanvas
    #     canvas = FigureCanvas(figure)
    #     return canvas

    def update_recommendation(self):
        # Get feature values
        feature1 = self.slider1.value()
        feature2 = self.slider2.value()
        feature3 = self.slider3.value()

        # Simulate a dataset
        np.random.seed(42)
        X = np.random.rand(100, 3) * 10
        y = 2 * X[:, 0] + 3 * X[:, 1] + 5 * X[:, 2] + np.random.randn(100)

        # Train a simple linear regression model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        X_new = np.array([[feature1, feature2, feature3]])
        y_pred = model.predict(X_new)

        # Update plot
        self.ax.clear()
        self.ax.scatter(X_test[:, 0], y_test, color="black", label="Actual")
        self.ax.scatter(X_new[:, 0], y_pred, color="red", marker="x", label="Prediction")
        self.ax.set_xlabel("Feature 1")
        self.ax.set_ylabel("Target")
        self.ax.legend()

        # Update metrics
        mse = mean_squared_error(y_test, model.predict(X_test))
        r2 = r2_score(y_test, model.predict(X_test))
        self.metrics_label.setText(f"Mean Squared Error: {mse:.2f} | R2 Score: {r2:.2f}")

        # Redraw canvas
        # self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicRecommenderApp()
    window.show()
    sys.exit(app.exec())
