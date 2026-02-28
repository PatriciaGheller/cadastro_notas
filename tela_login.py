import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os

usuarios = {
    "professor": {"senha": "123", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "5678", "tipo": "aluno"},
}

colunas = ["Aluno", "Nota 1", "Nota 2", "Média", "Situação"]

if not os.path.exists("planilhaAlunos.xlsx"):
    df = pd.DataFrame(columns=colunas)
    df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")

def verificar_situacao(n1, n2):
    media = (n1+n2)/2
    if media >= 7: return media, "Aprovado"
    elif media >= 5: return media, "Recuperação"
    else: return media, "Reprovado"

def salvar_dados(tree):
    dados = [tree.item(line)["values"] for line in tree.get_children()]
    df = pd.DataFrame(data=dados, columns=colunas)
    df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")

def carregar_dados(tree, usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilhaAlunos.xlsx", engine="openpyxl")
        if "Média" not in df.columns or "Situação" not in df.columns:
            df["Média"] = (df["Nota 1"] + df["Nota 2"]) / 2
            df["Situação"] = df["Média"].apply(
                lambda m: "Aprovado" if m >= 7 else "Recuperação" if m >= 5 else "Reprovado"
            )
            df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")

        tree.delete(*tree.get_children())
        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                tree.insert("", "end", values=(row["Aluno"], row["Nota 1"], row["Nota 2"], row["Média"], row["Situação"]))
        else:
            df_aluno = df[df["Aluno"] == usuario]
            for _, row in df_aluno.iterrows():
                tree.insert("", "end", values=(row["Aluno"], row["Nota 1"], row["Nota 2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado.")

# Janela principal
root = tk.Tk()
root.title("Sistema de Notas")
root.geometry("820x600")

# Ocultar até login válido
root.withdraw()

# Criar tabela
tree = ttk.Treeview(root, columns=colunas, show="headings")
for c in colunas:
    tree.heading(c, text=c)
    tree.column(c, width=100)
tree.pack(expand=True, fill="both")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Campos de entrada
lblNome = tk.Label(root, text="Nome do Aluno:")
txtNome = tk.Entry(root)
lblNota1 = tk.Label(root, text="Nota 1")
txtNota1 = tk.Entry(root)
lblNota2 = tk.Label(root, text="Nota 2")
txtNota2 = tk.Entry(root)

lblNome.pack(); txtNome.pack()
lblNota1.pack(); txtNota1.pack()
lblNota2.pack(); txtNota2.pack()

def cadastrar():
    try:
        n1, n2 = float(txtNota1.get()), float(txtNota2.get())
        media, sit = verificar_situacao(n1, n2)
        tree.insert("", "end", values=(txtNome.get(), n1, n2, f"{media:.2f}", sit))
        salvar_dados(tree)
    except ValueError:
        messagebox.showerror("Erro", "Digite notas válidas!")

btnCadastrar = tk.Button(root, text="Cadastrar Aluno", command=cadastrar)
btnCadastrar.pack(pady=10)

# Tela de login
def abrir_login():
    login = tk.Toplevel()
    login.title("Login")
    login.geometry("300x200")

    tk.Label(login, text="Usuário:").pack(pady=5)
    user = tk.Entry(login); user.pack(pady=5)
    tk.Label(login, text="Senha:").pack(pady=5)
    pwd = tk.Entry(login, show="*"); pwd.pack(pady=5)

    def validar():
        if user.get() in usuarios and usuarios[user.get()]["senha"] == pwd.get():
            tipo = usuarios[user.get()]["tipo"]
            carregar_dados(tree, user.get(), tipo)
            login.destroy()
            root.deiconify()  # Mostrar tela principal
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos!")

    tk.Button(login, text="Entrar", command=validar).pack(pady=20)

abrir_login()
root.mainloop()
