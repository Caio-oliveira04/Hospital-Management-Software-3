from Servidor import Servidor
from DataBase import DataBase

class ServidorFacade:
    def __init__(self):
        self.servidor = Servidor()

    def cadastro_medico(self, nome, combobox, senha, crm, especialidade):
        self.servidor.cadastro_medico(nome, combobox, senha, crm, especialidade)

    def cadastro_servidor(self):
        self.servidor.cadastro_servidor()

    def _login_servidor(self, email, senha):
        return self.servidor._login_servidor(email, senha)

    def reservar_quarto(self, numero_quarto, dias):
        self.servidor.reservar_quarto(numero_quarto, dias)

    def desocupar_quarto(self, numero_quarto):
        self.servidor.desocupar_quarto(numero_quarto)

    def obter_status_quarto(self, numero_quarto):
        return self.servidor.obter_status_quarto(numero_quarto)

    def adicionar_medicamento(self, nome, quantidade):
        self.servidor.adicionar_medicamento(nome, quantidade)

    def mostrar_medicamentos(self):
        return self.servidor.mostrar_medicamentos()

    def adicionar_escala(self):
        self.servidor.adicionar_escala()

    def mostrar_escala(self):
        self.servidor.mostrar_escala()
