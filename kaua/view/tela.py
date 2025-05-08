import tkinter as tk
from tkinter import messagebox
from controller.gestor_tarefa import GestorTarefas

class TelaTarefas:
    def __init__(self, raiz,gestor:GestorTarefas):
        self.gestor = gestor
        self.indice_editando = None

        self.raiz = raiz
        self.raiz.title("Lista de Tarefas")
        self.raiz.geometry("500x500")

        self.entrada = tk.Entry(raiz, width=50)
        self.entrada.pack(pady=10)

        frame_botoes = tk.Frame(raiz)
        frame_botoes.pack()

        self.btn_adicionar = tk.Button(frame_botoes, text="Adicionar", command=self.adicionar)
        self.btn_adicionar.grid(row=0, column=0, padx=5)

        self.btn_salvar = tk.Button(frame_botoes, text="Salvar Edição", command=self.salvar_edicao, state="disabled")
        self.btn_salvar.grid(row=0, column=1, padx=5)

        self.frame_tarefas = tk.Frame(raiz)
        self.frame_tarefas.pack(pady=10, fill="both", expand=True)

        self.atualizar_interface()

    def adicionar(self):
        texto = self.entrada.get().strip()
        if texto:
            self.gestor.adicionar(texto)
            self.entrada.delete(0, tk.END)
            self.atualizar_interface()
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa.")

    def editar(self, indice):
        tarefa = self.gestor.listar()[indice]
        self.entrada.delete(0, tk.END)
        self.entrada.insert(0, tarefa.texto)
        self.indice_editando = indice
        self.btn_adicionar.config(state="disabled")
        self.btn_salvar.config(state="normal")

    def salvar_edicao(self):
        novo_texto = self.entrada.get().strip()
        if novo_texto and self.indice_editando is not None:
            self.gestor.editar(self.indice_editando, novo_texto)
            self.entrada.delete(0, tk.END)
            self.indice_editando = None
            self.btn_adicionar.config(state="normal")
            self.btn_salvar.config(state="disabled")
            self.atualizar_interface()
        else:
            messagebox.showwarning("Erro", "Nada para salvar.")

    def remover(self, indice):
        self.gestor.remover(indice)
        self.atualizar_interface()

    def alternar(self, indice, var):
        self.gestor.alternar_status(indice)

    def salvar_em_arquivo(self):
        self.gestor.salvar()
        messagebox.showinfo("Salvo", "Tarefas salvas com sucesso!")

    def atualizar_interface(self):
        for widget in self.frame_tarefas.winfo_children():
            widget.destroy()

        for i, tarefa in enumerate(self.gestor.listar()):
            frame = tk.Frame(self.frame_tarefas)
            frame.pack(fill="x", pady=2)

            var = tk.BooleanVar(value=tarefa.concluida)
            chk = tk.Checkbutton(frame, variable=var, command=lambda i=i, v=var: self.alternar(i, v))
            chk.pack(side="left")

            lbl = tk.Label(frame, text=tarefa.texto, anchor="w")
            lbl.pack(side="left", fill="x", expand=True)

            btn_editar = tk.Button(frame, text="✏️", command=lambda i=i: self.editar(i), width=3)
            btn_editar.pack(side="right", padx=2)

            btn_remover = tk.Button(frame, text="🗑️", command=lambda i=i: self.remover(i), width=3)
            btn_remover.pack(side="right")
