import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yecgaa',
    database='bdcrud',
)

cursor = conexao.cursor()


#CREATE
nome_produto = "Descongex"
valor = 12
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit() #edita o banco de dados
resultado = cursor.fetchall()#lendo o banco de dados
#Fim CREATE

#READ 
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
#conexao.commit() #edita o banco de dados
resultado = cursor.fetchall() #lendo o banco de dados

print(resultado)

#/READ

#UPDATE
nome_produto = "Todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #edita o banco de dados

#FIM UPDATE



#DELETE
nome_produto = "Todynho"
comando = f'DELETE vendas SET valor = WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() #edita o banco de dados
#DELETE




cursor.close()
conexao.close()
