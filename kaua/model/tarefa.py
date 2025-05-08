class Tarefa:
    def __init__(self, texto: str):
        self.texto = texto
        self.concluida = False

    def alternar_status(self):
        self.concluida = not self.concluida

        
