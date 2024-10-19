# Sistema de Gerenciamento de Clientes

Este é um sistema simples de gerenciamento de clientes desenvolvido com **Flask** e **SQLite**. O sistema permite adicionar, consultar e visualizar informações dos clientes em uma tabela, além de possibilitar a exportação dos dados para Excel.

## Funcionalidades

- **Adicionar cliente**: Preencher um formulário com nome, endereço, telefone e e-mail.
- **Consultar cliente**: Buscar um cliente pelo nome e visualizar os detalhes.
- **Visualizar clientes**: Exibir todos os clientes cadastrados em uma tabela.
- **Exportar para Excel**: Exportar a lista de clientes para um arquivo Excel.

## Tecnologias Utilizadas

- **Python (Flask)**: Framework web para criar o back-end.
- **SQLite**: Banco de dados leve e local.
- **Bootstrap**: Biblioteca CSS para responsividade e layout.
- **Pandas**: Biblioteca para manipulação de dados e exportação para Excel.

## Requisitos

Certifique-se de ter o seguinte instalado:

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/sistemadeclientes.git
   cd sistemadeclientes

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows

pip install -r requirements.txt

python app.py

O sistema estará rodando em http://127.0.0.1:5000.

Uso
1. Adicionar Cliente
Acesse http://127.0.0.1:5000/add para abrir a página de formulário.
Preencha os campos Nome, Endereço, Telefone e E-mail e clique em "Adicionar Cliente".
2. Visualizar Clientes
Acesse http://127.0.0.1:5000/view para visualizar a lista de clientes cadastrados em uma tabela.
Use a opção "Exportar para Excel" para baixar a tabela de clientes em formato .xlsx.
3. Consultar Cliente
Acesse http://127.0.0.1:5000/search para buscar um cliente pelo nome.

Estrutura de Diretórios

/project
│
├── /templates
│   ├── add_client.html
│   ├── search_client.html
│   ├── view_clients.html
├── /static
│   ├── /css
│   │   ├── style.css
├── app.py
├── database.db
├── README.md
├── requirements.txt


Aqui está o arquivo README.md para a sua aplicação Flask com banco de dados SQLite, detalhando os passos de instalação, execução e funcionalidades.

md
Copiar código
# Sistema de Gerenciamento de Clientes

Este é um sistema simples de gerenciamento de clientes desenvolvido com **Flask** e **SQLite**. O sistema permite adicionar, consultar e visualizar informações dos clientes em uma tabela, além de possibilitar a exportação dos dados para Excel.

## Funcionalidades

- **Adicionar cliente**: Preencher um formulário com nome, endereço, telefone e e-mail.
- **Consultar cliente**: Buscar um cliente pelo nome e visualizar os detalhes.
- **Visualizar clientes**: Exibir todos os clientes cadastrados em uma tabela.
- **Exportar para Excel**: Exportar a lista de clientes para um arquivo Excel.

## Tecnologias Utilizadas

- **Python (Flask)**: Framework web para criar o back-end.
- **SQLite**: Banco de dados leve e local.
- **Bootstrap**: Biblioteca CSS para responsividade e layout.
- **Pandas**: Biblioteca para manipulação de dados e exportação para Excel.

## Requisitos

Certifique-se de ter o seguinte instalado:

- Python 3.x
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/sistemadeclientes.git
   cd sistemadeclientes
Crie e ative um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Inicialize o banco de dados e execute o servidor:

bash
Copiar código
python app.py
O sistema estará rodando em http://127.0.0.1:5000.

Uso
1. Adicionar Cliente
Acesse http://127.0.0.1:5000/add para abrir a página de formulário.
Preencha os campos Nome, Endereço, Telefone e E-mail e clique em "Adicionar Cliente".
2. Visualizar Clientes
Acesse http://127.0.0.1:5000/view para visualizar a lista de clientes cadastrados em uma tabela.
Use a opção "Exportar para Excel" para baixar a tabela de clientes em formato .xlsx.
3. Consultar Cliente
Acesse http://127.0.0.1:5000/search para buscar um cliente pelo nome.
Estrutura de Diretórios
bash
Copiar código
/project
│
├── /templates
│   ├── add_client.html
│   ├── search_client.html
│   ├── view_clients.html
├── /static
│   ├── /css
│   │   ├── style.css
├── app.py
├── database.db
├── README.md
├── requirements.txt
Personalização
Banco de Dados: O banco de dados SQLite está configurado para criar automaticamente o arquivo database.db na primeira execução.
Exportação: Os dados dos clientes podem ser exportados para Excel usando a biblioteca Pandas.
Dependências
As dependências estão listadas no arquivo requirements.txt:

Flask==2.0.1
pandas==1.3.3
openpyxl==3.0.7

Instale todas as dependências com:

pip install -r requirements.txt

Próximos Passos
Implementar funcionalidades de edição e remoção de clientes.
Adicionar autenticação para maior segurança.
Expandir o sistema para lidar com múltiplos departamentos ou filiais.
