# 📚 Sistema de Gestão Escolar 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) ![Excel](https://img.shields.io/badge/Excel-openpyxl-yellow?logo=microsoft-excel) ![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange) 

Um sistema simples de **gestão escolar** desenvolvido em Python, com interface gráfica em Tkinter e persistência de dados em Excel. Permite cadastrar alunos, calcular médias e determinar automaticamente a situação acadêmica. 

Este projeto conta com uma **interface RAD (Rapid Application Development)** contruída em **Tkinter**, seguindo princípios de **orientação a objetos**.

---

## ✨ Funcionalidades 

- Cadastro de alunos com nome e duas notas. 
- Cálculo automático da média aritmética. 
- Determinação da situação acadêmica: 
- ✅ Média >= 7 → **Aprovado** 
- ⚠️ Média >= 5 → **Recuperação** 
- ❌ Média < 5 → **Reprovado** 
- Exibição dos dados em tabela (`Treeview`) com barra de rolagem. 
- Persistência dos dados em planilhas Excel (`openpyxl`).
- Estrutura orientada a objetos para maior organização e manutenção do código. 

---

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.11** - linguagem principal
- **Tkinter** (construção da interface gráfica) 
- **ttk** - componentes avançados (Treeview, Scrollbar)
- **pandas** - manipulação e análise de dados 
- **openpyxl** leitura e escrita de planilhas Excel (.xlsx) 
- **venv** - gerenciamento de ambiente virtual 

---

## 📂 Estrutura do Projeto
cadastro_notas/
│
├── design_tela.py          # Primeira versão da interface gráfica
├── listaMediaAlunoFinal.py # Versão evoluída com persistência em Excel
├── planilhaAlunos.xlxs     # Persistência dos dados
├── rad_interface.py        # Interface gráfica e lógica principal
├── README.md               # Documentação atualizada
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

ou

python rad_interface.py

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
