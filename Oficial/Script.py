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

def contar_eventos_e_clicar_mais_eventos(driver):
    while True:
        print("--------------------------------")
        print("Contando eventos...")
        print("--------------------------------")
        # Encontra todos os eventos div com a classe 'calendar-grid-info ng-star-inserted'
        eventos = driver.find_elements(By.XPATH, "//div[@class='calendar-grid-info ng-star-inserted']")
        time.sleep(5)
        if eventos:  # Verifica se a lista 'eventos' não está vazia
            print("--------------------------------")
            print(f"{len(eventos)} eventos encontrados na página.")
            print("--------------------------------")
            time.sleep(2)
            print("--------------------------------")
            print("Redirecionando para o ultimo evento...")
            print("--------------------------------")
            time.sleep(5)
            ultimo_evento = eventos[-1]
            driver.execute_script("arguments[0].scrollIntoView();", ultimo_evento)
            print("--------------------------------")
            print("Ultimo evento na tela.")
            print("--------------------------------")
        else:  # Se a lista 'eventos' estiver vazia
            print("--------------------------------")
            print("Nenhum evento encontrado na página.")
            print("--------------------------------")

        print("--------------------------------")
        print("Verificando a existência do botão Mais Eventos...")
        print("--------------------------------")
        # Encontra todos os botao_mais_eventos div com o texto 'Mais eventos'
        botao_mais_eventos = driver.find_elements(By.XPATH, "//div[text()='Mais eventos']")
        time.sleep(5)
        if botao_mais_eventos:  # Verifica se a lista 'botao_mais_eventos' não está vazia
            print("--------------------------------")
            print("O botão 'Mais eventos' foi encontrado na página.")
            print("--------------------------------")
            time.sleep(1)
            # Cria um objeto ActionChains
            action_chains = ActionChains(driver)
            # Realiza um duplo clique no botão
            action_chains.double_click(botao_mais_eventos[0]).perform()
            print("--------------------------------")
            print("Aberto mais eventos")
            print("--------------------------------")
            time.sleep(5)
        else:  # Se a lista 'botao_mais_eventos' estiver vazia
            print("--------------------------------")
            print("O elemento 'Mais eventos' não foi encontrado na página.")
            print("--------------------------------")
            break  # Sai do loop
    time.sleep(5)

def coletar_participantes(driver, conexao):
    print("--------------------------------")
    print("Verificando os nomes dos participantes...")
    print("--------------------------------")
    time.sleep(2)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.participants-pair-game div.participant-wrapper div.participant")))
        participantes = driver.find_elements(By.CSS_SELECTOR, "div.participants-pair-game div.participant-wrapper div.participant")
        time.sleep(2)
        contador = 0  # Inicializa o contador
        jogos_ignorados = 0  # Inicializa o contador de jogos ignorados
        cursor = conexao.cursor()
        cursor.execute("TRUNCATE TABLE jogos")  # Limpa a tabela
        if participantes:
            print("--------------------------------")
            for i in range(0, len(participantes), 2):
                for _ in range(3):  # Tenta até 3 vezes
                    try:
                        driver.execute_script("arguments[0].scrollIntoView();", participantes[i])  # Rola a página até o elemento
                        time.sleep(1)  # Aguarda um pouco para a página carregar
                        participante1 = participantes[i].text.replace("Feminina", "").replace("Feminino", "").strip()
                        participante2 = participantes[i+1].text.replace("Feminina", "").replace("Feminino", "").strip() if i+1 < len(participantes) else ''
                        if participante1 and participante2:  # Se ambos os nomes dos times foram coletados
                            query = f"INSERT INTO jogos (casa, fora) VALUES ('{participante1}', '{participante2}')"
                            cursor.execute(query)  # Adiciona o jogo à tabela
                            print(f"{participante1} - {participante2}")
                            contador += 1  # Incrementa o contador
                            break  # Sai do loop
                        else:
                            print("Carregando novamente...")
                            time.sleep(5)  # Aguarda um pouco antes de tentar novamente
                    except StaleElementReferenceException:
                        print("Referência de elemento obsoleto encontrada. Tentando localizar o elemento novamente...")
                        participantes = driver.find_elements(By.CSS_SELECTOR, "div.participants-pair-game div.participant-wrapper div.participant")
                else:  # Se o loop terminou normalmente (não foi interrompido por um 'break')
                    print("Não foi possível carregar os nomes dos times após 3 tentativas. Ignorando este jogo.")
                    jogos_ignorados += 1  # Incrementa o contador de jogos ignorados
            conexao.commit()  # Commit as mudanças
            print("--------------------------------")
            print(f"Encontrados {contador} jogos")  # Imprime o número de jogos encontrados
            print(f"Ignorados {jogos_ignorados} jogos")  # Imprime o número de jogos ignorados
            print("--------------------------------")
            time.sleep(5)
        else:
            print("--------------------------------")
            print("Nenhum participante encontrado na página.")
            print("--------------------------------")
            time.sleep(5)
    except Exception as e:
        print(f"Erro ao tentar encontrar os participantes: {str(e)}")
    time.sleep(5)

def coletar_odd(driver, conexao):
    print("--------------------------------")
    print("Alterando página para buscar ODDs...")
    print("--------------------------------")
    driver.get('https://sports.sportingbet.com/pt-br/sports/futebol-4/amanh%C3%A3?popup=betfinder')
    time.sleep(10)
    search_field = driver.find_element(By.CSS_SELECTOR,'body > div.cdk-overlay-container > ms-modal-window > div > div > div.modal-body > ms-modal-dialog > ms-popup-proxy > ms-betfinder > ms-autocomplete > div.search-bar > ms-autocomplete-input > form > input')
    time.sleep(2)
    print("--------------------------------")
    print("coletando ODDs...")
    print("--------------------------------")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()
    for jogo in jogos:
        id_jogo, participante1, _, participante2, _, _, _, _, _, _, _, _, _ = jogo
        search_field.clear()  # Limpa o campo de entrada
        search_field.send_keys(f"{participante1} - {participante2}")  # Preenche o campo de entrada
        search_field.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            odds = driver.find_elements(By.CSS_SELECTOR, 'body > div.cdk-overlay-container > ms-modal-window > div > div > div.modal-body > ms-modal-dialog > ms-popup-proxy > ms-betfinder > ms-autocomplete > div.popular-recent-search-suggestion > div.events.popup-body.ng-star-inserted > div > ms-grid-search-result-card > div.competition-search-result-card > ms-grid > div > ms-event-group > ms-event > div > div')
            # Crie uma lista para armazenar os textos
            textos = []
            for odd in odds:
                texto = odd.text
                textos.append(texto)
            time.sleep(3)
            lista = textos[0].split('\n')  # Separa o primeiro elemento da lista 'textos' em uma nova lista
            try:
                odd_casa = float(lista[0])  # Obtém o texto do primeiro elemento da lista
                odd_visitante = float(lista[2])  # Obtém o texto do terceiro elemento da lista
                print(f"{participante1} ({odd_casa}) - {participante2} ({odd_visitante})")
                if odd_casa < odd_visitante:
                    time_favorito = participante1
                    odd_favorito = odd_casa
                    time_normal = participante2
                    odd_normal = odd_visitante
                else:
                    time_favorito = participante2
                    odd_favorito = odd_visitante
                    time_normal = participante1
                    odd_normal = odd_casa
                diferenca_odd = odd_normal - odd_favorito
                cursor.execute(f"UPDATE jogos SET time_favorito='{time_favorito}', time_normal='{time_normal}', odd_favorito={odd_favorito}, odd_normal={odd_normal}, diferenca_odd={diferenca_odd} WHERE ID={id_jogo}")
                conexao.commit()
            except ValueError:
                print(f"Não foi possível converter as odds para o jogo {participante1} - {participante2} para float. Tentando novamente com apenas {participante1}.")
        except (NoSuchElementException, IndexError):  # Adicionado IndexError para lidar com a lista vazia
            print(f"Não foi possível encontrar as odds para o jogo {participante1} - {participante2}. Tentando novamente com apenas {participante1}.")
            search_field.clear()  # Limpa o campo de entrada
            search_field.send_keys(f"{participante1}")  # Preenche o campo de entrada com apenas o participante1
            search_field.send_keys(Keys.RETURN)
            time.sleep(3)
            try:
                # Repita o processo de coleta de odds
                odds = driver.find_elements(By.CSS_SELECTOR, 'body > div.cdk-overlay-container > ms-modal-window > div > div > div.modal-body > ms-modal-dialog > ms-popup-proxy > ms-betfinder > ms-autocomplete > div.popular-recent-search-suggestion > div.events.popup-body.ng-star-inserted > div > ms-grid-search-result-card > div.competition-search-result-card > ms-grid > div > ms-event-group > ms-event > div > div')
                textos = []
                for odd in odds:
                    texto = odd.text
                    textos.append(texto)
                time.sleep(1)
                lista = textos[0].split('\n')
                odd_casa = float(lista[0])  # Obtém o texto do primeiro elemento da lista
                odd_visitante = float(lista[2])  # Obtém o texto do terceiro elemento da lista
                print(f"{participante1} ({odd_casa}) - {participante2} ({odd_visitante})")
                if odd_casa < odd_visitante:
                    time_favorito = participante1
                    odd_favorito = odd_casa
                    time_normal = participante2
                    odd_normal = odd_visitante
                else:
                    time_favorito = participante2
                    odd_favorito = odd_visitante
                    time_normal = participante1
                    odd_normal = odd_casa
                diferenca_odd = odd_normal - odd_favorito
                cursor.execute(f"UPDATE jogos SET time_favorito='{time_favorito}', time_normal='{time_normal}', odd_favorito={odd_favorito}, odd_normal={odd_normal}, diferenca_odd={diferenca_odd} WHERE ID={id_jogo}")
                conexao.commit()
            except (NoSuchElementException, IndexError, ValueError):
                print(f"Não foi possível encontrar ou converter as odds para o jogo {participante1}. Removendo este jogo do banco de dados.")
                cursor.execute(f"DELETE FROM jogos WHERE ID={id_jogo}")
                conexao.commit()
    print("--------------------------------")
    print("ODDs coletadas e adicionadas ao banco de dados.")
    print("--------------------------------")

def coletar_url(driver, conexao):
    print("Navegando para SofaScore...")
    driver.get('https://www.sofascore.com/')
    time.sleep(10)
    campo_pesquisa = driver.find_element("xpath", '//form[@class="Box Flex jtMoXd cQgcrM"]/input[@placeholder="Search"]')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()
    for jogo in jogos:
        id_jogo, participante1, _, participante2, _, _, _, _, _, _, _, _, _ = jogo
        print(f"Pesquisando: {participante1} - {participante2}")
        campo_pesquisa.click()
        campo_pesquisa.clear()
        campo_pesquisa.send_keys(f"{participante1} - {participante2}")
        campo_pesquisa.send_keys(Keys.RETURN)
        time.sleep(5)
        
        try:
            time.sleep(5)
            first_result = driver.find_element("xpath",'//div/a[@class="sc-ktPPKK fLZUf"]')
            first_result.click()
            time.sleep(2)
            campo_pesquisa.click()
            time.sleep(5)
            campo_pesquisa.clear()
            time.sleep(2)  # aguarde um pouco para a página carregar
            url_jogo = driver.current_url
            if "#id:" in url_jogo:
                print(f"URL do jogo {participante1} - {participante2}: {url_jogo}")
                cursor.execute(f"UPDATE jogos SET url_resultado='{url_jogo}' WHERE ID={id_jogo}")
                conexao.commit()
            else:
                print(f"URL inválida para o jogo {participante1} - {participante2}. Removendo este jogo do banco de dados.")
                cursor.execute(f"DELETE FROM jogos WHERE ID={id_jogo}")
                conexao.commit()
        except NoSuchElementException:
            print("Jogo não encontrado")
    print("--------------------------------")
    print("URLs coletadas e adicionadas ao banco de dados.")
    print("--------------------------------")


    
#preciso corrigir na coletar_odd o except ValueError: pois não entendi se ele pode deixar passar jogo sem pesquisar o primeiro time
#ja no coletar url não está clicando
#preciso de uma função onde jogue todos esses dados a um tabela "esperando resultado" que serão adicionados depois dos jogos os resultados
#criar um script onde ira buscar atraves da url o resultado
#preciso de uma função onde jogue todos esses dados a um banco onde sera os dados finalizados, esse banco é permanente e será feita analise atraves dos dados dele


def main():
    # Inicializa o navegador
    driver = inicializar_navegador() 
    conexao = connect_to_database()
    contar_eventos_e_clicar_mais_eventos(driver)
    coletar_participantes(driver, conexao)
    odds_validas = coletar_odd(driver, conexao)
    urls_validas = coletar_url(driver, conexao)
    driver.quit()
    print("--------------------------------")
    print("Navegador fechado.")
    print("--------------------------------")

# Executa a função principal se este script for executado diretamente
if __name__ == "__main__":
    main()


