import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QMessageBox


class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.load_button1 = QPushButton('Данные из таблицы "Студенты"')
        layout.addWidget(self.load_button1)

        self.load_button2 = QPushButton('Данные из таблицы "Оценки по английскому"')
        layout.addWidget(self.load_button2)

        self.central_widget.setLayout(layout)

        self.load_button1.clicked.connect(self.load_data_from_students)
        self.load_button2.clicked.connect(self.load_data_from_english_grades)

    def load_data_from_english_grades(self):
        connection = None
        try:
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM english_grades WHERE english_grades = 5')
            result = cursor.fetchall()

            if not result:
                self.text_edit.setPlainText('Данных нет.')
                return

            data_text = 'Данные:\n\n'
            for row in result:
                if len(row) >= 5:
                    data_text += f'Id студента: {row[1]}\n'
                    data_text += f'Оценка по английскому языку: {row[2]}\n'
                else:
                    data_text += 'Недостаточно данных.\n\n'

            self.text_edit.setPlainText(data_text)

        except sqlite3.Error as e:
            QMessageBox.critical(self,  '', f'Ошибка подключения к базе данных: {e}')
        except Exception as e:
            QMessageBox.critical(self, '', f'Произошла ошибка: {e}')
        finally:
            if connection:
                connection.close()

    def load_data_from_students(self):
        connection = None
        try:
            connection = sqlite3.connect('students.db')
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM students')
            result = cursor.fetchall()

            if not result:
                self.text_edit.setPlainText('Данных нет.')
                return

            data_text = 'Данные:\n\n'
            for row in result:
                if len(row) >= 6:  
                    data_text += f'Id Студента: {row[0]}\n'
                    data_text += f'ФИО: {row[1]}'
                    data_text += f'Номер телефона: {row[2]}\n'
                    data_text += f'Адрес: {row[3]}\n\n'
                    data_text += f'Номер курса: {row[4]}\n\n'
                    data_text += f'Номер группы: {row[5]}\n\n'
                else:
                    data_text += 'Недостаточно данных.\n\n'

            self.text_edit.setPlainText(data_text)

        except sqlite3.Error as e:
            QMessageBox.critical(self, '', f'Ошибка подключения к базе данных: {e}')
        except Exception as e:
            QMessageBox.critical(self, '', f'Произошла ошибка: {e}')
        finally:
            if connection:
                connection.close()


def main():
    app = QApplication(sys.argv)
    window = DatabaseViewer()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
