import tkinter as tk 
from tkinter import ttk

janela = tk.Tk()
janela.title("Sistema de Gestão Escolar")
janela.geometry("600x400")

# Campos de entrada
tk.Label(janela, text="Nome do Aluno:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Nota 1:").pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()

tk.Label(janela, text="Nota 2:").pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()

# Tabela com colunas
tabela = ttk.Treeview(
    janela, 
    columns=("Nome", "Nota1", "Nota2", "Média", "Situação"), 
    show="headings"
)
tabela.heading("Nome", text="Nome do Aluno")
tabela.heading("Nota1", text="Nota 1")
tabela.heading("Nota2", text="Nota 2")
tabela.heading("Média", text="Média")
tabela.heading("Situação", text="Situação")

# Barra de rolagem vertical
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)

# Layout
tabela.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Dados iniciais
alunos_iniciais = [
    ("Alice", 8.5, 7.0),
    ("Bruno", 5.0, 6.0),
    ("Carlos", 3.5, 4.0),
    ("Daniela", 9.0, 9.5)
]

for aluno in alunos_iniciais:
    nome, nota1, nota2 = aluno
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))

# Linhas de teste para forçar a rolagem
for i in range(30):
    nota1, nota2 = i % 10, (i % 10) + 1
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    tabela.insert("", "end", values=(f"Aluno {i}", nota1, nota2, f"{media:.2f}", situacao))

# Função para cadastrar aluno
def cadastrar_aluno():
    nome = entrada_nome.get()
    nota1 = float(entrada_nota1.get())
    nota2 = float(entrada_nota2.get())
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))

# Botão
tk.Button(janela, text="Cadastrar", command=cadastrar_aluno).pack()

janela.mainloop()
