import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit, QPushButton, QLabel
from PyQt5.QtCore import QDate

class DateSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.date_edit = QDateEdit(self)
        self.date_edit.setCalendarPopup(True)

        # Definindo a data mínima como 1 de janeiro de 2024
        min_date = QDate(2024, 1, 1)
        self.date_edit.setMinimumDate(min_date)

        # Definindo a data inicial como 1 de janeiro de 2024
        initial_date = QDate(2024, 1, 1)
        self.date_edit.setDate(initial_date)

        layout.addWidget(self.date_edit)

        self.print_button = QPushButton('Imprimir Data', self)
        self.print_button.clicked.connect(self.printDate)
        layout.addWidget(self.print_button)

        # Rótulo para exibir a data selecionada
        self.date_label = QLabel('Nenhuma data selecionada', self)
        layout.addWidget(self.date_label)

        self.setLayout(layout)
        self.setWindowTitle('Selecionar Data')
        self.show()

        # Definindo um estilo básico
        self.setStyleSheet("QWidget { background-color: white; color: black; }"
                           "QDateEdit { background-color: white; color: black; }"
                           "QDateEdit::down-arrow { image: url(down-arrow.png); }"
                           "QDateEdit::drop-down { subcontrol-origin: padding; subcontrol-position: top right; width: 20px; border-left-width: 1px; border-left-color: #8f8f91; border-left-style: solid; }")

    def printDate(self):
        selected_date = self.date_edit.date().toString('dd/MM/yyyy')
        self.date_label.setText(f'A data selecionada é: {selected_date}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateSelector()
    sys.exit(app.exec_())
