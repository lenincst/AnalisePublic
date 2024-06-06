from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import mysql.connector
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

def inicializar_navegador():
    print("--------------------------------")
    print("Navegador iniciado.")
    print("--------------------------------")
    # Inicializa o driver do navegador (neste caso, Chrome)
    driver = webdriver.Chrome()
    

    # Abre a página da web especificada
    driver.get('https://sports.sportingbet.com/pt-br/sports/futebol-4/amanh%C3%A3')

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Aguarda até que um elemento específico da página esteja visível
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))  # Substituído pelo ID do botão
        )
        print("--------------------------------")
        print("“Aceitar todos os cookies” disponivel.")
        print("--------------------------------")
        time.sleep(5)  # Espera 5 segundos
        element.click()  # Clica no botão
        print("--------------------------------")
        print("Cookies aceitos!")
        print("--------------------------------")
        time.sleep(5)
    except:
        print("Erro ao carregar a página.")
        driver.quit()

    return driver

def connect_to_database():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="D2vveaax",
            database="dadosodds"
        )
        if conexao.is_connected():
            print("--------------------------------")
            print("Conexão com MySQL estabelecida")
            print("--------------------------------")
            return conexao
    except Exception as e:
        print("--------------------------------")
        print(f"Erro ao conectar ao MySQL: {e}")
        print("--------------------------------")
        return None

def buscar_jogos(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT casa, fora FROM jogos")
    jogos = [{'casa': casa, 'fora': fora} for casa, fora in cursor]
    return jogos

from selenium.common.exceptions import NoSuchElementException

def coletar_url(driver, conexao):

    def buscar_jogos(conexao):
        cursor = conexao.cursor()
        cursor.execute("SELECT ID, casa, fora FROM jogos")
        jogos = [{'ID': ID, 'casa': casa, 'fora': fora} for ID, casa, fora in cursor]
        return jogos

    print("Navegando para SofaScore...")
    driver.get('https://www.sofascore.com/')
    time.sleep(10)
    cursor = conexao.cursor()

    jogos = buscar_jogos(conexao)

    for jogo in jogos:
        try:
            campo_pesquisa = driver.find_element("xpath", '//form[@class="Box Flex jtMoXd cQgcrM"]/input[@placeholder="Search"]')
            campo_pesquisa.click()
            time.sleep(1)
            campo_pesquisa.clear()
            time.sleep(1)
            campo_pesquisa.send_keys(jogo['casa'] + ' - ' + jogo['fora'])
            time.sleep(7)
            # Aqui, localizamos o primeiro elemento após a pesquisa e clicamos nele
            elemento = driver.find_element("css selector", '.Box.iEvFkE .Box.Flex.ghpsFf.cQgcrM')
            elemento.click()
            time.sleep(10)
            # Aqui, coletamos a URL da página atual
            url_atual = driver.current_url
            if "#id:" in url_atual:
                # Atualiza a URL no banco de dados
                cursor.execute(f"UPDATE jogos SET url_resultado = '{url_atual}' WHERE ID = {jogo['ID']}")
            else:
                # Marca a URL como inválida e remove a linha do banco de dados
                cursor.execute(f"DELETE FROM jogos WHERE ID = {jogo['ID']}")
            conexao.commit()
            # Volta para a página inicial do SofaScore
            driver.get('https://www.sofascore.com/')
            time.sleep(10)
        except NoSuchElementException:
            print(f"Elemento não encontrado para o jogo: {jogo['casa']} - {jogo['fora']}")

    print("Todas as URLs foram inseridas.")


        #colocar outro tratamento de erros pois está indo repetidas as URL, então se for repetir a url, exclui a linha
        

        



def main():
    # Inicializa o navegador
    driver = inicializar_navegador() 

    # Conecta ao banco de dados
    conexao = connect_to_database()

    buscar_jogos(conexao)

    # Coleta as odds e adiciona ao banco de dados
    coletar_url(driver, conexao)

    driver.quit()
    print("--------------------------------")
    print("Navegador fechado.")
    print("--------------------------------")

# Executa a função principal se este script for executado diretamente
if __name__ == "__main__":
    main()
