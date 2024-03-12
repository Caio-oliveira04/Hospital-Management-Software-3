import json
import pathlib
import hashlib

class DataBase:
    
    def _carregar_dados(self, file):
        if pathlib.Path(file).exists():
            with open(file, "r") as arquivo:
                return [json.loads(linha) for linha in arquivo]
        else:
            return []

    def _salvar_dados(self, file, dados):
        with open(file, "w") as arquivo:
            for usuario in dados:
                json.dump(usuario, arquivo)
                arquivo.write('\n')

    def _hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def _buscar_usuario_por_email(self, email, dados):
        for i, usuario in enumerate(dados):
            if usuario.get("Email") == email:
                return usuario, i
        return None, -1

    def _buscar_usuario_por_nome(self, nome, dados):
        for i, usuario in enumerate(dados):
            if usuario.get("Nome") == nome:
                return usuario, i
        return None, -1
