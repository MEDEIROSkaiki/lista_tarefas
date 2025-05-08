import tkinter as tk
from controller.gestor_tarefa import GestorTarefas
from repositorio.repositorio import RepositorioTarefa
from view.tela import TelaTarefas

if __name__ == "__main__":
    raiz = tk.Tk()
    repo = RepositorioTarefa()
    gestor = GestorTarefas(repo)
    app = TelaTarefas(raiz,gestor)
    raiz.mainloop()
