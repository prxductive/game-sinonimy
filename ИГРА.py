import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QSizePolicy
from PySide6.QtGui import QIcon, Qt, QFont, QPixmap
from PySide6.QtCore import Qt

def create_synonym_widget():
    layout = QVBoxLayout()

    button = QPushButton("СИНОНИМ")
    button.setEnabled(False)  # Делаем кнопку неактивной, чтобы она выглядела как надпись

    layout.addWidget(button)

    widget = QWidget()
    widget.setLayout(layout)
    widget.setStyleSheet("background-image: url('blue.png'); background-size: cover;")  # Устанавливаем фоновое изображение для виджета
    widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # Виджет будет занимать все доступное пространство
    return widget

def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()

def main_menu(main_window, layout):
    button_play = QPushButton("ИГРАТЬ", parent=main_window)
    button_play.setFont(QFont('Comic Sans', 30))
    button_play.setFixedSize(400, 100)
    button_play.setStyleSheet("""
    background-image: url('Играть.png');
    background-repeat: no-repeat;
    background-position: center;
    background-color: rgb(0, 255, 0);
    color: white;
    border-radius: 15px;
""")
    button_play.clicked.connect(lambda: start_game(main_window, layout))

    button_exit = QPushButton("ВЫХОД", parent=main_window)
    button_exit.setFont(QFont('Comic Sans', 30))
    button_exit.setFixedSize(400, 100)
    button_exit.setStyleSheet("""
    background-image: url('Выход.jpg');
    background-repeat: no-repeat;
    background-position: center;
    background-color: rgb(0, 255, 0);
    color: white;
    border-radius: 15px;
""")
    button_exit.clicked.connect(main_window.close)

    label = QLabel("НАЙДИ СИНОНИМ",  parent=main_window)
    label.setAlignment(Qt.AlignCenter)
    label.setFont(QFont('Comic Sans', 30))
    label.setStyleSheet("background: transparent")  # Добавлено здесь

    layout_play = QHBoxLayout()
    layout_play.addStretch()
    layout_play.addWidget(button_play)
    layout_play.addStretch()

    layout_exit = QHBoxLayout()
    layout_exit.addStretch()
    layout_exit.addWidget(button_exit)
    layout_exit.addStretch()

    layout.addStretch(3)
    layout.addLayout(layout_play)
    layout.addStretch(0.5)
    layout.addLayout(layout_exit)
    layout.addStretch(3)
    layout.addWidget(label)

def start_game(main_window, layout):
    clear_layout(layout)
    synonym_widget = create_synonym_widget()
    layout.addWidget(synonym_widget)

def main():
    app = QApplication(sys.argv)

    main_window = QMainWindow()
    icon = QIcon("sinonim.png")
    main_window.setGeometry(100, 100, 300, 150)
    main_window.setWindowTitle("Синонимы")
    main_window.setWindowIcon(icon)

    layout = QVBoxLayout()

    main_menu(main_window, layout)

    widget = QWidget()
    widget.setLayout(layout)
    main_window.setCentralWidget(widget)

    main_window.setStyleSheet("background-image: url('sirenpink.png'); background-size: cover;")

    main_window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
