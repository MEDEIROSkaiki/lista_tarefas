import json
import os
from model.tarefa import Tarefa

class RepositorioTarefa:

    def __init__(self): 
        self.CAMINHO_ARQUIVO = "lista_tarefas.json"  # Nome alterado para evitar conflitos

    def carregar_tarefas(self):
        tarefas = []
        if os.path.exists(self.CAMINHO_ARQUIVO):
            try:
                with open(self.CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    for item in dados:
                        tarefa = Tarefa(item["texto"])
                        tarefa.concluida = item["concluida"]
                        tarefas.append(tarefa)
            except Exception as e:
                print(f"Erro ao carregar tarefas: {e}")
        return tarefas

    def salvar_tarefas(self,tarefas):
        dados = [{"texto": t.texto, "concluida": t.concluida} for t in tarefas]
        try:
            with open(self.CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar tarefas: {e}")
