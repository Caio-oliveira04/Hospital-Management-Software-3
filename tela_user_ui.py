from PyQt5 import QtCore, QtGui, QtWidgets
import sys, visual_tela2
from Usuario import Usuario
from PyQt5.QtCore import QDate

usuario1 = Usuario()

class Ui_TelaUser(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1227, 778)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 34, 42, 255), stop:1 rgba(58, 96, 115, 255));")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(10, -50, 201, 191))
        self.label_logo.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/imagens/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 1231, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_img_medico = QtWidgets.QLabel(Form)
        self.label_img_medico.setGeometry(QtCore.QRect(30, 190, 261, 221))
        self.label_img_medico.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_img_medico.setText("")
        self.label_img_medico.setPixmap(QtGui.QPixmap(":/imagens/ilustracao-em-vetor-medico-retrato-de-medico-masculino-isolado-em-branco-ilustracao-medica_659981-7-PhotoRoom.png-PhotoRoom.png"))
        self.label_img_medico.setScaledContents(True)
        self.label_img_medico.setObjectName("label_img_medico")
        self.comboBox_especialistas = QtWidgets.QComboBox(Form)
        self.comboBox_especialistas.setGeometry(QtCore.QRect(120, 170, 301, 31))
        self.comboBox_especialistas.setStyleSheet("background-color: rgba(176, 244, 176,200);")
        self.comboBox_especialistas.setObjectName("comboBox_especialistas")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(70, 460, 401, 211))
        self.calendarWidget.setStyleSheet("color: rgb(0, 0, 0);\n" "background-color: rgb(184, 255, 184);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_text_dia = QtWidgets.QLabel(Form)
        self.label_text_dia.setGeometry(QtCore.QRect(80, 400, 441, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_dia.setFont(font)
        self.label_text_dia.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_dia.setObjectName("label_text_dia")
        self.label_text_escolha = QtWidgets.QLabel(Form)
        self.label_text_escolha.setGeometry(QtCore.QRect(130, 120, 441, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_escolha.setFont(font)
        self.label_text_escolha.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_escolha.setObjectName("label_text_escolha")
        self.label_text_info_medico = QtWidgets.QLabel(Form)
        self.label_text_info_medico.setGeometry(QtCore.QRect(240, 210, 271, 201))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_text_info_medico.setFont(font)
        self.label_text_info_medico.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_info_medico.setObjectName("label_text_info_medico")
        self.pushButton_marcar = QtWidgets.QPushButton(Form)
        self.pushButton_marcar.setGeometry(QtCore.QRect(180, 690, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_marcar.setFont(font)
        self.pushButton_marcar.setStyleSheet("\n"
"QPushButton#pushButton_confirmar {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_confirmar:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_confirmar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_confirmar { \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_marcar.setText("MARCAR")
        self.pushButton_marcar.setIconSize(QtCore.QSize(7, 7))
        self.pushButton_marcar.setObjectName("pushButton_confirmar")
        self.label_imagem_sobreposicao = QtWidgets.QLabel(Form)
        self.label_imagem_sobreposicao.setGeometry(QtCore.QRect(30, 120, 491, 641))
        self.label_imagem_sobreposicao.setStyleSheet("background-color:rgba(0,0,0,80);\n" "border-radius:50px;\n""")
        self.label_imagem_sobreposicao.setText("")
        self.label_imagem_sobreposicao.setObjectName("label_imagem_sobreposicao")
        self.label_fundo_cadastro = QtWidgets.QLabel(Form)
        self.label_fundo_cadastro.setGeometry(QtCore.QRect(560, 120, 631, 641))
        self.label_fundo_cadastro.setStyleSheet("background-color: rgba(0, 0, 0,90);\n""border-radius:50px;")
        self.label_fundo_cadastro.setText("")
        self.label_fundo_cadastro.setObjectName("label_fundo_cadastro")
        self.label_text_marcadas = QtWidgets.QLabel(Form)
        self.label_text_marcadas.setGeometry(QtCore.QRect(645, 120, 441, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_marcadas.setFont(font)
        self.label_text_marcadas.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(184, 255, 184);")
        self.label_text_marcadas.setObjectName("label_text_marcadas")
        self.listWidget_marcadas = QtWidgets.QListWidget(Form)
        self.listWidget_marcadas.setGeometry(QtCore.QRect(610, 170, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_marcadas.setFont(font)
        self.listWidget_marcadas.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(225,225,225);")
        self.listWidget_marcadas.setObjectName("listWidget_marcadas")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.dateEdit_par_remarcar = QtWidgets.QDateEdit(Form)
        self.dateEdit_par_remarcar.setCalendarPopup(True)
        self.dateEdit_par_remarcar.setGeometry(QtCore.QRect(1010, 180, 141, 41))

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        min_date = QDate(2024, 1, 1)
        initial_date = QDate(2024, 1, 1)
        self.dateEdit_par_remarcar.setDate(initial_date)
        self.dateEdit_par_remarcar.setMinimumDate(min_date)
        self.dateEdit_par_remarcar.setFont(font)
        self.dateEdit_par_remarcar.setStyleSheet("background-color: white; color: black")
        self.dateEdit_par_remarcar.setObjectName("dateEdit_par_remarcar")
        self.pushButton_remarcar = QtWidgets.QPushButton(Form)
        self.pushButton_remarcar.setGeometry(QtCore.QRect(1010, 230, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_remarcar.setFont(font)
        self.pushButton_remarcar.setStyleSheet("QPushButton#pushButton_remarcar {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_remarcar:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_remarcar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"QPushButton#pushButton_remarcar { \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_remarcar.setObjectName("pushButton_remarcar")
        self.pushButton_desmarcar = QtWidgets.QPushButton(Form)
        self.pushButton_desmarcar.setGeometry(QtCore.QRect(1010, 270, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_desmarcar.setFont(font)
        self.pushButton_desmarcar.setStyleSheet("QPushButton#pushButton_desmarcar {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_desmarcar:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_desmarcar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"QPushButton#pushButton_desmarcar\n"
" { \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_desmarcar.setObjectName("pushButton_desmarcar")
        self.label_text_solicitados = QtWidgets.QLabel(Form)
        self.label_text_solicitados.setGeometry(QtCore.QRect(660, 330, 441, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_solicitados.setFont(font)
        self.label_text_solicitados.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_solicitados.setObjectName("label_text_solicitados")
        self.label_text_feitos = QtWidgets.QLabel(Form)
        self.label_text_feitos.setGeometry(QtCore.QRect(690, 480, 441, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_feitos.setFont(font)
        self.label_text_feitos.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_feitos.setObjectName("label_text_feitos")
        self.pushButton_marcar_exame = QtWidgets.QPushButton(Form)
        self.pushButton_marcar_exame.setGeometry(QtCore.QRect(1010, 390, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_marcar_exame.setFont(font)
        self.pushButton_marcar_exame.setStyleSheet("QPushButton#pushButton_marcar_exame {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_marcar_exame:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_marcar_exame:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"QPushButton#pushButton_marcar_exame { \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_marcar_exame.setObjectName("pushButton_marcar_exame")
        self.pushButton_ver_resultado = QtWidgets.QPushButton(Form)
        self.pushButton_ver_resultado.setGeometry(QtCore.QRect(1010, 550, 141, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ver_resultado.setFont(font)
        self.pushButton_ver_resultado.setStyleSheet("QPushButton#pushButton_ver_resultado {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_ver_resultado:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_ver_resultado:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"QPushButton#pushButton_ver_resultado { \n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_ver_resultado.setObjectName("pushButton_ver_resultado")
        self.label_text_resultados = QtWidgets.QLabel(Form)
        self.label_text_resultados.setGeometry(QtCore.QRect(720, 621, 171, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_text_resultados.setFont(font)
        self.label_text_resultados.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(184, 255, 184);")
        self.label_text_resultados.setObjectName("label_text_resultados")
        self.label_ver_resultados = QtWidgets.QLabel(Form)
        self.label_ver_resultados.setGeometry(QtCore.QRect(610, 670, 381, 61))
        self.label_ver_resultados.setStyleSheet("background-color: rgba(255, 255, 255,0.08);\n" "border-radius: 25px;\n" "")
        self.label_ver_resultados.setObjectName("label_ver_resultados")
        self.listWidget_solcitados = QtWidgets.QListWidget(Form)
        self.listWidget_solcitados.setGeometry(QtCore.QRect(610, 380, 391, 101))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_solcitados.setFont(font)
        self.listWidget_solcitados.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(225,225,225);")
        self.listWidget_solcitados.setObjectName("listWidget_solcitados")
        self.listWidget_feitos = QtWidgets.QListWidget(Form)
        self.listWidget_feitos.setGeometry(QtCore.QRect(610, 530, 391, 101))
        font = QtGui.QFont()
        font.setFamily("Elephant")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_feitos.setFont(font)
        self.listWidget_feitos.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(225,225,225);")
        self.listWidget_feitos.setObjectName("listWidget_feitos")
        self.label_saldo = QtWidgets.QLabel(Form)
        self.label_saldo.setGeometry(QtCore.QRect(900, 0, 230, 61))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(13)
        self.label_saldo.setFont(font)
        self.label_saldo.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n" "color: rgb(0, 0, 0);")
        self.label_saldo.setObjectName("label_saldo")
        self.pushButton_depositar = QtWidgets.QPushButton(Form)
        self.pushButton_depositar.setGeometry(QtCore.QRect(1090, 50, 61, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_voltar = QtWidgets.QPushButton(Form)
        self.pushButton_voltar.setGeometry(QtCore.QRect(5, 745, 80, 31))
        self.pushButton_voltar.setFont(font)
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.pushButton_voltar.setStyleSheet("""
        QPushButton {
            background-color: white;
            border-radius:8px;
        }
        QPushButton:hover {
            background-color: #EEEEEE; 
        }
        QPushButton:pressed {
            background-color: #DDDDDD;
        }""")
        self.pushButton_fechar = QtWidgets.QPushButton(Form)
        self.pushButton_fechar.setGeometry(QtCore.QRect(1190, 745, 30, 31))
        self.pushButton_fechar.setFont(font)
        self.pushButton_fechar.setObjectName("pushButton_fechar")
        self.pushButton_fechar.setStyleSheet("""
        QPushButton {
            color:white;                                
            background-color: red;
            border-radius:8px;
        }
        QPushButton:hover {
            background-color: #EEEEEE; 
        }
        QPushButton:pressed {
            background-color: #DDDDDD;
        }""")


        font = QtGui.QFont()
        font.setPointSize(6)
        self.pushButton_depositar.setFont(font)
        self.pushButton_depositar.setStyleSheet("QPushButton#pushButton_depositar {\n"
"       background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(184, 255, 184, 255), stop:1 rgba(89, 124, 89, 255));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_depositar:hover {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"\n"
"QPushButton#pushButton_depositar:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(135, 193, 255, 255), stop:1 rgba(100, 138, 149, 255));\n"
"}\n"
"QPushButton#pushButton_depositar { \n"
"    color: rgb(0, 0, 0);\n"
"}")


        self.pushButton_depositar.setObjectName("pushButton_depositar")
        self.lineEdit_valor_deposito = QtWidgets.QLineEdit(Form)
        self.lineEdit_valor_deposito.setGeometry(QtCore.QRect(870, 50, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_valor_deposito.setFont(font)
        self.lineEdit_valor_deposito.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_valor_deposito.setStyleSheet("    width: 450px;\n"
"       height: 65px;\n"
"       border-radius: 15px; /* Ajuste o valor conforme necessário */\n"
"       background: rgba(0,0,0, 0.2);\n"
"       border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_valor_deposito.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_valor_deposito.setClearButtonEnabled(True)
        self.lineEdit_valor_deposito.setObjectName("lineEdit_valor_deposito")
        self.label_imagem_sobreposicao.raise_()
        self.label_2.raise_()
        self.label_img_medico.raise_()
        self.comboBox_especialistas.raise_()
        self.label_logo.raise_()
        self.calendarWidget.raise_()
        self.label_text_dia.raise_()
        self.label_text_escolha.raise_()
        self.label_text_info_medico.raise_()
        self.pushButton_marcar.raise_()
        self.label_fundo_cadastro.raise_()
        self.label_text_marcadas.raise_()
        self.listWidget_marcadas.raise_()
        self.pushButton_remarcar.raise_()
        self.pushButton_desmarcar.raise_()
        self.label_text_solicitados.raise_()
        self.label_text_feitos.raise_()
        self.pushButton_marcar_exame.raise_()
        self.pushButton_ver_resultado.raise_()
        self.label_text_resultados.raise_()
        self.label_ver_resultados.raise_()
        self.listWidget_solcitados.raise_()
        self.listWidget_feitos.raise_()
        self.label_saldo.raise_()
        self.pushButton_depositar.raise_()
        self.lineEdit_valor_deposito.raise_()
        self.pushButton_voltar.raise_()
        self.pushButton_fechar.raise_()
        self.dateEdit_par_remarcar.raise_()

        self.crm = ''
        self.nome = ''
        self.especialidade = ''
        self.lista_medicos = []
        self.print()
        self.set_combox()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

     
    def set_crm(self, crm):
        self.crm = crm
    
    def set_nome(self, nome):
        self.nome = nome

    def set_especialidade(self, especialidade):
        self.especialidade = especialidade

    def print(self):
        self.label_text_info_medico.setText(f"Crm: {self.crm}\n\nNome: {self.nome}\n\nEspecialidade: {self.especialidade}")
    
    def set_lista_medicos(self, lista):
        self.lista_medicos = lista

    def set_combox(self):
        self.comboBox_especialistas.clear()
        self.comboBox_especialistas.addItem("...")

        for medico in self.lista_medicos:
                self.comboBox_especialistas.addItem(medico)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form")) 
        self.pushButton_depositar.setText(_translate("Form", "Depositar"))
        self.label_text_dia.setText(_translate("Form", "escolha o dia para a consulta "))
        self.label_text_escolha.setText(_translate("Form", "escolha o especialista"))
        self.pushButton_marcar.setWhatsThis(_translate("Form", "<html><head/><body><p>SLA</p><p><br/></p></body></html>"))
        self.label_text_marcadas.setText(_translate("Form", "CONSULTAS MARCADAS"))
        __sortingEnabled = self.listWidget_marcadas.isSortingEnabled()
        self.listWidget_marcadas.setSortingEnabled(False)
        self.listWidget_marcadas.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_solcitados.isSortingEnabled()
        self.listWidget_solcitados.setSortingEnabled(False)
        self.listWidget_solcitados.setSortingEnabled(__sortingEnabled)
        self.pushButton_remarcar.setText(_translate("Form", "REMARCAR"))
        self.pushButton_desmarcar.setText(_translate("Form", "DESMARCAR"))
        self.label_text_solicitados.setText(_translate("Form", "EXAMES SOLICITADOS "))
        self.label_text_feitos.setText(_translate("Form", "EXAMES FEITOS"))
        self.pushButton_marcar_exame.setText(_translate("Form", "MARCAR"))
        self.pushButton_ver_resultado.setText(_translate("Form", "VER RESULTADO"))
        self.label_text_resultados.setText(_translate("Form", "RESULTADO"))
        __sortingEnabled = self.listWidget_feitos.isSortingEnabled()
        self.listWidget_feitos.setSortingEnabled(False)
        self.listWidget_feitos.setSortingEnabled(__sortingEnabled)
        self.lineEdit_valor_deposito.setPlaceholderText(_translate("Form", "VALOR P/ DEPOSITAR"))
        self.pushButton_voltar.setText(_translate("Form", "<-- Voltar"))
        self.pushButton_fechar.setText(_translate("Form", "X"))

   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaUser()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


