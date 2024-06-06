import mysql.connector

def connect_to_database():
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

def fetch_and_compare_odds(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT time_casa, time_visitante, odd_casa, odd_visitante FROM partidas")
    rows = cursor.fetchall()

    for row in rows:
        time_casa, time_visitante, odd_casa, odd_visitante = row
        jogo = f"{time_casa} - {time_visitante}"
        if odd_casa < odd_visitante:
            odd = f"odd_casa: {odd_casa}"
        else:
            odd = f"odd_visitante: {odd_visitante}"
        cursor.execute("INSERT INTO jogos (jogo, odd) VALUES (%s, %s)", (jogo, odd))

def main():
    conexao = connect_to_database()
    if conexao:
        fetch_and_compare_odds(conexao)
        conexao.commit()
        conexao.close()

if __name__ == "__main__":
    main()
