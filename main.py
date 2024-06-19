from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QBrush
from PySide6.QtCore import Qt, QSize, Signal, QTimer
import sys
import random
import codecs

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Синонимы")

        self.setGeometry(0, 0, 1920, 1080)
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
background-image: url('Играть.jpg');
background-repeat: no-repeat;
background-position: center;
background-color: rgb(63, 206, 77);
color: white;
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
color: white;
border-radius: 7px;
""")
        self.button_exit.clicked.connect(self.close)

        self.label = QLabel("ПОДБЕРИ СИНОНИМ", parent=self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Comic Sans', 30))
        self.label.setStyleSheet("background: transparent")
        self.label.adjustSize()

        self.level_window = LevelWindow()

    def showEvent(self, event):

        self.button_play.move(self.width() // 2 - self.button_play.width() // 2, self.height() // 3 - self.button_play.height() // 2 + 20)
        self.button_exit.move(self.width() // 2 - self.button_exit.width() // 2, self.height() // 2 - self.button_exit.height() // 2 - 20)
        self.label.move(self.width() // 2 - self.label.width() // 2, 2 * self.height() // 3 - self.label.height() // 2 + 100)

    def button_play_clicked(self):
        self.level_window.showFullScreen()
        self.hide()

class CustomTextEdit(QTextEdit):
    returnPressed = Signal()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.setText(self.toPlainText().lower())
            self.returnPressed.emit()
            # Установка выравнивания по центру после ввода текста
            self.setAlignment(Qt.AlignCenter)
        else:
            super().keyPressEvent(event)



class LevelWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Синонимы")

        self.setGeometry(0, 0, 1920, 1080)
        self.move(0, 0)

        # Загрузка изображения
        self.pixmap = QPixmap('blue.png')

        # Установка изображения в качестве фона
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Window, QBrush(self.pixmap))
        self.setPalette(self.palette)

        # Чтение слов и синонимов из файлов
        with codecs.open('слова.txt', 'r', 'utf-8') as f:
            self.words = [word.strip() for word in f]
        self.synonyms = {}
        with codecs.open('синонимы.txt', 'r', 'utf-8') as f:
            for line in f:
                parts = line.strip().split(',')
                word = parts[0]
                word_synonyms = parts[1:]
                self.synonyms[word] = word_synonyms

        # Выбор первого слова из списка
        self.current_word = self.words.pop(0)

        # Создание текстовых полей
        self.text_field_center = QTextEdit(self)
        self.text_field_center.setFont(QFont('Comic Sans', 30))
        self.text_field_center.setStyleSheet("background-color: white; border-radius: 7px; border: 2px solid black;")
        self.text_field_center.setReadOnly(True)  # Пользователь не может вводить текст
        self.text_field_center.setFixedSize(QSize(500, 80))  # Установка фиксированного размера
        self.text_field_center.setText(self.current_word)
        self.text_field_center.setAlignment(Qt.AlignCenter)

        self.text_field_bottom = CustomTextEdit(self)
        self.text_field_bottom.setFont(QFont('Comic Sans', 30))
        self.text_field_bottom.setStyleSheet("background-color: white; border-radius: 7px; border: 2px solid black;")
        self.text_field_bottom.setFixedSize(QSize(500, 80))
        self.text_field_bottom.setAlignment(Qt.AlignCenter)
        self.text_field_bottom.returnPressed.connect(self.check_synonym)  # Подключение слота

        # Создание сообщения о правильности
        self.correct_label = QLabel("ВЕРНО!", self)
        self.correct_label.setFont(QFont('Comic Sans', 30))
        self.correct_label.setStyleSheet("background-color: white; border: 2px solid black; color: green;")
        self.correct_label.move(690,650)
        self.correct_label.adjustSize()
        self.correct_label.hide()  # Скрытие сообщения

        # Создание сообщения о неправильности
        self.incorrect_label = QLabel("НЕВЕРНО!", self)
        self.incorrect_label.setFont(QFont('Comic Sans', 30))
        self.incorrect_label.setStyleSheet("background-color: white; border: 2px solid black; color: red;")
        self.incorrect_label.move(670,650)
        self.incorrect_label.adjustSize()
        self.incorrect_label.hide()  # Скрытие сообщения

        # Создание сообщения о завершении игры
        self.finished_label = QLabel("Поздравляем! Вы прошли игру!", self)
        self.finished_label.setFont(QFont('Comic Sans', 30))
        self.finished_label.setStyleSheet("background-color: white; border: 2px solid black; color: black;")
        self.finished_label.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру
        self.finished_label.adjustSize()
        self.finished_label.hide()  # Скрытие сообщения


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
        layout.addWidget(self.finished_label)  # Добавление метки в макет
        layout.addStretch()

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Создание кнопки паузы
        self.pause_button = QPushButton(self)
        self.pause_button.setIcon(QIcon('pause.png'))
        self.pause_button.setIconSize(QSize(50, 50))
        self.pause_button.setFixedSize(QSize(50, 50))
        self.pause_button.move(10, 10)  # Перемещение кнопки в левый верхний угол
        self.pause_button.setStyleSheet("background-color: transparent; border: none;")
        self.pause_button.clicked.connect(self.show_buttons)  # Подключение слота

        # Создание дополнительных кнопок
        self.quit_button = QPushButton(self)
        self.quit_button.setIcon(QIcon('quit.png'))
        self.quit_button.setIconSize(QSize(50, 50))
        self.quit_button.setFixedSize(QSize(50, 50))
        self.quit_button.move(70, 10)
        self.quit_button.setStyleSheet("background-color: transparent; border: none;")
        self.quit_button.clicked.connect(self.close)  # Подключение слота
        self.quit_button.hide()  # Скрытие кнопки

        self.continue_button = QPushButton(self)
        self.continue_button.setIcon(QIcon('continue.png'))
        self.continue_button.setIconSize(QSize(50, 50))
        self.continue_button.setFixedSize(QSize(50, 50))
        self.continue_button.move(130, 10)
        self.continue_button.setStyleSheet("background-color: transparent; border: none;")
        self.continue_button.clicked.connect(self.hide_buttons)  # Подключение слота
        self.continue_button.hide()  # Скрытие кнопки

        # Создание надписи
        self.level = 1
        self.level_label = QLabel(f"Ур.{self.level}", self)
        self.level_label.setFont(QFont('Comic Sans', 30))
        self.level_label.setStyleSheet("background: transparent; color: black;")
        self.level_label.adjustSize()


    def showEvent(self, event):
        # Позиционирование надписи в правом нижнем углу
        self.level_label.move(self.width() - self.level_label.width() - 10, self.height() - self.level_label.height() - 10)

    def show_buttons(self):
        """Показывает дополнительные кнопки при нажатии на кнопку паузы."""
        self.quit_button.show()
        self.continue_button.show()
        self.text_field_bottom.setReadOnly(True)

    def hide_buttons(self):
        """Скрывает дополнительные кнопки при нажатии на кнопку continue."""
        self.quit_button.hide()
        self.continue_button.hide()
        self.text_field_bottom.setReadOnly(False)

    def check_synonym(self):
        """Проверяет, является ли введенное пользователем слово синонимом отображаемого слова."""
        user_input = self.text_field_bottom.toPlainText().strip().lower()

        if user_input in self.synonyms.get(self.current_word, []):
            # Если введенное пользователем слово является синонимом отображаемого слова
            self.correct_label.show()  # Показать сообщение
            QTimer.singleShot(1000, self.correct_label.hide)  # Скрыть сообщение через 1 секунду
            self.text_field_bottom.clear()  # Очистить нижнее текстовое поле
            self.text_field_bottom.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру в нижнем текстовом поле
            if self.words:  # Если в списке еще есть слова
                self.current_word = self.words.pop(0)  # Выбрать следующее слово из списка
                self.text_field_center.setText(self.current_word)  # Установить новое слово
                self.text_field_center.setAlignment(Qt.AlignCenter)  # Выравнивание текста по центру
            else:
                self.text_field_center.hide()  # Скрыть центральное текстовое поле
                self.text_field_bottom.hide()  # Скрыть нижнее текстовое поле
                self.finished_label.move((self.width() - self.finished_label.width()) // 2, (self.height() - self.finished_label.height()) // 2)  # Позиционирование сообщения по центру экрана
                self.finished_label.show()  # Показать сообщение
            self.level += 1  # Увеличиваем уровень на 1
            self.level_label.setText(f"Ур.{self.level}")  # Обновляем текст метки уровня
            self.level_label.adjustSize()  # Обновляем размер метки уровня
            self.level_label.move(self.width() - self.level_label.width() - 10, self.height() - self.level_label.height() - 10)  # Обновляем позицию метки уровня
        else:
            self.incorrect_label.show()  # Показать сообщение "НЕВЕРНО!"
            QTimer.singleShot(1000, self.incorrect_label.hide)  # Скрыть сообщение через 1 секунду

app = QApplication([])
window = MainWindow()
window.showFullScreen()
sys.exit(app.exec())

