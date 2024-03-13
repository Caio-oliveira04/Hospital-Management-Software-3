import json
import pathlib
import os
import time
import hashlib
from tela_med_ui import *
from DataBase import DataBase

db = DataBase()

class Usuario:
    CLIENTES_FILE = "clientes.txt"

    def __init__(self):
        self.nome = ""
        self.email = ""
        self.senha = ""
        self.saldo = None
        self.ui = UI_TelaMed()

    def set_email(self, email):
            self.email = email

    def get_email(self):
        return self.email        
    
    def getSaldo(self, email):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                return usuario["Saldo"]
            else:
                print(f"Usuário com o email {email} não encontrado.")
                return None  

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
            return None 
        except Exception as e:
            print(f'Erro ao obter saldo: {e}')
            return None  

    def cadastro_user(self, nome, email, senha):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            novo_usuario = {
                "Nome": nome,
                "Email": email,
                "Senha": db._hash_senha(senha),
                "Consultas": [],
                "Saldo": 0,
                "Exames_solicitados": [],
                "Exame_feitos": [],
                "Remedios_receitados": [],
                "Remedios_comprados": [],
                "Observacoes": ["Sem observações anteriores"] * 3  
            }
            dados.append(novo_usuario)
            db._salvar_dados(self.CLIENTES_FILE, dados)
            return True

        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')
        
        except Exception as e:
            print(f'Erro ao salvar os dados: {e}')

    def login_user(self, email, senha):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            for usuario in dados:
                if usuario["Email"] == email and usuario["Senha"] == db._hash_senha(senha):
                    return True
                elif usuario["Email"] == email and usuario["Senha"] != senha:
                    return False
                elif usuario["Email"] != email and usuario["Senha"] == senha:
                    return False
                
        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao realizar login: {e}')
    
    def marcar_consulta(self, email, comboBox, data):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                especialista, valor_str = comboBox.split(" - R$ ")
                valor = int(valor_str)
                if valor is not None and valor <= usuario["Saldo"]:
                    usuario["Saldo"] -= valor
                    nova_consulta = f"{especialista} {data}"
                    usuario["Consultas"].append(nova_consulta)
                    db._salvar_dados(self.CLIENTES_FILE ,dados)
                    return True
                else:
                    return False

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except ValueError as ve:
            print(f'Valor inválido: {ve}')
        except Exception as e:
            print(f'Erro ao marcar a consulta: {e}')

    def remarcar_consulta(self, email, data_antiga, nova_data):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                consultas = usuario.get("Consultas", [])
                encontrada = False

                for i, consulta in enumerate(consultas):
                    if data_antiga in consulta:
                        consultas[i] = consulta.replace(data_antiga, nova_data)
                        encontrada = True
                        print(f"Data da consulta atualizada: {consulta} -> {consultas[i]}")
                        break

                if not encontrada:
                    print(f"Nenhuma consulta encontrada para a data {data_antiga}")
                db._salvar_dados(self.CLIENTES_FILE ,dados)

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao remarcar a consulta: {e}')

    def desmarcar_consulta(self, email, data_antiga):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                consultas = usuario.get("Consultas", [])
                encontrada = False

                for i, consulta in enumerate(consultas):
                    if data_antiga in consulta:
                        consultas.pop(i)
                        encontrada = True
                        print(f"Consulta desmarcada: {consulta}")
                        break

                if not encontrada:
                    print(f"Nenhuma consulta encontrada para a data {data_antiga}")

                usuario["Consultas"] = consultas  
                db._salvar_dados(self.CLIENTES_FILE ,dados)
                print('Consulta desmarcada com sucesso!')

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao desmarcar a consulta: {e}')

    def print_exames_solicitados(self, email, listWidget_solicitados):
        try:
                listWidget_solicitados.clear()
                dados = db._carregar_dados(self.CLIENTES_FILE)

                email = email
                usuario, _ = db._buscar_usuario_por_email(email, dados)

                if usuario:
                    Exames_solicitados = usuario.get("Exames_solicitados", [])

                    if Exames_solicitados:
                        for exame in reversed(Exames_solicitados):  
                            listWidget_solicitados.insertItem(0, exame)  
                    else:
                        print("Nenhum exame solicitado.")
                else:
                    print(f"Usuário com o email {email} não encontrado.")


        except Exception as e:
            print(f"Erro: {e}")

    def get_resultado_exame(self, email, exame):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            usuario, _ = db._buscar_usuario_por_email(email, dados)

            if usuario:
                exames_feitos = usuario.get("Exame_feitos", [])

                for exame_feito in exames_feitos:
                    if exame_feito.get("exame") == exame:
                        return exame_feito.get("resultado")

                return f"Resultado do exame {exame} não encontrado para o usuário {usuario['Nome']}."

            else:
                return 'Usuário não encontrado.'

        except FileNotFoundError:
            return f'Arquivo não encontrado: {self.CLIENTES_FILE}'
        except Exception as e:
            return f'Erro ao obter resultado do exame: {e}'

    def print_remedios_receitados(self):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)

            email = input("Digite seu email: ")
            usuario, _ = db._buscar_usuario_por_email(email, dados)

            if usuario:
                remedios_receitados = usuario.get("Remedios_receitados", [])

                if remedios_receitados:
                    print("Remédios Receitados:")
                    for i, remedio in enumerate(remedios_receitados, start=1):
                        print(f"   -> Remédio {i}: {remedio}")
                else:
                    print("Nenhum remédio receitado.")

            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir remédios receitados: {e}')

    def adicionar_dinheiro(self, email_alvo, deposito):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario_alvo, _ = db._buscar_usuario_por_email(email_alvo, dados)

            if usuario_alvo:
                usuario_alvo["Saldo"] += deposito
                db._salvar_dados(self.CLIENTES_FILE ,dados)
                print(f'Dinheiro adicionado com sucesso para {usuario_alvo["Nome"]}')
                return
            else:
                print('Usuário não encontrado.')

        except ValueError:
            print('Valor inválido. Certifique-se de inserir um número válido.')
        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def print_consultas_marcadas(self, email, listWidget_marcadas):
        try:
            listWidget_marcadas.clear()
            dados = db._carregar_dados(self.CLIENTES_FILE)

            usuario, _ = db._buscar_usuario_por_email(email, dados)

            if usuario:
                consultas_marcadas = usuario.get("Consultas", [])

                if consultas_marcadas:
                    for consulta in reversed(consultas_marcadas):  
                        listWidget_marcadas.insertItem(0, consulta)  
                else:
                    print("Nenhuma consulta marcada.")
            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir consultas marcadas: {e}')

    def print_exames_feitos(self, email, listWidget_feitos):
        try:
            listWidget_feitos.clear()
            dados = db._carregar_dados(self.CLIENTES_FILE)

            email = email
            usuario, _ = db._buscar_usuario_por_email(email, dados)

            if usuario:
                exames_feitos = usuario.get("Exame_feitos", [])

                if exames_feitos:
                    for exame_feito in exames_feitos:
                        exame = exame_feito.get("exame")
                        listWidget_feitos.insertItem(0, exame)  
                else:
                    print("Nenhum exame feito.")
            else:
                print(f"Usuário com o email {email} não encontrado.")

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
        except Exception as e:
            print(f'Erro ao imprimir exames feitos: {e}')

    def marcar_exame(self, email, exame):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                novo_exame = {"exame": exame, "resultado": "sem resultado"}
                usuario["Exame_feitos"].append(novo_exame)
                usuario["Exames_solicitados"].remove(exame)
                db._salvar_dados(self.CLIENTES_FILE, dados)
                print(f'Exame marcado com sucesso para {usuario["Nome"]}')
                return True
            else:
                print('Usuário não encontrado.')

        except Exception as e:
            print(f'Ocorreu um erro ao marcar o exame: {e}')

    def set_resultado_exame(self, email, exame, resultado):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_email(email, dados)

            if usuario:
                for exame_feito in usuario["Exame_feitos"]:
                    if exame_feito.get("exame") == exame:
                        exame_feito["resultado"] = resultado
                        usuario["Exame_feitos"].append(exame_feito) 
                        db._salvar_dados(self.CLIENTES_FILE, dados)
                        print(f'Resultado do exame {exame} atualizado com sucesso para {usuario["Nome"]}')
                        return True

                print(f'Exame {exame} não encontrado para o usuário {usuario["Nome"]}')

            else:
                print('Usuário não encontrado.')

        except Exception as e:
            print(f'Ocorreu um erro ao definir o resultado do exame: {e}')
                
    def print_observacoes(self, nome):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, _ = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                observacoes = usuario.get("Observacoes", [])

                if observacoes:
                    primeira_observacao = observacoes[0] 
                    segunda_observacao = observacoes[1]
                    terceira_observacao = observacoes[2] 
                    return primeira_observacao, segunda_observacao, terceira_observacao
                else:
                    print("Sem observações.")
            else:
                print(f"Usuário com o email {nome} não encontrado.")
                return "Sem observações", "Sem observações", "Sem observações"

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
            return "Sem observações", "Sem observações", "Sem observações"
        except Exception as e:
            print(f'Erro ao obter as primeiras observações: {e}')
            return "Sem observações", "Sem observações", "Sem observações"

    def set_observacao(self, nome, nova_observacao):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, index = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                observacoes = usuario.get("Observacoes", [])

                sem_observacoes_index = next((i for i, obs in enumerate(observacoes) if obs == "Sem observações anteriores"), None)

                if sem_observacoes_index is not None:
                    observacoes[sem_observacoes_index] = nova_observacao
                else:
                    observacoes[0] = nova_observacao

                usuario["Observacoes"] = observacoes
                db._salvar_dados(self.CLIENTES_FILE, dados)
                print(f'Observação atualizada com sucesso para {usuario["Nome"]}')
                return True

            else:
                print('Usuário não encontrado.')
                return False

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
            return False
        except Exception as e:
            print(f'Ocorreu um erro ao definir a observação: {e}')
            return False

    def get_primeiros_resultados_exames(self, nome):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, _ = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                exames_feitos = usuario.get("Exame_feitos", [])
                primeiros_resultados = ["Sem resultados anteriores"] * 3 

                for i, exame_feito in enumerate(exames_feitos):
                    if i < 3:
                        primeiros_resultados[i] = exame_feito.get("resultado")

                return tuple(primeiros_resultados)

            else:
                print('Usuário não encontrado.')
                return "Sem resultado", "Sem resultado", "Sem resultado"

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
            return "Sem resultado", "Sem resultado", "Sem resultado"
        except Exception as e:
            print(f'Erro ao obter os primeiros resultados dos exames: {e}')
            return "Sem resultado", "Sem resultado", "Sem resultado"

    def get_primeiros_remedios_comprados(self, nome):
        try:
            dados = db._carregar_dados(self.CLIENTES_FILE)
            usuario, _ = db._buscar_usuario_por_nome(nome, dados)

            if usuario:
                remedios_comprados = usuario.get("Remedios_comprados", [])
                primeiros_remedios = ["Nenhum medicamento anterior"] * 3  

                for i, remedio_comprado in enumerate(remedios_comprados):
                    if i < 3:
                        primeiros_remedios[i] = remedio_comprado

                return tuple(primeiros_remedios)

            else:
                print('Usuário não encontrado.')
                return "Sem remedio comprado", "Sem remedio comprado", "Sem remedio comprado"

        except FileNotFoundError:
            print(f'Arquivo não encontrado: {self.CLIENTES_FILE}')
            return "Sem remedio comprado", "Sem remedio comprado", "Sem remedio comprado"
        except Exception as e:
            print(f'Erro ao obter os primeiros remedios comprados: {e}')
            return "Sem remedio comprado", "Sem remedio comprado", "Sem remedio comprado"

