import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFrame, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        icon = QIcon("sinonim.png")
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Синонимы")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        button = QPushButton("СИНОНИМ")
        button.setEnabled(False)  # Делаем кнопку неактивной, чтобы она выглядела как надпись

        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        frame.setLayout(QHBoxLayout())
        frame.layout().addWidget(button)
        frame.layout().setAlignment(Qt.AlignCenter)
        frame.layout().setContentsMargins(2, 2, 2, 2)  # Устанавливаем отступы в пару пунктов

        layout.addWidget(frame)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Здесь мы устанавливаем фоновое изображение для окна
        self.setStyleSheet("background-image: url('blue.png');")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.showMaximized()
app.exec_()
