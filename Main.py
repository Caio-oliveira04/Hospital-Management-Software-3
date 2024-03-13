from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys
from UsuarioFacade import *
from tela_login_user_ui import *
from tela_user_ui import *
from tela_login_med import *
from tela_login_funcionario import *
from MedicoFacade import *
from tela_med_ui import *
from tela_funcionario import *
from ServidorFacade import *
from PyQt5.QtGui import QColor


medico1 = MedicoFacade()
usuario1 = UsuarioFacade()
servidor1 = ServidorFacade()

class TelaFuncionario (QDialog):
    def __init__(self, *args, **kwargs):
            super(TelaFuncionario, self).__init__(*args, **kwargs)
            self.ui = Ui_TelaServidor()
            self.ui.setupUi(self)
            self.verificar_quartos()
            self.ui.pushButton_ocupado.clicked.connect(self.reservar_quarto)
            self.ui.pushButton_livre.clicked.connect(self.desocupar_quarto)
            self.desocupar_quarto()
            self.ui.pushButton_adicionar_medicamento.clicked.connect(self.cadastrar_remedio)  
            self. exibir_estoque()
            self.ui.pushButton_cadastrar_medico.clicked.connect(self.cadastrar_medico)
            self.ui.pushButton_voltar.clicked.connect(self.voltar)
            self.ui.pushButton_fechar.clicked.connect(self.fechar)
    
    def verificar_quartos(self):
        for index in range(self.ui.listWidget_quartos.count()):
            item = self.ui.listWidget_quartos.item(index)
            
            if item is not None:
                numero_quarto = item.text().strip()
                
                if numero_quarto:
                    status = servidor1.obter_status_quarto(numero_quarto)
                    if status == "Livre":
                       item.setBackground(QColor(0, 141, 0, 84))
                    else:
                        item.setBackground(QColor(255, 0, 0, 76))

    def reservar_quarto(self):
        quarto_selecionado = self.ui.listWidget_quartos.selectedItems()

        for item in quarto_selecionado:
            item.setBackground(QColor(255, 0, 0, 76))
            numero_quarto = item.text()
            dias = self.ui.lineEdit_Dias_reserva.text()
            servidor1.reservar_quarto(numero_quarto, dias)
    
    def desocupar_quarto(self):
        quarto_selecionado = self.ui.listWidget_quartos.selectedItems()

        for item in quarto_selecionado:
            item.setBackground(QColor(0, 141, 0, 84))
            numero_quarto = item.text()  
            servidor1.desocupar_quarto(numero_quarto)

    def cadastrar_remedio(self):
        medicamento = self.ui.lineEdit_remedio_padicionar.text()
        quantidade, nome = map(str.strip, medicamento.split("/"))
        quantidade = int(quantidade)
        servidor1.adicionar_medicamento(nome, quantidade)
        self.exibir_estoque()

    def exibir_estoque(self):
        self.ui.listWidget_estoque_remedios.clear()

        lista_medicamentos = servidor1.mostrar_medicamentos()
        
        for quantidade, nome in lista_medicamentos:
            item_text = f"{quantidade}x   {nome}"
            item = QListWidgetItem(item_text)
            self.ui.listWidget_estoque_remedios.addItem(item)

    def cadastrar_medico(self):
        nome = self.ui.lineEdit_nome.text()
        valor = self.ui.valor_consulta.text()
        senha = self.ui.lineEdit_Senha.text()
        crm = self.ui.lineEdit_Crm.text()
        especialidade = self.ui.lineEdit_Especialidade.text()
        combobox = f"{especialidade} - R$ {valor}"
        servidor1.cadastro_medico(nome, combobox, senha, crm, especialidade)
    
    def voltar(self):
        self.window = LoginFuncionario()
        self.window.show()
        self.close() 
    
    def fechar(self):
        self.close()

class LoginFuncionario (QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginFuncionario, self).__init__(*args, **kwargs)
        self.ui = Ui_LoginFuncionario()
        self.ui.setupUi(self)
        self.ui.pushButton_login.clicked.connect(self.login)  
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
        self.ui.pushButton_medico.clicked.connect(self.open_login_med)
        self.ui.pushButton_paciente.clicked.connect(self.open_login_paciente)

    def fechar(self):
        self.close()  
    
    def open_login_med(self):
        self.window = LoginMed()
        self.window.show()
        self.close()       
    
    def open_login_paciente(self):
        self.window = LoginUser()
        self.window.show()
        self.close()    

    def login(self):
        email = self.ui.lineEdit_email_login.text()
        senha = self.ui.lineEdit_senha_login.text()
        retorno = servidor1._login_servidor(email, senha)
        if retorno:
            self.open_tela_funcionario()
        else:
            self.ui.label_status_login.setText("Email or password incorrect. Please try again.")


    def open_tela_funcionario(self):
        self.window = TelaFuncionario()
        self.window.show()
        self.close()       

class LoginMed (QDialog):
    
    def __init__(self, *args, **kwargs):
        super(LoginMed, self).__init__(*args, **kwargs)
        self.ui = UI_LoginMed()
        self.ui.setupUi(self)
        self.ui.pushButton_Paciente.clicked.connect(self.open_login_paciente)
        self.ui.pushButton_servidor.clicked.connect(self.open_login_servidor)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)

    def fechar(self):
        self.close()  

    def open_login_paciente(self):
        self.window = LoginUser()
        self.window.show()
        self.close()   

    def open_login_servidor(self):
        self.window = LoginFuncionario()
        self.window.show()
        self.close() 

    def open_tela_med(self):
        self.window = TelaMed()
        self.window.show()
        self.close() 

    def login(self):
        crm = self.ui.lineEdit_email_login.text()
        senha = self.ui.lineEdit_senha_login.text()
        retorno_login = medico1._login_med(crm, senha)
        if retorno_login:
            self.open_tela_med()
        else:
            self.ui.label_status_login.setText("Email or password incorrect. Please try again.")


class TelaMed(QDialog):
    
    def __init__(self, *args, **kwargs):
        super(TelaMed, self).__init__(*args, **kwargs)
        self.ui = UI_TelaMed()
        self.ui.setupUi(self)
        self.print_pacientes()
        self.ui.pushButton_prescrever.clicked.connect(self.solicitar_exame)
        self.ui.pushButton_solicitar.clicked.connect(self.solicitar_remedio)
        self.ui.pushButton_consultar.clicked.connect(self.print_prontuario)
        self.ui.pushButton_voltar.clicked.connect(self.voltar)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
    
    def print_pacientes(self):
        medico1.listar_pacientes(self.ui.listWidget_pacientes)
    
    def solicitar_exame(self):
        paciente_selecionado = self.ui.listWidget_pacientes.selectedItems()
        
        for item in paciente_selecionado:
            nome = item.text()
            exame = self.ui.lineEdit_exame_remedio.text()
            medico1.solicitar_exame(nome, exame )

    def solicitar_remedio(self):
        paciente_selecionado = self.ui.listWidget_pacientes.selectedItems()
        
        for item in paciente_selecionado:
            nome = item.text()
            remedio = self.ui.lineEdit_exame_remedio.text()
            medico1.prescrever_medicamento(nome, remedio)

    def print_prontuario(self):
        paciente_selecionado = self.ui.listWidget_pacientes.selectedItems()
        
        for item in paciente_selecionado:
            nome = item.text()
            primeira_observacao, segunda_observacao, terceira_observacao = usuario1.print_observacoes(nome)
            self.ui.label_obs1.setText(primeira_observacao)
            self.ui.label_obs2.setText(segunda_observacao)
            self.ui.label_obs3.setText(terceira_observacao)

            resultados = usuario1.get_primeiros_resultados_exames(nome)
            primeiro_resultado, segundo_resultado, terceiro_resultado = resultados
            self.ui.label_exe1.setText(primeiro_resultado)
            self.ui.label_exe2.setText(segundo_resultado)
            self.ui.label_exe3.setText(terceiro_resultado)

            remedios_tomados = usuario1.get_primeiros_remedios_comprados(nome)
            primeiro_remedio, segundo_remedio, terceiro_remedio = remedios_tomados
            self.ui.label_remedio1.setText(primeiro_remedio)
            self.ui.label_remedio2.setText(segundo_remedio)
            self.ui.label_remedio3.setText(terceiro_remedio)
    
    def voltar(self):
        self.window = LoginMed()
        self.window.show()
        self.close()
    
    def fechar(self):
        self.close()

class LoginUser(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginUser, self).__init__(*args, **kwargs)
        self.ui = UI_LoginUser()
        self.ui.setupUi(self)
        self.ui.pushButton_cadatro.clicked.connect(self.cadastro)
        self.ui.pushButton_login.clicked.connect(self.login)
        self.email = ""
        self.ui.pushButton_medico.clicked.connect(self.open_login_med)
        self.ui.pushButton_servidor.clicked.connect(self.open_login_server)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)

    def fechar(self):
        self.close()  

    def open_login_med(self):
        self.window = LoginMed()
        self.window.show()
        self.close() 
    
    def open_login_server(self):
        self.window = LoginFuncionario()
        self.window.show()
        self.close()

    def cadastro(self):
        user = self.ui.lineEdit_usuario_cadastro.text()
        email = self.ui.lineEdit_email_cadastro.text()
        senha = self.ui.lineEdit_senha_cadatre.text()
        retorno = usuario1.cadastro_user(user, email, senha)
        if retorno:
            self.open_tela_user(email)

    def login(self):
        email = self.ui.lineEdit_email_login.text()
        senha = self.ui.lineEdit_senha_login.text()
        retorno_login = usuario1.login_user(email, senha)
        if retorno_login:
            self.open_tela_user(email)
        else:
            self.ui.label_status_login.setText("Email or password incorrect. Please try again.")

    def open_tela_user(self, email):
        self.window = TelaUser()
        self.window.set_email(email)
        self.window.print_saldo(email)
        self.window.exibir_consultas_marcadas()
        self.window.printar_exames_feitos()
        self.window.exibir_exames_solicitados()
        usuario1.set_email(email)
        self.window.set_lista_medicos()
        self.window.show()
        self.close()

class TelaUser(QDialog):
    def __init__(self, *args, **kwargs):
        super(TelaUser, self).__init__(*args, **kwargs)
        self.ui = Ui_TelaUser()
        self.ui.setupUi(self)
        self.email = ""
        self.set_lista_medicos()
        self.ui.pushButton_depositar.clicked.connect(self.deposito)
        self.ui.pushButton_marcar.clicked.connect(lambda: self.marcar(self.ui.comboBox_especialistas.currentText()))
        self.ui.pushButton_desmarcar.clicked.connect(self.desmarcar_consulta)
        self.ui.comboBox_especialistas.currentIndexChanged.connect(self.exibir_info_med)
        self.ui.pushButton_marcar_exame.clicked.connect(self.marcar_exame)
        self.ui.pushButton_ver_resultado.clicked.connect(self.print_resultados)
        self.ui.pushButton_voltar.clicked.connect(self.voltar)
        self.ui.pushButton_fechar.clicked.connect(self.fechar)
        self.ui.pushButton_remarcar.clicked.connect(self.remarcar)

    def set_lista_medicos(self):
        lista = medico1.obter_todas_combobox()
        self.ui.set_lista_medicos(lista)
        self.ui.set_combox()

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email
    
    def exibir_info_med(self):
        comboBox = self.ui.comboBox_especialistas.currentText() 
        crm = medico1.obter_crm_por_comboBox(comboBox)
        nome = medico1.obter_nome_por_comboBox(comboBox)
        especialidade = medico1.obter_especialidade_por_comboBox(comboBox)
        self.ui.set_crm(crm)
        self.ui.set_nome(nome)
        self.ui.set_especialidade(especialidade)
        self.ui.print()
        
    def exibir_consultas_marcadas(self):
        usuario1.print_consultas_marcadas(self.email, self.ui.listWidget_marcadas)

    def exibir_exames_solicitados(self):
        usuario1.print_exames_solicitados(self.email, self.ui.listWidget_solcitados)

    def print_saldo(self, email):
        self.ui.label_saldo.setText(f"Saldo: R$ {usuario1.getSaldo(email):.2f}")

    def desmarcar_consulta(self):
        consulta_selecionada = self.ui.listWidget_marcadas.selectedItems()
        for item in consulta_selecionada:
            data_antiga = item.text()
            usuario1.desmarcar_consulta(self.email, data_antiga)

            self.ui.listWidget_marcadas.takeItem(self.ui.listWidget_marcadas.row(item))
 
    def deposito(self):
        try:
            deposit_amount_str = self.ui.lineEdit_valor_deposito.text()
            deposit_amount = float(deposit_amount_str)
            usuario1.adicionar_dinheiro(self.email, deposit_amount)
            self.print_saldo(self.email)
        except ValueError:
            print("Invalid deposit amount. Please enter a valid number.")

    def marcar(self, combox_selecionada):

        if combox_selecionada != '...':
            selected_date = self.ui.calendarWidget.selectedDate()
            status = usuario1.marcar_consulta(self.email, combox_selecionada, selected_date.toString('dd/MM/yyyy'))
            if status:
                self.exibir_consultas_marcadas()
                self.print_saldo(self.email)
                self.ui.label_saldo.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0);") 
            else:
                self.ui.label_saldo.setStyleSheet("color: red; background-color: rgba(0, 0, 0, 0);") 
                if usuario1.getSaldo(self.email) > 100:
                    self.ui.label_saldo.setStyleSheet("color: black; background-color: rgba(0, 0, 0, 0);") 
        
    def marcar_exame(self):
        selected_items = self.ui.listWidget_solcitados.selectedItems()
        for item in selected_items:
        
            if selected_items:
                exame = selected_items[0].text()
                if usuario1.marcar_exame(self.email, exame):
                    self.ui.listWidget_solcitados.takeItem(self.ui.listWidget_solcitados.row(selected_items[0]))
                    self.printar_exames_feitos()

    def printar_exames_feitos(self):
        usuario1.print_exames_feitos(self.email, self.ui.listWidget_feitos)

    def print_resultados(self):
        exame_escolhido = self.ui.listWidget_feitos.selectedItems()
        
        for item in exame_escolhido:
            exame = item.text()
            resultado = usuario1.get_resultado_exame(self.email, exame)
            self.ui.label_ver_resultados.setText(resultado)
    
    def voltar(self):
        self.window = LoginUser()
        self.window.show()
        self.close()
    
    def fechar(self):
        self.close()
    
    def remarcar(self):
        consulta_selecionada = self.ui.listWidget_marcadas.selectedItems()
        for item in consulta_selecionada:
            consulta = item.text()
            partes = consulta.split()
            data_antiga = partes[1]
            nova_data = self.ui.dateEdit_par_remarcar.date().toString('dd/MM/yyyy')
            usuario1.remarcar_consulta(self.email, data_antiga, nova_data)
            self.exibir_consultas_marcadas()

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = LoginUser()
    window.show()
sys.exit(app.exec_())