from PyQt5 import QtCore, QtGui, QtWidgets
import sys, imagens_rc
from Usuario import Usuario

class UI_LoginUser(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1227, 778)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 34, 42, 255), stop:1 rgba(58, 96, 115, 255));")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(200, 130, 301, 591))
        self.widget.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.widget.setObjectName("widget")
        self.label_imagem_login = QtWidgets.QLabel(self.widget)
        self.label_imagem_login.setGeometry(QtCore.QRect(10, 20, 391, 541))
        self.label_imagem_login.setStyleSheet("border-image: url(:/imagens/background enfermeiros.jpg);\n"
"border-top-left-radius:60px;")
        self.label_imagem_login.setText("")
        self.label_imagem_login.setObjectName("label_imagem_login")
        self.label_imagem_sobreposicao = QtWidgets.QLabel(self.widget)
        self.label_imagem_sobreposicao.setGeometry(QtCore.QRect(10, 20, 391, 541))
        self.label_imagem_sobreposicao.setStyleSheet("background-color:rgba(0,0,0,80);\n"
"border-top-left-radius:60px;\n"
"")
        self.label_imagem_sobreposicao.setText("")
        self.label_imagem_sobreposicao.setObjectName("label_imagem_sobreposicao")
        self.label_text_login = QtWidgets.QLabel(self.widget)
        self.label_text_login.setGeometry(QtCore.QRect(70, 12, 401, 141))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_text_login.setFont(font)
        self.label_text_login.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_text_login.setWhatsThis("")
        self.label_text_login.setStyleSheet("QLabel {\n"
"    color:rgba(22, 34, 42, 255);\n"
"    letter-spacing: 1.5px; /* Ajuste o valor conforme necessário */\n"
"}\n"
"")
        self.label_text_login.setObjectName("label_text_login")
        self.pushButton_login = QtWidgets.QPushButton(self.widget)
        self.pushButton_login.setGeometry(QtCore.QRect(60, 250, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton#pushButton_login {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"\n"
"QPushButton#pushButton_login:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_login:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_login.setIconSize(QtCore.QSize(7, 7))
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit_email_login = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email_login.setGeometry(QtCore.QRect(90, 140, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_email_login.setFont(font)
        self.lineEdit_email_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_email_login.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-right-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_email_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email_login.setClearButtonEnabled(True)
        self.lineEdit_email_login.setObjectName("lineEdit_email_login")
        self.lineEdit_senha_login = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_senha_login.setGeometry(QtCore.QRect(90, 190, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_senha_login.setFont(font)
        self.lineEdit_senha_login.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-right-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_senha_login.setClearButtonEnabled(True)
        self.lineEdit_senha_login.setObjectName("lineEdit_senha_login")
        self.label_imagem_cadeado_login = QtWidgets.QLabel(self.widget)
        self.label_imagem_cadeado_login.setGeometry(QtCore.QRect(60, 193, 28, 25))
        self.label_imagem_cadeado_login.setText("")
        self.label_imagem_cadeado_login.setPixmap(QtGui.QPixmap(":/imagens/icons8-cadeado-48.png"))
        self.label_imagem_cadeado_login.setScaledContents(True)
        self.label_imagem_cadeado_login.setObjectName("label_imagem_cadeado_login")
        self.label_imagem_email = QtWidgets.QLabel(self.widget)
        self.label_imagem_email.setGeometry(QtCore.QRect(60, 143, 27, 27))
        self.label_imagem_email.setText("")
        self.label_imagem_email.setPixmap(QtGui.QPixmap(":/imagens/icons8-nova-mensagem-48.png"))
        self.label_imagem_email.setScaledContents(True)
        self.label_imagem_email.setObjectName("label_imagem_email")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 140, 41, 31))
        self.label_4.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 41, 31))
        self.label_5.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_imagem_login.raise_()
        self.label_imagem_sobreposicao.raise_()
        self.pushButton_login.raise_()
        self.label_imagem_cadeado_login.raise_()
        self.lineEdit_senha_login.raise_()
        self.label_imagem_email.raise_()
        self.lineEdit_email_login.raise_()
        self.label_text_login.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(500, 150, 531, 541))
        self.widget_2.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label_fundo_cadastro = QtWidgets.QLabel(self.widget_2)
        self.label_fundo_cadastro.setGeometry(QtCore.QRect(0, 0, 531, 541))
        self.label_fundo_cadastro.setStyleSheet("background-color: rgba(0, 0, 0,90);\n"
"border-bottom-right-radius:50px;")
        self.label_fundo_cadastro.setText("")
        self.label_fundo_cadastro.setObjectName("label_fundo_cadastro")
        self.label_imagem_usuario_cad = QtWidgets.QLabel(self.widget_2)
        self.label_imagem_usuario_cad.setGeometry(QtCore.QRect(126, 155, 31, 31))
        self.label_imagem_usuario_cad.setStyleSheet("color: rgb(85, 255, 255);")
        self.label_imagem_usuario_cad.setText("")
        self.label_imagem_usuario_cad.setPixmap(QtGui.QPixmap(":/imagens/icons8-usuário-48.png"))
        self.label_imagem_usuario_cad.setScaledContents(True)
        self.label_imagem_usuario_cad.setWordWrap(False)
        self.label_imagem_usuario_cad.setIndent(-100)
        self.label_imagem_usuario_cad.setOpenExternalLinks(True)
        self.label_imagem_usuario_cad.setObjectName("label_imagem_usuario_cad")
        self.label_imagem_email_cad = QtWidgets.QLabel(self.widget_2)
        self.label_imagem_email_cad.setGeometry(QtCore.QRect(126, 235, 30, 30))
        self.label_imagem_email_cad.setText("")
        self.label_imagem_email_cad.setPixmap(QtGui.QPixmap(":/imagens/icons8-nova-mensagem-48.png"))
        self.label_imagem_email_cad.setScaledContents(True)
        self.label_imagem_email_cad.setObjectName("label_imagem_email_cad")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(126, 314, 31, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/imagens/icons8-cadeado-48.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.lineEdit_usuario_cadastro = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_usuario_cadastro.setGeometry(QtCore.QRect(160, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_usuario_cadastro.setFont(font)
        self.lineEdit_usuario_cadastro.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-right-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_usuario_cadastro.setCursorPosition(0)
        self.lineEdit_usuario_cadastro.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_usuario_cadastro.setClearButtonEnabled(True)
        self.lineEdit_usuario_cadastro.setObjectName("lineEdit_usuario_cadastro")
        self.lineEdit_email_cadastro = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_email_cadastro.setGeometry(QtCore.QRect(160, 230, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_email_cadastro.setFont(font)
        self.lineEdit_email_cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_email_cadastro.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-right-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_email_cadastro.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_email_cadastro.setClearButtonEnabled(True)
        self.lineEdit_email_cadastro.setObjectName("lineEdit_email_cadastro")
        self.label_text_cadastrese = QtWidgets.QLabel(self.widget_2)
        self.label_text_cadastrese.setGeometry(QtCore.QRect(120, -12, 401, 141))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_text_cadastrese.setFont(font)
        self.label_text_cadastrese.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_text_cadastrese.setWhatsThis("")
        self.label_text_cadastrese.setStyleSheet("\n"
"QLabel {\n"
"    color:rgba(225,225,255,100);\n"
"    letter-spacing: 5px; /* Ajuste o valor conforme necessário */\n"
"}\n"
"")
        self.label_text_cadastrese.setObjectName("label_text_cadastrese")
        self.pushButton_cadatro = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_cadatro.setGeometry(QtCore.QRect(220, 400, 181, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cadatro.setFont(font)
        self.pushButton_cadatro.setStyleSheet("QPushButton#pushButton_cadatro {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_cadatro:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"\n"
"QPushButton#pushButton_cadatro:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_cadatro.setIconSize(QtCore.QSize(7, 7))
        self.pushButton_cadatro.setObjectName("pushButton_cadatro")
        self.label_nome_git = QtWidgets.QLabel(self.widget_2)
        self.label_nome_git.setGeometry(QtCore.QRect(195, 478, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BlkEx BT")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_nome_git.setFont(font)
        self.label_nome_git.setStyleSheet("color: rgba(0, 0, 0, 150);")
        self.label_nome_git.setObjectName("label_nome_git")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(120, 150, 41, 41))
        self.label.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(120, 230, 41, 41))
        self.label_2.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_fundo_cadastro.raise_()
        self.label_imagem_email_cad.raise_()
        self.label_imagem_usuario_cad.raise_()
        self.lineEdit_usuario_cadastro.raise_()
        self.label_10.raise_()
        self.lineEdit_email_cadastro.raise_()
        self.label_text_cadastrese.raise_()
        self.pushButton_cadatro.raise_()
        self.label_nome_git.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_senha_cadatre = QtWidgets.QLineEdit(Form)
        self.lineEdit_senha_cadatre.setGeometry(QtCore.QRect(660, 460, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 LtEx BT")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_senha_cadatre.setFont(font)
        self.lineEdit_senha_cadatre.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-right-radius:15px;\n"
"    border-top-right-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.lineEdit_senha_cadatre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha_cadatre.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_senha_cadatre.setClearButtonEnabled(True)
        self.lineEdit_senha_cadatre.setObjectName("lineEdit_senha_cadatre")
        self.label_imagem_git = QtWidgets.QLabel(Form)
        self.label_imagem_git.setGeometry(QtCore.QRect(654, 640, 31, 31))
        self.label_imagem_git.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color:rgba(0,0,0,200);")
        self.label_imagem_git.setText("")
        self.label_imagem_git.setPixmap(QtGui.QPixmap(":/imagens/icons8-github-48.png"))
        self.label_imagem_git.setScaledContents(True)
        self.label_imagem_git.setObjectName("label_imagem_git")
        self.label_logo_top = QtWidgets.QLabel(Form)
        self.label_logo_top.setGeometry(QtCore.QRect(40, -20, 181, 171))
        self.label_logo_top.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"")
        self.label_logo_top.setText("")
        self.label_logo_top.setPixmap(QtGui.QPixmap(":/imagens/logo.png"))
        self.label_logo_top.setScaledContents(True)
        self.label_logo_top.setObjectName("label_logo_top")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(620, 460, 41, 41))
        self.label_3.setStyleSheet("    width: 450px;\n"
"    height: 65px;\n"
"    border-bottom-left-radius:15px;\n"
"    border-top-left-radius:15px;\n"
"    background: rgba(255, 255, 255, 0.2);\n"
"    border: 1px solid rgba(233, 226, 226, 0.35);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        x = QtGui.QFont()
        x.setPointSize(8)
        x.setBold(True)
        x.setWeight(75)
        Form.setFont(x)
        self.label_status_login = QtWidgets.QLabel(Form)
        self.label_status_login.setGeometry(QtCore.QRect(205, 413, 300, 41))
        x = QtGui.QFont()
        x.setPointSize(8)
        self.label_status_login.setFont(x)
        self.label_status_login.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 0, 0);")
        self.label_status_login.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_login.setObjectName("label_status_login")

        self.pushButton_medico = QtWidgets.QPushButton(Form)
        self.pushButton_medico.setGeometry(QtCore.QRect(480, 730, 121, 28))
        self.pushButton_medico.setFont(font)
        self.pushButton_medico.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;\n"
"border-bottom: 2px solid rgb(225,225,225);\n"
"color:rgb(225,225,225);\n"
"padding-bottom:0.10px;\n"
"")
        self.pushButton_medico.setObjectName("pushButton_medico")
        
        self.pushButton_servidor = QtWidgets.QPushButton(Form)
        self.pushButton_servidor.setGeometry(QtCore.QRect(620, 730, 121, 28))
        self.pushButton_servidor.setFont(font)
        self.pushButton_servidor.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"border: none;\n"
"border-bottom: 2px solid rgb(225,225,225);\n"
"color:rgb(225,225,225);\n"
"padding-bottom:0.10px;\n"
"")
        self.pushButton_servidor.setObjectName("pushButton_servidor")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_text_login.setText(_translate("Form", "L O G I N"))
        self.pushButton_login.setText(_translate("Form", "ENTRAR"))
        self.lineEdit_email_login.setPlaceholderText(_translate("Form", "E M A I L"))
        self.lineEdit_senha_login.setPlaceholderText(_translate("Form", "S E N H A "))
        self.lineEdit_usuario_cadastro.setPlaceholderText(_translate("Form", "U S U Á R I O"))
        self.lineEdit_email_cadastro.setPlaceholderText(_translate("Form", "E M A I L"))
        self.label_text_cadastrese.setText(_translate("Form", "CADASTRE-SE"))
        self.pushButton_cadatro.setText(_translate("Form", "CADASTRAR"))
        self.label_nome_git.setText(_translate("Form", "\n"
"Caio-oliveira04"))
        self.lineEdit_senha_cadatre.setPlaceholderText(_translate("Form", "S E N H A "))
        self.pushButton_medico.setText(_translate("Form", "Medico"))
        self.pushButton_servidor.setText(_translate("Form", "Servidor"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI_LoginUser()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


       

