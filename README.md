
# 🛒 CRUD de Gerenciamento de Supermercado

Este é um projeto simples de **CRUD (Create, Read, Update, Delete)** desenvolvido em **Python** utilizando o **MySQL** como banco de dados. O sistema simula a gestão de produtos de um supermercado via terminal, permitindo adicionar, listar, editar e excluir produtos de forma prática.

## 💻 Tecnologias Utilizadas
- Python
- MySQL
- Biblioteca `pymysql`

## ⚙️ Funcionalidades
- ✅ Adicionar produto
- ✅ Listar produtos
- ✅ Editar nome de um produto
- ✅ Editar valor de um produto
- ✅ Deletar produto
- ✅ Encerrar o sistema

## 🗂️ Estrutura do Banco de Dados

Você precisa criar um banco de dados MySQL com a seguinte estrutura:

```sql
CREATE DATABASE bdyoutube;

USE bdyoutube;

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255),
    valor DECIMAL(10, 2)
);
```

## 🚀 Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/guilhermetrutaa/CRUD-Python-Console.git
```

2. Instale a biblioteca necessária:
```bash
pip install pymysql
```

3. Configure a conexão com o banco de dados no código:
```python
conexao = pymysql.connect (
    host='Coloque sua host',
    user='Coloque seu user',
    password='Coloque sua senha aqui',
    database='Coloque seu banco de dados',
)
```

4. Execute o arquivo Python:
```bash
python nome_do_arquivo.py
```

## 📋 Como Usar

Ao rodar o sistema, será exibido um menu com as seguintes opções:
- `1` - Adicionar Produto
- `2` - Listar Produtos
- `3` - Editar Nome Produto
- `4` - Editar Valor Produto
- `5` - Deletar Produto
- `6` - Sair do Sistema

Basta digitar o número da opção desejada e seguir as instruções no terminal.

## 💡 Observações
- Este projeto é apenas um exemplo didático e pode ser aprimorado para incluir tratamento de erros mais robusto, integração com interface gráfica, e melhorias no design da base de dados.
- O sistema realiza todas as operações diretamente no banco de dados, por isso é importante garantir que as credenciais e permissões estejam corretas.

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
