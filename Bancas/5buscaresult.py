from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import time
import os

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

def buscar_urls(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT url FROM jogos")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def atualizar_resultado(conexao, url, resultado):
    cursor = conexao.cursor()
    query = "UPDATE jogos SET resultado = %s WHERE url = %s"
    cursor.execute(query, (resultado, url))
    conexao.commit()

def inicializar_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    time.sleep(12)
    return driver

def coletar_resultado(driver):
    try:
        resultado = driver.find_element("xpath", '//div[@class="Box iCtkKe"]/span[@class="Text glganO"]').text
        return resultado
    except NoSuchElementException:
        return "resultado não encontrado"

def principal():
    conexao = conectar_banco_dados()
    if conexao:
        urls = buscar_urls(conexao)

        driver = inicializar_webdriver()

        for url in urls:
            driver.get(url)
            time.sleep(10)  # aguarde um pouco para a página carregar
            resultado = coletar_resultado(driver)
            print(f"Resultado para a URL {url}: {resultado}")
            atualizar_resultado(conexao, url, resultado)  # atualiza o resultado no banco de dados

        conexao.close()
        driver.quit()

if __name__ == "__main__":
    principal()
