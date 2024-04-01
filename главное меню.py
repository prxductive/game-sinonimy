import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PySide6.QtGui import QIcon, Qt, QFont, QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        icon = QIcon("sinonim.png")
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Синонимы")
        self.setWindowIcon(icon)

        self.button_play = QPushButton("ИГРАТЬ", parent=self)
        self.button_play.setFont(QFont('Comic Sans', 30))
        self.button_play.setFixedSize(400, 100)
        self.button_play.setStyleSheet("""
    background-image: url('Играть.png');
    background-repeat: no-repeat;
    background-position: center;
    background-color: rgb(0, 255, 0);
    color: white;
    border-radius: 15px;
""")

        self.button_exit = QPushButton("ВЫХОД", parent=self)
        self.button_exit.setFont(QFont('Comic Sans', 30))
        self.button_exit.setFixedSize(400, 100)
        self.button_exit.setStyleSheet("""
    background-image: url('Выход.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-color: rgb(0, 255, 0);
    color: white;
    border-radius: 15px;
""")
        self.button_exit.clicked.connect(self.close)

        self.label = QLabel("НАЙДИ СИНОНИМ",  parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Comic Sans', 30))
        self.label.setStyleSheet("background: transparent")  # Добавлено здесь

        layout_play = QHBoxLayout()
        layout_play.addStretch()
        layout_play.addWidget(self.button_play)
        layout_play.addStretch()

        layout_exit = QHBoxLayout()
        layout_exit.addStretch()
        layout_exit.addWidget(self.button_exit)
        layout_exit.addStretch()

        layout = QVBoxLayout()
        layout.addStretch(3)
        layout.addLayout(layout_play)
        layout.addStretch(0.5)
        layout.addLayout(layout_exit)
        layout.addStretch(3)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setStyleSheet("background-image: url('sirenpink.png'); background-size: cover;")

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.showMaximized()
app.exec()
