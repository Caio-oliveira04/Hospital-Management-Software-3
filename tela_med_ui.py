from PyQt5 import QtCore, QtGui, QtWidgets
import sys, imagens_rc


class UI_TelaMed(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1227, 778)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(22, 34, 42, 255), stop:1 rgba(58, 96, 115, 255));")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 1231, 101))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_logo = QtWidgets.QLabel(Form)
        self.label_logo.setGeometry(QtCore.QRect(10, -50, 201, 191))
        self.label_logo.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/imagens/logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 140, 1111, 591))
        self.widget.setStyleSheet("background-color: rgba(0, 0, 0, 0.25);\n"
" border-radius:10px;\n"
"")
        self.widget.setObjectName("widget")
        self.listWidget_pacientes = QtWidgets.QListWidget(self.widget)
        self.listWidget_pacientes.setGeometry(QtCore.QRect(50, 40, 341, 311))
        self.listWidget_pacientes.setStyleSheet("color: rgb(255, 255, 255);")
        self.listWidget_pacientes.setObjectName("listWidget_pacientes")
        self.lineEdit_exame_remedio = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_exame_remedio.setGeometry(QtCore.QRect(50, 420, 341, 51))
        self.lineEdit_exame_remedio.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_exame_remedio.setObjectName("lineEdit_exame_remedio")
        self.label_text_1 = QtWidgets.QLabel(self.widget)
        self.label_text_1.setGeometry(QtCore.QRect(50, 380, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_1.setFont(font)
        self.label_text_1.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_text_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_1.setObjectName("label_text_1")
        self.label_text_paciente = QtWidgets.QLabel(self.widget)
        self.label_text_paciente.setGeometry(QtCore.QRect(50, 20, 341, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_text_paciente.setFont(font)
        self.label_text_paciente.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_text_paciente.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_paciente.setObjectName("label_text_paciente")
        self.pushButton_consultar = QtWidgets.QPushButton(self.widget)
        self.pushButton_consultar.setGeometry(QtCore.QRect(400, 120, 111, 28))
        self.pushButton_consultar.setStyleSheet("QPushButton#pushButton_consultar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton#pushButton_consultar:hover{ \n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"QPushButton#pushButton_consultar:pressed {\n"
"    padding-left: 5px;\\n\"\n"
"    padding-top: 5px;\\n\"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_consultar.setObjectName("pushButton_consultar")

        self.pushButton_enviar = QtWidgets.QPushButton(Form)
        self.pushButton_enviar.setGeometry(QtCore.QRect(230, 705, 81, 21))
        self.pushButton_enviar.setStyleSheet("background-color: rgba(255, 255, 255, 0.3);\n"
"border-radius:8px;\n"
"")
        self.pushButton_enviar.setObjectName("pushButton_enviar")

        self.pushButton_prescrever = QtWidgets.QPushButton(self.widget)
        self.pushButton_prescrever.setGeometry(QtCore.QRect(400, 180, 111, 28))
        self.pushButton_prescrever.setStyleSheet("QPushButton#pushButton_prescrever{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton#pushButton_prescrever:hover{ \n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"QPushButton#pushButton_prescrever:pressed {\n"
"    padding-left: 5px;\\n\"\n"
"    padding-top: 5px;\\n\"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_prescrever.setObjectName("pushButton_prescrever")
        self.pushButton_solicitar = QtWidgets.QPushButton(self.widget)
        self.pushButton_solicitar.setGeometry(QtCore.QRect(400, 240, 111, 28))
        self.pushButton_solicitar.setStyleSheet("QPushButton#pushButton_solicitar{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112,226));\n"
"    color: rgba(225, 225, 225, 210);\n"
"    border-radius:9px;\n"
"}\n"
"QPushButton#pushButton_solicitar:hover{ \n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"QPushButton#pushButton_solicitar:pressed {\n"
"    padding-left: 5px;\\n\"\n"
"    padding-top: 5px;\\n\"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 225), stop:1 rgba(85, 98, 112,226));\n"
"}\n"
"")
        self.pushButton_solicitar.setObjectName("pushButton_solicitar")
        self.label_prontuario = QtWidgets.QLabel(self.widget)
        self.label_prontuario.setGeometry(QtCore.QRect(660, 20, 341, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_prontuario.setFont(font)
        self.label_prontuario.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_prontuario.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prontuario.setObjectName("label_prontuario")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(600, 40, 461, 521))
        self.label_5.setStyleSheet(" border-radius:40px;\n"
"background-color: rgb(255, 255, 255, 0.2);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lineEdit_chat = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_chat.setGeometry(QtCore.QRect(50, 500, 341, 61))
        self.lineEdit_chat.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_chat.setObjectName("lineEdit_chat")
        self.label_text = QtWidgets.QLabel(self.widget)
        self.label_text.setGeometry(QtCore.QRect(50, 470, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text.setObjectName("label_text")
        self.label_text_2 = QtWidgets.QLabel(self.widget)
        self.label_text_2.setGeometry(QtCore.QRect(50, 400, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_2.setFont(font)
        self.label_text_2.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_text_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text_2.setObjectName("label_text_2")
        self.label_txt_obs = QtWidgets.QLabel(self.widget)
        self.label_txt_obs.setGeometry(QtCore.QRect(670, 60, 331, 41))
        self.label_txt_obs.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_txt_obs.setObjectName("label_txt_obs")
        self.label_obs1 = QtWidgets.QLabel(self.widget)
        self.label_obs1.setGeometry(QtCore.QRect(650, 100, 421, 41))
        self.label_obs1.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_obs1.setObjectName("label_obs1")
        self.label_obs2 = QtWidgets.QLabel(self.widget)
        self.label_obs2.setGeometry(QtCore.QRect(650, 130, 421, 41))
        self.label_obs2.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_obs2.setObjectName("label_obs2")
        self.label_obs3 = QtWidgets.QLabel(self.widget)
        self.label_obs3.setGeometry(QtCore.QRect(650, 160, 421, 41))
        self.label_obs3.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_obs3.setObjectName("label_obs3")
        self.label_txt_exames = QtWidgets.QLabel(self.widget)
        self.label_txt_exames.setGeometry(QtCore.QRect(680, 200, 291, 41))
        self.label_txt_exames.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_txt_exames.setObjectName("label_txt_exames")
        self.label_exe1 = QtWidgets.QLabel(self.widget)
        self.label_exe1.setGeometry(QtCore.QRect(650, 240, 421, 41))
        self.label_exe1.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_exe1.setObjectName("label_exe1")
        self.label_exe3 = QtWidgets.QLabel(self.widget)
        self.label_exe3.setGeometry(QtCore.QRect(650, 300, 421, 41))
        self.label_exe3.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_exe3.setObjectName("label_exe3")
        self.label_exe2 = QtWidgets.QLabel(self.widget)
        self.label_exe2.setGeometry(QtCore.QRect(650, 270, 421, 41))
        self.label_exe2.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_exe2.setObjectName("label_exe2")
        self.label_txt_remedio = QtWidgets.QLabel(self.widget)
        self.label_txt_remedio.setGeometry(QtCore.QRect(674, 360, 315, 41))
        self.label_txt_remedio.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_txt_remedio.setObjectName("label_txt_remedio")
        self.label_remedio1 = QtWidgets.QLabel(self.widget)
        self.label_remedio1.setGeometry(QtCore.QRect(650, 420, 421, 41))
        self.label_remedio1.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_remedio1.setObjectName("label_result1")
        self.label_remedio3 = QtWidgets.QLabel(self.widget)
        self.label_remedio3.setGeometry(QtCore.QRect(650, 480, 421, 41))
        self.label_remedio3.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_remedio3.setObjectName("label_result3")
        self.label_remedio2 = QtWidgets.QLabel(self.widget)
        self.label_remedio2.setGeometry(QtCore.QRect(650, 450, 421, 41))
        self.label_remedio2.setStyleSheet("background-color: qconicalgradient(cx:0.56, cy:1, angle:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label_remedio2.setObjectName("label_result2")
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

        self.pushButton_enviar.raise_()
        self.label_5.raise_()
        self.listWidget_pacientes.raise_()
        self.lineEdit_exame_remedio.raise_()
        self.label_text_1.raise_()
        self.label_text_paciente.raise_()
        self.pushButton_consultar.raise_()
        self.pushButton_prescrever.raise_()
        self.pushButton_solicitar.raise_()
        self.label_prontuario.raise_()
        self.lineEdit_chat.raise_()
        self.label_text.raise_()
        self.label_text_2.raise_()
        self.label_txt_obs.raise_()
        self.label_obs1.raise_()
        self.label_obs2.raise_()
        self.label_obs3.raise_()
        self.label_txt_exames.raise_()
        self.label_exe1.raise_()
        self.label_exe3.raise_()
        self.label_exe2.raise_()
        self.label_txt_remedio.raise_()
        self.label_remedio3.raise_()
        self.label_remedio1.raise_()
        self.label_remedio2.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.label_logo.raise_()
        self.pushButton_voltar.raise_()
        self.pushButton_fechar.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.listWidget_pacientes.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.listWidget_pacientes.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_text_1.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#ffffff;\">Digite o rémedio ou exame para solicitar </span></p><p><br/></p></body></html>"))
        self.label_text_paciente.setText(_translate("Form", "Selecione um paciente"))
        self.pushButton_consultar.setText(_translate("Form", "Ver Prontuario"))
        self.pushButton_prescrever.setText(_translate("Form", "Solicitar Exame"))
        self.pushButton_solicitar.setText(_translate("Form", "Solicitar remedio"))
        self.label_prontuario.setText(_translate("Form", "Prontuario"))
        self.label_text.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt;\">Atribua uma observação a essa consulta</span></p></body></html>"))
        self.label_text_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:8pt; color:#ffffff;\">e clique no seu aperte seu respectivo botão</span></p><p><br/></p></body></html>"))
        self.label_txt_obs.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Observação de consultas anteriores:</span></p></body></html>"))
        self.label_txt_exames.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Resultado de exames anteriores:</span></p></body></html>"))
        self.label_exe1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\"><br/></span></p></body></html>"))
        self.label_exe3.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_exe2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_txt_remedio.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Rémedios que o paciente já faz uso:</span></p></body></html>"))
        self.label_remedio1.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_remedio3.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_remedio2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_enviar.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">Ocupado</span></p></body></html>"))
        self.pushButton_enviar.setWhatsThis(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">Ocupado</span></p></body></html>"))
        self.pushButton_enviar.setText(_translate("Form", "Enviar"))
        self.pushButton_voltar.setText(_translate("Form", "<-- Voltar"))
        self.pushButton_fechar.setText(_translate("Form", "X"))

       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI_TelaMed()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
