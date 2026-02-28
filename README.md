# Sistema de Gestão Escolar

Este projeto é um sistema simples de gestão escolar desenvolvido em **Python**, com interface gráfica em **Tkinter** e persistência de dados em **Excel**.  
O objetivo é cadastrar alunos, calcular médias das notas e determinar automaticamente a situação acadêmica (Aprovado, Recuperação ou Reprovado).

---

## 🚀 Funcionalidades
- Cadastro de alunos com nome e duas notas.
- Cálculo automático da média aritmética.
- Determinação da situação acadêmica:
  - Média >= 7 → **Aprovado**
  - Média >= 5 → **Recuperação**
  - Média < 5 → **Reprovado**
- Exibição dos dados em uma tabela (`Treeview`) com barra de rolagem.
- Persistência dos dados em planilhas Excel (arquivo `.xlsx`).

---

## 🛠️ Tecnologias e Bibliotecas
- **Python 3.12**
- **Tkinter** → para a interface gráfica.
- **ttk (Treeview, Scrollbar)** → para tabelas e rolagem.
- **openpyxl** → para salvar e manipular dados em Excel.
- **venv** → ambiente virtual para gerenciar dependências.

---

## 📂 Estrutura do Projeto
cadastro_notas/
│
├── design_tela.py          # Primeira versão da interface gráfica
├── listaMediaAlunoFinal.py # Versão evoluída com persistência em Excel
├── requirements.txt        # Dependências do projeto
└── venv/                   # Ambiente virtual (não versionado)


---

## ▶️ Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/PatriciaGheller/cadastro_notas.git
   cd cadastro_notas

2. Crie e ative o ambiente virtual:

python -m venv venv
source venv/Scripts/activate   # Git Bash / Linux / Mac
venv\Scripts\activate.bat      # Windows CMD

3. Instale as dependências:

pip install -r requirements.txt

4. Execute a interface gráfica:

python design_tela.py

ou

python listaMediaAlunoFinal.py

## 📖 Evolução das Interfaces Gráficas

- design_tela.py  
Primeira versão da interface gráfica.
Permite cadastrar alunos e visualizar as notas em uma tabela com barra de rolagem.
Os dados ficam apenas em memória (não são salvos).

- listaMediaAlunoFinal.py  
Versão evoluída.
Além da interface gráfica, implementa persistência em Excel usando openpyxl.
Isso garante que os dados cadastrados sejam salvos e possam ser consultados posteriormente.
Representa a evolução do sistema, separando responsabilidades e tornando-o mais robusto.

## 📌 Próximos Passos

- Documentar melhor no README.md exemplos de uso.

- Adicionar testes automatizados.

- Melhorar a interface gráfica com novos recursos (ex: edição e exclusão de alunos).
