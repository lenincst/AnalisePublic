import mysql.connector

def conectar_banco_dados():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="D2vveaax",
            database="odds"
        )
        if conexao.is_connected():
            print("Conexão com MySQL estabelecida")
            return conexao
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def excluir_jogos_nao_encontrados(conexao):
    cursor = conexao.cursor()
    query = "DELETE FROM jogos WHERE url = 'jogo não encontrado'"
    cursor.execute(query)
    conexao.commit()
    print(f"{cursor.rowcount} linhas foram deletadas.")

def principal():
    conexao = conectar_banco_dados()
    if conexao:
        excluir_jogos_nao_encontrados(conexao)
        conexao.close()

if __name__ == "__main__":
    principal()
