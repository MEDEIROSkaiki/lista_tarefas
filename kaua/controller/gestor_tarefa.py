from model.tarefa import Tarefa
import repositorio.repositorio as repositorio

class GestorTarefas:
    def __init__(self, repo:repositorio.RepositorioTarefa):
        self.repo = repo
        self.tarefas:list[Tarefa] = repo.carregar_tarefas()

    def adicionar(self, texto):
        self.tarefas.append(Tarefa(texto))
        self.__salvar()

    def editar(self, indice, novo_texto):
        self.tarefas[indice].texto = novo_texto
        self.__salvar()

    def remover(self, indice):
        del self.tarefas[indice]
        self.__salvar()

    def alternar_status(self, indice):
        tarefa = self.tarefas[indice]
        tarefa.alternar_status()
        self.__salvar()

    def __salvar(self):
        self.repo.salvar_tarefas(self.tarefas)

    def listar(self):
        return self.tarefas
