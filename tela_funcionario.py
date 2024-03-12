from PyQt5 import QtCore, QtGui, QtWidgets
import sys, imagens_rc


class Ui_TelaServidor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1227, 798)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 34, 42, 255), stop:1 rgba(58, 96, 115, 255));")
        self.label_logo_top = QtWidgets.QLabel(Form)
        self.label_logo_top.setGeometry(QtCore.QRect(10, -50, 201, 191))
        self.label_logo_top.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.label_logo_top.setText("")
        self.label_logo_top.setPixmap(QtGui.QPixmap(":/imagens/logo.png"))
        self.label_logo_top.setScaledContents(True)
        self.label_logo_top.setObjectName("label_logo_top")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 1231, 101))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(820, 110, 391, 311))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 0.35);\n"
"border-radius:20px;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 191, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(70, 50, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_nome.setFont(font)
        self.lineEdit_nome.setWhatsThis("")
        self.lineEdit_nome.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_nome.setInputMask("")
        self.lineEdit_nome.setText("")
        self.lineEdit_nome.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.valor_consulta = QtWidgets.QLineEdit(self.widget)
        self.valor_consulta.setGeometry(QtCore.QRect(70, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.valor_consulta.setFont(font)
        self.valor_consulta.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.valor_consulta.setText("")
        self.valor_consulta.setAlignment(QtCore.Qt.AlignCenter)
        self.valor_consulta.setObjectName("lineEdit_comboBox")
        self.lineEdit_Senha = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Senha.setGeometry(QtCore.QRect(70, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Senha.setFont(font)
        self.lineEdit_Senha.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_Senha.setText("")
        self.lineEdit_Senha.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Senha.setObjectName("lineEdit_Senha")
        self.pushButton_cadastrar_medico = QtWidgets.QPushButton(self.widget)
        self.pushButton_cadastrar_medico.setGeometry(QtCore.QRect(140, 260, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastrar_medico.setFont(font)
        self.pushButton_cadastrar_medico.setStyleSheet("QPushButton#pushButton_cadastrar_medico {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_cadastrar_medico:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_cadastrar_medico:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_cadastrar_medico.setObjectName("pushButton_cadastrar_medico")
        self.lineEdit_Especialidade = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Especialidade.setGeometry(QtCore.QRect(70, 210, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Especialidade.setFont(font)
        self.lineEdit_Especialidade.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_Especialidade.setText("")
        self.lineEdit_Especialidade.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Especialidade.setObjectName("lineEdit_Especialidade")
        self.lineEdit_Crm = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Crm.setGeometry(QtCore.QRect(70, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Crm.setFont(font)
        self.lineEdit_Crm.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_Crm.setText("")
        self.lineEdit_Crm.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Crm.setObjectName("lineEdit_Crm")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 430, 1211, 341))
        self.widget_2.setStyleSheet("background-color: rgba(0, 0, 0, 0.35);\n"
"border-radius:20px;")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(500, 10, 231, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 871, 281))
        self.tableWidget.setStyleSheet("background-color: rgba(225, 225, 225, 0.1);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.lineEdit_nome_escala = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_nome_escala.setGeometry(QtCore.QRect(940, 170, 221, 31))
        self.lineEdit_nome_escala.setFont(font)
        self.lineEdit_nome_escala.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_nome_escala.setText("")
        self.lineEdit_nome_escala.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_nome_escala.setObjectName("lineEdit_nome_escala")
        self.pushButton_cadastrar_funcionario = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_cadastrar_funcionario.setGeometry(QtCore.QRect(990, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cadastrar_funcionario.setFont(font)
        self.pushButton_cadastrar_funcionario.setStyleSheet("QPushButton#pushButton_cadastrar_funcionario {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_cadastrar_funcionario:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_cadastrar_funcionario:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_cadastrar_funcionario.setObjectName("pushButton_cadastrar_funcionario")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(910, 120, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(1010, 140, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.widget_4 = QtWidgets.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(20, 110, 411, 311))
        self.widget_4.setStyleSheet("background-color: rgba(0, 0, 0, 0.35);\n"
"border-radius:20px;")
        self.widget_4.setObjectName("widget_4")
        self.label_text_quartos = QtWidgets.QLabel(self.widget_4)
        self.label_text_quartos.setGeometry(QtCore.QRect(100, 10, 201, 21))
        self.label_text_quartos.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_text_quartos.setObjectName("label_text_quartos")
        self.listWidget_quartos = QtWidgets.QListWidget(self.widget_4)
        self.listWidget_quartos.setGeometry(QtCore.QRect(10, 50, 256, 231))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_quartos.setFont(font)
        self.listWidget_quartos.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget_quartos.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"color: rgb(255, 255, 255);")
        self.listWidget_quartos.setObjectName("listWidget_quartos")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_quartos.addItem(item)
        self.pushButton_ocupado = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_ocupado.setGeometry(QtCore.QRect(280, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ocupado.setFont(font)
        self.pushButton_ocupado.setStyleSheet("QPushButton#pushButton_ocupado {\n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(250, 0, 0, 255), stop:1 rgba(170, 0, 0, 255));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_ocupado:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.0298507, y1:0.068, x2:1, y2:1, stop:0.189055 rgba(255, 165, 165, 255), stop:0.970149 rgba(255, 169, 169, 168), stop:1 rgba(206, 255, 183, 168));\n"
"}\n"
"\n"
"QPushButton#pushButton_ocupado:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.0298507, y1:0.068, x2:1, y2:1, stop:0.189055 rgba(255, 165, 165, 255), stop:0.970149 rgba(255, 169, 169, 168), stop:1 rgba(206, 255, 183, 168));\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_ocupado.setObjectName("pushButton_ocupado")
        self.pushButton_livre = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_livre.setGeometry(QtCore.QRect(280, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_livre.setFont(font)
        self.pushButton_livre.setStyleSheet("QPushButton#pushButton_livre {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 209, 0, 255), stop:1 rgba(0, 132, 0, 255));\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_livre:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.0298507, y1:0.068, x2:1, y2:1, stop:0.189055 rgba(195, 255, 179, 255), stop:1 rgba(206, 255, 183, 168));\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_livre:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"   background-color: qlineargradient(spread:pad, x1:0.0298507, y1:0.068, x2:1, y2:1, stop:0.189055 rgba(195, 255, 179, 255), stop:1 rgba(206, 255, 183, 168));\n"
"}\n"
"\n"
"")
        self.pushButton_livre.setObjectName("pushButton_livre")
        self.lineEdit_Dias_reserva = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_Dias_reserva.setGeometry(QtCore.QRect(280, 91, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Dias_reserva.setFont(font)
        self.lineEdit_Dias_reserva.setWhatsThis("")
        self.lineEdit_Dias_reserva.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_Dias_reserva.setInputMask("")
        self.lineEdit_Dias_reserva.setText("")
        self.lineEdit_Dias_reserva.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Dias_reserva.setObjectName("lineEdit_Dias_reserva")
        self.widget_5 = QtWidgets.QWidget(Form)
        self.widget_5.setGeometry(QtCore.QRect(440, 110, 371, 311))
        self.widget_5.setStyleSheet("background-color: rgba(0, 0, 0, 0.35);\n"
"border-radius:20px;")
        self.widget_5.setObjectName("widget_5")
        self.listWidget_estoque_remedios = QtWidgets.QListWidget(self.widget_5)
        self.listWidget_estoque_remedios.setGeometry(QtCore.QRect(50, 40, 271, 201))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_estoque_remedios.setFont(font)
        self.listWidget_estoque_remedios.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"color: rgb(255, 255, 255);")
        self.listWidget_estoque_remedios.setObjectName("listWidget_estoque_remedios")
        self.lineEdit_remedio_padicionar = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_remedio_padicionar.setGeometry(QtCore.QRect(30, 260, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_remedio_padicionar.setFont(font)
        self.lineEdit_remedio_padicionar.setStyleSheet("background-color: rgba(255, 255, 255, 0.1);\n"
"border-radius:9px;\n"
"")
        self.lineEdit_remedio_padicionar.setText("")
        self.lineEdit_remedio_padicionar.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_remedio_padicionar.setObjectName("lineEdit_remedio_padicionar")
        self.pushButton_adicionar_medicamento = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_adicionar_medicamento.setGeometry(QtCore.QRect(250, 262, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_adicionar_medicamento.setFont(font)
        self.pushButton_adicionar_medicamento.setStyleSheet("QPushButton#pushButton_adicionar_medicamento {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_adicionar_medicamento:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_adicionar_medicamento:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_adicionar_medicamento.setObjectName("pushButton_adicionar_medicamento")
        self.label_text_remed = QtWidgets.QLabel(self.widget_5)
        self.label_text_remed.setGeometry(QtCore.QRect(90, 10, 201, 21))
        self.label_text_remed.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_text_remed.setObjectName("label_text_remed")
        self.label_txt = QtWidgets.QLabel(self.widget_5)
        self.label_txt.setGeometry(QtCore.QRect(10, 244, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_txt.setFont(font)
        self.label_txt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.label_txt.setText("")
        self.label_txt.setObjectName("label_txt")
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_voltar = QtWidgets.QPushButton(Form)
        self.pushButton_voltar.setGeometry(QtCore.QRect(5, 765, 80, 31))
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
        self.pushButton_fechar.setGeometry(QtCore.QRect(1190, 765, 30, 31))
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
        self.label.raise_()
        self.label_logo_top.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.widget_4.raise_()
        self.widget_5.raise_()
        self.pushButton_voltar.raise_()
        self.pushButton_fechar.raise_()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Cadastre um Médico</span></p></body></html>"))
        self.lineEdit_nome.setPlaceholderText(_translate("Form", "N o m e"))
        self.valor_consulta.setPlaceholderText(_translate("Form", "V A L O R"))
        self.lineEdit_Senha.setPlaceholderText(_translate("Form", "S e n h a"))
        self.pushButton_cadastrar_medico.setText(_translate("Form", "Cadastrar"))
        self.lineEdit_Especialidade.setPlaceholderText(_translate("Form", "E s p e c i a l i d a d e"))
        self.lineEdit_Crm.setPlaceholderText(_translate("Form", "C R M"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Escala de funcionarios</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Segunda - Feira"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Terça - Feira"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Quarta - Feira"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Quinta - feira"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sexta - feira"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Sábado"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Domingo"))
        self.pushButton_cadastrar_funcionario.setText(_translate("Form", "Adicionar"))
        self.label_5.setText(_translate("Form", "Digite o nome de um funcionario para adicionar "))
        self.label_6.setText(_translate("Form", "na escala"))
        self.label_text_quartos.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Alocação dos Quartos</span></p></body></html>"))
        __sortingEnabled = self.listWidget_quartos.isSortingEnabled()
        self.listWidget_quartos.setSortingEnabled(False)
        item = self.listWidget_quartos.item(0)
        item.setText(_translate("Form", "Quarto 01"))
        item = self.listWidget_quartos.item(1)
        item.setText(_translate("Form", "Quarto 02"))
        item = self.listWidget_quartos.item(2)
        item.setText(_translate("Form", "Quarto 03"))
        item = self.listWidget_quartos.item(3)
        item.setText(_translate("Form", "Quarto 04"))
        item = self.listWidget_quartos.item(4)
        item.setText(_translate("Form", "Quarto 05"))
        item = self.listWidget_quartos.item(5)
        item.setText(_translate("Form", "Quarto 06"))
        item = self.listWidget_quartos.item(6)
        item.setText(_translate("Form", "Quarto 07"))
        item = self.listWidget_quartos.item(7)
        item.setText(_translate("Form", "Quarto 08"))
        item = self.listWidget_quartos.item(8)
        item.setText(_translate("Form", "Quarto 09"))
        item = self.listWidget_quartos.item(9)
        item.setText(_translate("Form", "Quarto 10"))
        item = self.listWidget_quartos.item(10)
        item.setText(_translate("Form", "Quarto 11"))
        item = self.listWidget_quartos.item(11)
        item.setText(_translate("Form", "Quarto 12"))
        item = self.listWidget_quartos.item(12)
        item.setText(_translate("Form", "Quarto 13"))
        item = self.listWidget_quartos.item(13)
        item.setText(_translate("Form", "Quarto 14"))
        item = self.listWidget_quartos.item(14)
        item.setText(_translate("Form", "Quarto 15"))
        self.listWidget_quartos.setSortingEnabled(__sortingEnabled)
        self.pushButton_ocupado.setToolTip(_translate("Form", "<html><head/><body><p>Ocupado</p></body></html>"))
        self.pushButton_ocupado.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Ocupado</span></p></body></html>"))
        self.pushButton_ocupado.setText(_translate("Form", "Reservar"))
        self.pushButton_livre.setText(_translate("Form", "Desocupar"))
        self.lineEdit_Dias_reserva.setPlaceholderText(_translate("Form", "Dias"))
        self.lineEdit_remedio_padicionar.setPlaceholderText(_translate("Form", "Qntd / nome do medicamento"))
        self.lineEdit_nome_escala.setPlaceholderText(_translate("Form", "Nome"))
        self.pushButton_adicionar_medicamento.setText(_translate("Form", "Adicionar"))
        self.label_text_remed.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Estoque de remedios</span></p></body></html>"))
        self.pushButton_voltar.setText(_translate("Form", "<-- Voltar"))
        self.pushButton_fechar.setText(_translate("Form", "X"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_TelaServidor()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
