# ✅ Gerenciador de Tarefas em Python com Tkinter

> 🛠 Projeto técnico com foco em organização de tarefas, utilizando interface gráfica em Python com arquitetura limpa baseada no padrão MVC.
> 

---

## 🎯 Objetivo do Projeto

Este projeto tem como finalidade o desenvolvimento de um **Gerenciador de Tarefas** com interface gráfica em Python, utilizando a biblioteca **Tkinter** e uma arquitetura organizada por camadas.

O objetivo principal é aplicar práticas de:

- Programação orientada a objetos (POO)
- Separação de responsabilidades com padrão MVC (Model-View-Controller)
- Manipulação de arquivos (`JSON`)
- Criação de interfaces gráficas amigáveis com **Tkinter**

---

### 🧱 Estrutura do Projeto (Arquitetura por Camadas)

```bash
gerenciador-de-tarefas/
│
├── controllers/              # Camada de controle (conecta modelos e visualizações)
│
├── models/                   # Representação dos dados (ex: classe Tarefa)
│
├── repositories/             # Persistência e carregamento de dados (ex: tarefas.json)
│
├── views/                    # Interface gráfica (Tkinter)
│
├── main.py                   # Ponto de entrada da aplicação
├── tarefas.json                # Base de dados local (arquivo com tarefas salvas)
└── README.md                 # Documentação do projeto
```

---

### 🧠 Funcionalidades da Aplicação

- ✅ **Adicionar nova tarefa**
- ✏️ **Editar tarefa existente**
- 🗑 **Excluir tarefa**
- 📋 **Listar todas as tarefas**
- 🖥 **Interface gráfica completa com Tkinte**

---

### ▶️ Como Executar

1. **Clone o repositório:**
    
    ```bash
    git clone https://github.com/Romope83/python--todo-list-app.git
    cd C:\caminho\para\sua\pasta
    ```
    
2. **Execute o projeto:**
    
    ```bash
    
    python main.py
    ```
    
3. Ou
    
    ```bash
    
    py main.py
    ```
    

> ✅ O projeto não depende de bibliotecas externas, pois utiliza apenas Tkinter (já incluído no Python) e JSON.
> 

---

### 📦 Requisitos

- Python 3.10 ou superior
- Tkinter (incluído no Python por padrão)

---

### 👨‍💻 Autores

- Ronaldo Moreira
    - Estrutura base do projeto
    - Interface gráfica
- Kaiki Medeiros
    - Documentação
    - Polimentos finais
- Kaua Felipe de Melo
    - Melhorias no código e interface
    - GitHub
- Felipe Oliveira
    - Operações principais

 

---

### 🗂 Organização

O projeto está organizado no Trello:

🔗 [Acesse o Quadro no Trello](https://trello.com/invite/b/681002808656a89075bc4303/ATTI095d35feac8dd1ff19e34617de339cfdDF025706/tkinter)

---

### 🧾 Licença

Este projeto está licenciado sob a Licença do SENAI.

Você pode utilizar, modificar e distribuir para fins educacionais ou pessoais.

---

### 📌 Conclusão

Este gerenciador de tarefas demonstra a aplicação de boas práticas de arquitetura de software (MVC), separação de responsabilidades e construção de interfaces gráficas com Python puro.

Serve como uma base sólida para projetos maiores e também como prática de organização de código.
