import json
import os
import pathlib
import time
import hashlib
from Usuario import Usuario
from DataBase import DataBase
db = DataBase()

class Medico(DataBase):
    CLIENTES_FILE = "clientes.txt"
    MEDICO_FILE = "medicos.txt"

    def __init__(self):
        self.nome = ''
        self.comboBox = ''
        self.senha = ''
        self.especialidade = ''
        self.crm = ''
        self.hospital_vinculado = ''

    def _login_med(self, crm, senha):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)

            for usuario in dados_med:
                if usuario["Crm"] == crm and usuario["Senha"] == db._hash_senha(senha):
                    return True
                elif usuario["Crm"] ==  crm and usuario["Senha"] != senha:
                    print("Senha incorreta")
                    return False
                elif usuario["Crm"] !=  crm and usuario["Senha"] == senha:
                    return False

            print("Crm não encontrado")


        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
        except Exception as e:
            print(f'Erro ao realizar login: {e}')

    def consultar(self):
        dados = db._carregar_dados(self.CLIENTES_FILE)
        email = input("Digite o email do paciente: ")
        usuario, index = db._buscar_usuario_por_email(email, dados)

        if usuario:
            print(f'PRONTUARIO de {usuario["Nome"]}')
            
            usuario2 = Usuario()
            usuario2.print_resultados_exames(email)

            # Pergunte ao médico se deseja marcar um exame
            decisao = input('Deseja marcar um exame para este paciente? (sim/não) ')
            if decisao.lower() == 'sim':
                self.solicitar_exame(email)
        else:
            print(f"Usuário com o email {email} não encontrado.")

    def solicitar_exame(self, nome, exame):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            usuario, index = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                usuario["Exames_solicitados"].append(exame)
                db._salvar_dados(self.CLIENTES_FILE, dados)  
                print(f'Exame "{exame}" solicitado com sucesso!')
            else:
                print(f"Usuário com o email {nome} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao solicitar o exame: {e}')


    def prescrever_medicamento(self, nome, remedio):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            usuario, index = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                usuario["Remedios_receitados"].append(remedio)
                db._salvar_dados(self.CLIENTES_FILE, dados)  # Corrigido para salvar dados do usuário
                print(f"{remedio}" 'prescrito com sucesso!')
            else:
                print(f"Usuário com o email {nome} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao solicitar o exame: {e}')        

    def receitar_remedio(self):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            email = input("Digite o email do paciente: ")
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                remedio = input("Digite o nome do remédio a ser receitado: ")
                usuario.setdefault("Remedios_receitados", []).append(remedio)
                
                db._salvar_dados(self.CLIENTES_FILE, dados)

                print(f"Remédio '{remedio}' receitado com sucesso para {usuario['Nome']}.")
                time.sleep(2)

            else:
                print(f"Usuário com o email {email} não encontrado.")
                time.sleep(2)

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao receitar remédio: {e}')

    def obter_nome_por_comboBox(self, comboBox):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)
            for doctor_info in dados_med:
                if doctor_info["comboBox"] == comboBox:
                    return doctor_info["Nome"]
            
            return None

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
            return None
        except Exception as e:
            print(f'Erro ao obter nome por comboBox: {e}')
            return None

    def obter_crm_por_comboBox(self, comboBox):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)

            for doctor_info in dados_med:
                if doctor_info["comboBox"] == comboBox:
                    return doctor_info["Crm"]
            return None

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
            return None
        except Exception as e:
            print(f'Erro ao obter CRM por comboBox: {e}')
            return None

    def obter_especialidade_por_comboBox(self, comboBox):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)

            for doctor_info in dados_med:
                if doctor_info["comboBox"] == comboBox:
                    return doctor_info["Especialidade"]

            return None

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
            return None
        except Exception as e:
            print(f'Erro ao obter especialidade por comboBox: {e}')
            return None

    def listar_pacientes(self, listWidget_pacientes):
        try:
            listWidget_pacientes.clear()
            dados = db._carregar_dados(self.CLIENTES_FILE)

            if dados:
                print("Lista de Clientes:")
                for usuario in dados:
                     nome = usuario.get("Nome")
                     listWidget_pacientes.addItem(nome)
            else:
                print("Não há clientes cadastrados.")
       
        except FileNotFoundError:
                print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
                print(f'Erro ao listar clientes: {e}')  
    
    def obter_todas_combobox(self):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)

            if dados_med:
                comboboxes = [doctor_info["comboBox"] for doctor_info in dados_med]
                return comboboxes
            else:
                print("Não há médicos cadastrados.")
                return []

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
            return []
        except Exception as e:
            print(f'Erro ao obter todas as comboboxes: {e}')
            return []
    
    def _buscar_usuario_por_comboBoxcr(self, comboBoxcr, dados):
        for i, usuario in enumerate(dados):
            if usuario["comboBoxcr"] == comboBoxcr:
                return usuario, i
        return None, -1

