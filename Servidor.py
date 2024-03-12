import json
import os
import pathlib
import time
import hashlib
from Usuario import Usuario
from DataBase import DataBase

db = DataBase()

class Servidor:
    CLIENTES_FILE = "clientes.txt"
    MEDICO_FILE = "medicos.txt"
    SERVIDOR_FILE = "servidor.txt"
    QUARTO_FILE = "quartos.txt"
    MEDICAMENTOS_FILE = "medicamentos.txt"
    ESCALA_FILE = "escala_funcionarios.txt"

    def __init__(self):
        self.nome = ''
        self.email = ''
        self.senha = ''
        self.funcao = ''


    def cadastro_medico(self, nome, combobox, senha, crm, especialidade):
        try:
            dados_med = db._carregar_dados(self.MEDICO_FILE)

            novo_med = {
                "Nome": nome,
                "comboBox": combobox,
                "Senha": db._hash_senha(senha),
                "Crm": crm,
                "Especialidade": especialidade,
            }

            dados_med.append(novo_med)

            db._salvar_dados(self.MEDICO_FILE, dados_med)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')
            
    def _login_servidor(self, email, senha):
        try:
            dados_servidor = db._carregar_dados(self.SERVIDOR_FILE)

            for usuario in dados_servidor:
                if usuario["Email"] == email and usuario["Senha"] == db._hash_senha(senha):
                    return True
                elif usuario["Email"] == email and usuario["Senha"] != senha:
                    return False
                elif usuario["Email"] != email and usuario["Senha"] == senha:
                    print("Email incorreto")
                    return False

            print("Email não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.MEDICO_FILE}')
        except Exception as e:
            print(f'Erro ao realizar login: {e}')


    def reservar_quarto(self, numero_quarto, dias):
        try:
            dados_quarto = db._carregar_dados(self.QUARTO_FILE)
            
            for quarto in dados_quarto:
                if quarto.get('Numero') == numero_quarto:
                    quarto_encontrado = True
                    quarto['Status'] = 'Ocupado'
                    quarto['Dias estadia'] = dias
                    break

            db._salvar_dados(self.QUARTO_FILE, dados_quarto)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def desocupar_quarto(self, numero_quarto):
        try:
            dados_quarto = db._carregar_dados(self.QUARTO_FILE)
            
            for quarto in dados_quarto:
                if quarto.get('Numero') == numero_quarto:
                    quarto_encontrado = True
                    quarto['Status'] = 'Livre'
                    break

            db._salvar_dados(self.QUARTO_FILE, dados_quarto)

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def obter_status_quarto(self, numero_quarto):
        try:
            dados_quarto = db._carregar_dados(self.QUARTO_FILE)

            for quarto in dados_quarto:
                if quarto.get('Numero') == numero_quarto:
                    return quarto.get('Status')

        except Exception as e:
            print(f'Erro ao carregar os dados: {e}')

        return 'Erro ao obter o status do quarto'

    def adicionar_medicamento(self, nome, quantidade):
        try:
            medicamentos = db._carregar_dados(self. MEDICAMENTOS_FILE)
            novo_medicamento = {
                "nome": nome,
                "quantidade": quantidade,
            }
            medicamentos.append(novo_medicamento)
            db._salvar_dados(self.MEDICAMENTOS_FILE, medicamentos)
            print(f"\nMedicamento {self.nome} adicionado ao estoque.\n")

        except FileNotFoundError:
            print("Erro: Arquivo de medicamentos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao adicionar medicamento: {e}')
    
    def mostrar_medicamentos(self):
        try:
            medicamentos = db._carregar_dados(self.MEDICAMENTOS_FILE)
            if not medicamentos:
                print("Não há medicamentos cadastrados.")
                return []

            lista_medicamentos = []
            for medicamento in medicamentos:
                nome = medicamento.get('nome', 'N/A')
                quantidade = medicamento.get('quantidade', 'N/A')
                tupla_medicamento = (quantidade, nome)
                lista_medicamentos.append(tupla_medicamento)

            return lista_medicamentos
                
        except FileNotFoundError:
            print("Erro: Arquivo de medicamentos não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao mostrar medicamentos: {e}')
            return []
        
    def adicionar_escala(self):
        try:
            self.funcionario =  input('Digite o nome do funcionario que será adicionado a escala: ')
            print()
            self.dias_trabalhados = input(f'Dias da semana que {self.funcionario} irá trabalhar, no seguinte formato:["dias da semana",..]')
            print()
            self.horas_por_dia = input(f'Digite quantas horas {self.funcionario} irá trabalhar por dia')
            escala = db._carregar_dados(self.ESCALA_FILE)
            nova_entrada = {
                "funcionario": self.funcionario,
                "dias_trabalhados": self.dias_trabalhados,
                "horas_por_dia": self.horas_por_dia
            }
            escala.append(nova_entrada)
            db._salvar_dados(self.ESCALA_FILE, escala)
            print(f"\nEscala adicionada para {self.funcionario}.\n")

        except FileNotFoundError:
            print("Erro: Arquivo de escalas não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao adicionar escala: {e}')

    def mostrar_escala(self):
        try:
            escala = db._carregar_dados(self.ESCALA_FILE)
            if not escala:
                print("Não há escalas cadastradas.")
                return

            print("\nEscala de Funcionários:")
            for entrada in escala:
                print(f"Funcionário: {entrada.get('funcionario', 'N/A')}, Dias Trabalhados: {entrada.get('dias_trabalhados', 'N/A')}, Horas por Dia: {entrada.get('horas_por_dia', 'N/A')}")
                print("------------------------------")
            escape = input ('0 Para sair')
            if escape == 0:
                return
        except FileNotFoundError:
            print("Erro: Arquivo de escalas não encontrado.")
        except json.JSONDecodeError:
            print("Erro: Problema ao decodificar o arquivo JSON.")
        except Exception as e:
            print(f'Erro ao mostrar escala: {e}')