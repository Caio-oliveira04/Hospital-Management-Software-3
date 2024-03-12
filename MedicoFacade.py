from Medico import Medico
from DataBase import DataBase

class MedicoFacade:
    def __init__(self):
        self.medico = Medico()

    def _login_med(self, crm, senha):
        return self.medico._login_med(crm, senha)

    def consultar(self):
        self.medico.consultar()

    def solicitar_exame(self, nome, exame):
        self.medico.solicitar_exame(nome, exame)

    def prescrever_medicamento(self, nome, remedio):
        self.medico.prescrever_medicamento(nome, remedio)

    def receitar_remedio(self):
        self.medico.receitar_remedio()

    def obter_nome_por_comboBox(self, comboBox):
        return self.medico.obter_nome_por_comboBox(comboBox)

    def obter_crm_por_comboBox(self, comboBox):
        return self.medico.obter_crm_por_comboBox(comboBox)

    def obter_especialidade_por_comboBox(self, comboBox):
        return self.medico.obter_especialidade_por_comboBox(comboBox)

    def listar_pacientes(self, listWidget_pacientes):
        self.medico.listar_pacientes(listWidget_pacientes)
    
    def obter_todas_combobox(self):
        return self.medico.obter_todas_combobox()
