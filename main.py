from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QBrush
from PySide6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Синонимы")

        self.setGeometry(0, 0, 1920, 1080) # Установка размеров окна на 1920x1080 пикселей
        self.move(0, 0)

        # Загрузка изображения
        self.pixmap = QPixmap('sirenpink.png')

        # Установка изображения в качестве фона
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(self.palette)

        self.button_play = QPushButton("ИГРАТЬ", self)
        self.button_play.clicked.connect(self.button_play_clicked)
        self.button_play.setFont(QFont('Comic Sans', 30))
        self.button_play.setFixedSize(400, 80)
        self.button_play.setStyleSheet("""
background-image: url('Играть.png');
background-repeat: no-repeat;
background-position: center;
background-color: rgb(63, 206, 77);
color: black;
border-radius: 7px;
""")

        self.button_exit = QPushButton("ВЫХОД", self)
        self.button_exit.setFont(QFont('Comic Sans', 30))
        self.button_exit.setFixedSize(400, 80)
        self.button_exit.setStyleSheet("""
background-image: url('Выход.jpg');
background-repeat: no-repeat;
background-position: center;
background-color: rgb(229, 109, 109);
color: black;
border-radius: 7px;
""")
        self.button_exit.clicked.connect(self.close)

        self.label = QLabel("ПОДБЕРИ СИНОНИМ", parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Comic Sans', 30))
        self.label.setStyleSheet("background: transparent")
        self.label.adjustSize()

        self.level_window = LevelWindow() # Create LevelWindow instance here

    def showEvent(self, event):
        # Position the widgets
        self.button_play.move(self.width() // 2 - self.button_play.width() // 2, self.height() // 3 - self.button_play.height() // 2 + 20) # Position the "ИГРАТЬ" button in the center of the top third of the window
        self.button_exit.move(self.width() // 2 - self.button_exit.width() // 2, self.height() // 2 - self.button_exit.height() // 2 - 20) # Position the "ВЫХОД" button in the center of the window, but 30 pixels lower
        self.label.move(self.width() // 2 - self.label.width() // 2, 2 * self.height() // 3 - self.label.height() // 2 + 100)

    def button_play_clicked(self):
        self.level_window.showFullScreen() # Show the LevelWindow
        self.hide()

class LevelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Синонимы")

        self.setGeometry(0, 0, 1920, 1080) # Установка размеров окна на 1920x1080 пикселей
        self.move(0, 0)

        # Загрузка изображения
        self.pixmap = QPixmap('blue.png')

        # Установка изображения в качестве фона
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(self.palette)

        # Создание текстовых полей
        self.text_field_center = QTextEdit(self)
        self.text_field_center.setFont(QFont('Comic Sans', 30))
        self.text_field_center.setStyleSheet("background-color: white; border-radius: 7px; border: 2px solid black;")
        self.text_field_center.setReadOnly(True)  # Пользователь не может вводить текст
        self.text_field_center.setFixedSize(QSize(500, 80))  # Установка фиксированного размера
        self.text_field_center.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру

        self.text_field_bottom = QTextEdit(self)
        self.text_field_bottom.setFont(QFont('Comic Sans', 30))
        self.text_field_bottom.setStyleSheet("background-color: white; border-radius: 7px; border: 2px solid black;")
        self.text_field_bottom.setFixedSize(QSize(500, 80))  # Установка фиксированного размера
        self.text_field_bottom.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру

        # Расположение текстовых полей
        layout_center = QHBoxLayout()
        layout_center.addStretch()
        layout_center.addWidget(self.text_field_center)
        layout_center.addStretch()

        layout_bottom = QHBoxLayout()
        layout_bottom.addStretch()
        layout_bottom.addWidget(self.text_field_bottom)
        layout_bottom.addStretch()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(layout_center)
        layout.addSpacing(100)  # Добавление отступа
        layout.addLayout(layout_bottom)
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

       # Создание кнопки паузы
        self.pause_button = QPushButton(self)
        self.pause_button.setIcon(QIcon('pause.png'))  # Установка иконки кнопки
        self.pause_button.setIconSize(QSize(50, 50))  # Установка размера иконки
        self.pause_button.setFixedSize(QSize(50, 50))  # Установка размера кнопки
        self.pause_button.move(10, 10)  # Перемещение кнопки в левый верхний угол
        self.pause_button.setStyleSheet("background-color: transparent; border: none;")  # Установка стиля кнопки
        self.pause_button.clicked.connect(self.show_buttons)  # Подключение слота

        # Создание дополнительных кнопок
        self.quit_button = QPushButton(self)
        self.quit_button.setIcon(QIcon('quit.png'))  # Установка иконки кнопки
        self.quit_button.setIconSize(QSize(50, 50))  # Установка размера иконки
        self.quit_button.setFixedSize(QSize(50, 50))  # Установка размера кнопки
        self.quit_button.move(70, 10)  # Перемещение кнопки вправо от кнопки паузы
        self.quit_button.setStyleSheet("background-color: transparent; border: none;")  # Установка стиля кнопки
        self.quit_button.clicked.connect(self.close)  # Подключение слота
        self.quit_button.hide()  # Скрытие кнопки

        self.continue_button = QPushButton(self)
        self.continue_button.setIcon(QIcon('continue.png'))  # Установка иконки кнопки
        self.continue_button.setIconSize(QSize(50, 50))  # Установка размера иконки
        self.continue_button.setFixedSize(QSize(50, 50))  # Установка размера кнопки
        self.continue_button.move(130, 10)  # Перемещение кнопки вправо от первой дополнительной кнопки
        self.continue_button.setStyleSheet("background-color: transparent; border: none;")  # Установка стиля кнопки
        self.continue_button.clicked.connect(self.hide_buttons)  # Подключение слота
        self.continue_button.hide()  # Скрытие кнопки

    def show_buttons(self):
        """Показывает дополнительные кнопки при нажатии на кнопку паузы."""
        self.quit_button.show()
        self.continue_button.show()

    def hide_buttons(self):
        """Скрывает дополнительные кнопки при нажатии на кнопку continue."""
        self.quit_button.hide()
        self.continue_button.hide()

app = QApplication([])
window = MainWindow()
window.showFullScreen() # Show the MainWindow in full screen
sys.exit(app.exec())
