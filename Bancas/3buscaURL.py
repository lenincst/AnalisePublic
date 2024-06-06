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

def buscar_jogos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT jogo FROM jogos")
    rows = cursor.fetchall()
    return [row[0] for row in rows]

def atualizar_url(conexao, jogo, url):
    cursor = conexao.cursor()
    query = "UPDATE jogos SET url = %s WHERE jogo = %s"
    cursor.execute(query, (url, jogo))
    conexao.commit()

def remover_jogo(conexao, jogo):
    cursor = conexao.cursor()
    query = "DELETE FROM jogos WHERE jogo = %s"
    cursor.execute(query, (jogo,))
    conexao.commit()

def inicializar_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.sofascore.com/")
    driver.maximize_window()
    time.sleep(12)
    return driver

def pesquisar(driver, texto):
    campo_pesquisa = driver.find_element("xpath", '//form[@class="Box Flex jtMoXd cQgcrM"]/input[@placeholder="Search"]')
    campo_pesquisa.click()
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(texto)
    campo_pesquisa.send_keys(Keys.RETURN)

def clicar_no_primeiro_resultado(driver):
    try:
        time.sleep(10)
        first_result = driver.find_element("xpath",'//div/a[@class="sc-ktPPKK fLZUf"]')
        first_result.click()
        time.sleep(10)  # aguarde um pouco para a página carregar
        return driver.current_url
    except NoSuchElementException:
        return "jogo não encontrado"

def principal():
    conexao = conectar_banco_dados()
    if conexao:
        jogos = buscar_jogos(conexao)

        driver = inicializar_webdriver()

        for jogo in jogos:
            pesquisar(driver, jogo)
            url = clicar_no_primeiro_resultado(driver)
            if url != "jogo não encontrado":
                atualizar_url(conexao, jogo, url)  # atualiza a URL no banco de dados
            else:
                remover_jogo(conexao, jogo)  # remove o jogo do banco de dados
            driver.get("https://www.sofascore.com/")  # volta para a página inicial
            time.sleep(2)  # aguarde um pouco para a página carregar

        conexao.close()
        driver.quit()

if __name__ == "__main__":
    principal()
