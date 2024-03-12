from DataBase import DataBase
from Usuario import Usuario

class UsuarioFacade:
    def __init__(self):
        self.usuario = Usuario()

    def set_email(self, email):
        return self.usuario.set_email(email)

    def getSaldo(self, email):
        return self.usuario.getSaldo(email)

    def cadastro_user(self, nome, email, senha):
        return self.usuario.cadastro_user(nome, email, senha)

    def login_user(self, email, senha):
        return self.usuario.login_user(email, senha)

    def marcar_consulta(self, email, comboBox, data):
        return self.usuario.marcar_consulta(email, comboBox, data)

    def remarcar_consulta(self):
        return self.usuario.remarcar_consulta()

    def desmarcar_consulta(self, email, data_antiga):
        return self.usuario.desmarcar_consulta(email, data_antiga)

    def print_exames_solicitados(self, email, listWidget_solicitados):
        return self.usuario.print_exames_solicitados(email, listWidget_solicitados)

    def get_resultado_exame(self, email, exame):
        return self.usuario.get_resultado_exame(email, exame)

    def print_remedios_receitados(self):
        return self.usuario.print_remedios_receitados()

    def adicionar_dinheiro(self, email_alvo, deposito):
        return self.usuario.adicionar_dinheiro(email_alvo, deposito)

    def print_consultas_marcadas(self, email, listWidget_marcadas):
        return self.usuario.print_consultas_marcadas(email, listWidget_marcadas)

    def print_exames_feitos(self, email, listWidget_feitos):
        return self.usuario.print_exames_feitos(email, listWidget_feitos)

    def marcar_exame(self, email, exame):
        return self.usuario.marcar_exame(email, exame)

    def set_resultado_exame(self, email, exame, resultado):
        return self.usuario.set_resultado_exame(email, exame, resultado)

    def print_observacoes(self, nome):
        return self.usuario.print_observacoes(nome)

    def set_observacao(self, nome, nova_observacao):
        return self.usuario.set_observacao(nome, nova_observacao)

    def get_primeiros_resultados_exames(self, nome):
        return self.usuario.get_primeiros_resultados_exames(nome)

    def get_primeiros_remedios_comprados(self, nome):
        return self.usuario.get_primeiros_remedios_comprados(nome)
