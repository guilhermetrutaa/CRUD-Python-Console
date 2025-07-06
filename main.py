import pymysql.cursors

conexao = pymysql.connect (
    host='Coloque sua host',
    user='Coloque seu user',
    password='Coloque sua senha aqui',
    database='Coloque seu banco de dados',
)

cursor = conexao.cursor()

print("--- Gerencia de Supermercado ---")
print("1. Adicionar Produto")
print("2. Listar Produtos")
print("3. Editar Nome Produto")
print("4. Editar Valor Produto")
print("5. Deletar Produto")
print("6. Sair")
print("--------------------------------")

while True:
    escolha = input("Digite o número da opção desejada: ")

    try:
        escolha_int =  int(escolha)

        if escolha_int == 1:
            print("--- Adicionar Produto ---")
            nome_produto = input("Nome do produto: ")

            while True:
                valor_str = input("Valor do produto: R$ ")
                try:
                    valor_produto = float(valor_str)
                    break
                except ValueError:
                    print("Coloque um valor válido!")

            nome = nome_produto
            valor = valor_produto

            comando_add = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
            cursor.execute(comando_add, (nome, valor))
            conexao.commit()
            print(f"Produto '{nome}' o(R$ {valor:.2f}) adicionado com sucesso!")
            break

        elif escolha_int == 2:
            comando_read = 'SELECT * FROM vendas'
            cursor.execute(comando_read)
            resultado = cursor.fetchall()
            print(resultado)
            break

        elif escolha_int == 3:
            print("--- Editar Nome Produto ---")
            nome_produto_editar = input("Nome do produto que deseja editar: ")
            nome_edit = input("Que nome deseja colocar ? ")

            nome_editar = nome_produto_editar
            nome_editDois = nome_edit

            comando_update = 'UPDATE vendas SET nome_produto = %s WHERE nome_produto = %s'
            cursor.execute(comando_update, (nome_editDois, nome_editar))
            conexao.commit()
            print(f"Produto '{nome_editar}' editado para '{nome_editDois}' com sucesso!'")
            break

        elif escolha_int == 4:
            print("--- Editar Valor Produto ---")
            nome_produto_editar = input("Nome do produto que deseja editar o valor: ")
            valor_edit = input("Que valor deseja colocar ? ")

            nome_editar = nome_produto_editar
            valor_edit = valor_edit

            comando_update = 'UPDATE vendas SET valor = %s WHERE nome_produto = %s'
            cursor.execute(comando_update, (valor_edit, nome_editar))
            conexao.commit()
            print(f"Produto '{nome_editar}' teve o valor editado para '{valor_edit}' com sucesso!'")
            break

        elif escolha_int == 5:
            print("--- Deletar Produto ---")
            nome_produto_deletar = input("Nome do produto que deseja deletar: ")

            nome_produto = nome_produto_deletar
            comando_delete = 'DELETE FROM vendas WHERE nome_produto = %s'
            cursor.execute(comando_delete, nome_produto)
            conexao.commit()
            print(f"Produto {nome_produto} deletado com sucesso!")
            break

        elif escolha_int == 6:
            print("Fechando Sistema, volte mais!")
            break


    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a opção do menu.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


conexao.close()
cursor.close()