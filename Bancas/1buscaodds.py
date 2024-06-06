import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector

# Função para criar conexão com o banco de dados MySQL
def criar_conexao():
    try:
        # Tenta estabelecer a conexão com o banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="D2vveaax",
            database="odds"
        )
        # Verifica se a conexão foi estabelecida com sucesso
        if conexao.is_connected():
            print("Conexão com MySQL estabelecida")
            return conexao
    except Exception as e:
        # Imprime um erro caso a conexão falhe
        print(f"Erro ao conectar ao MySQL: {e}")

# Função para inicializar o navegador e configurar a página web
def inicializar_navegador():
    print("Inicializando o navegador...")
    # Inicializa o driver do navegador (neste caso, Chrome)
    driver = webdriver.Chrome()

    # Abre a página da web especificada
    driver.get('https://sports.sportingbet.com/pt-br/sports/futebol-4/amanh%C3%A3')

    # Maximiza a janela do navegador
    driver.maximize_window()

    # Aguarda 12 segundos para garantir que a página carregue completamente
    time.sleep(12)

    # Tenta aceitar os cookies, se o botão estiver presente
    try:
        botao_aceitar_cookies = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        botao_aceitar_cookies.click()
    except Exception as e:
        print(f"Erro ao tentar aceitar cookies: {e}")

    return driver

# Função para obter a data atual
def obter_data_partida():
    # Obtém a data atual no formato 'AAAA-MM-DD'
    data_partida = datetime.now().strftime('%Y-%m-%d')
    return data_partida

# Função para obter os elementos dos participantes dos jogos
def obter_participantes_e_times(driver):
    print("Obtendo participantes e times...")
    # Encontra todos os elementos que representam os participantes dos jogos
    participantes = driver.find_elements(By.CSS_SELECTOR, 'div.participants-pair-game')
    if participantes:
        print("Elementos dos participantes encontrados.")
    else:
        print("Elementos dos participantes não encontrados.")
    return participantes

# Função para imprimir e armazenar informações das partidas
def imprimir_partidas(driver, partida_num, eventos):
    print("Imprimindo partidas...")
    # Lista para armazenar as partidas
    partidas = []
    # Itera sobre cada evento (partida)
    for evento in eventos:
        # Obtém os nomes dos times
        times_elements = evento.find_elements(By.CSS_SELECTOR, 'div.participants-pair-game div.participant-wrapper div.participant')
        times = ' vs '.join([time.text for time in times_elements])
        time.sleep(2)
        # Obtém as odds (probabilidades) para os times
        odds = evento.find_elements(By.CSS_SELECTOR, 'ms-option.grid-option.ng-star-inserted')
        # Verifica se há elementos suficientes para odds
        if len(odds) < 3:
            continue  # Pula para o próximo evento se não houver elementos suficientes

        # Obtém as odds de vitória para o time da casa e o visitante
        odd_casa = odds[0].find_element(By.CSS_SELECTOR, 'div.option-value ms-font-resizer').text
        odd_visitante = odds[2].find_element(By.CSS_SELECTOR, 'div.option-value ms-font-resizer').text

        # Imprime os detalhes da partida
        print(f"Partida {partida_num} - {times}: | Casa: {odd_casa} | Fora: {odd_visitante} |")
        # Adiciona a partida à lista de partidas
        time.sleep(2)
        partidas.append((partida_num, times, odd_casa, odd_visitante))
        partida_num += 1

    return partida_num, partidas

# Função para rolar a página até o último participante visível
def rolar_ate_ultimo_participante(driver, participantes):
    print("Rolando até o último participante...")
    # Pausa para garantir que a página está carregada
    time.sleep(2)
    # Encontra o último elemento participante
    elemento_rodape = participantes[-1]
    print("Último participante encontrado.")
    time.sleep(2)
    # Rola a página até o último participante
    driver.execute_script("arguments[0].scrollIntoView();", elemento_rodape)
    # Aguarda 5 segundos para que o conteúdo carregue
    time.sleep(5)

# Função para clicar no botão "Mais eventos"
def clicar_mais_eventos(driver):
    print("Clicando em 'Mais eventos'...")
    try:
        # Aguarda até que o elemento esteja visível
        elemento = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Mais eventos']"))
        )
        print("Elemento 'Mais eventos' encontrado.")
        time.sleep(2)
        # Realiza um clique duplo no elemento
        ActionChains(driver).double_click(elemento).perform()
        time.sleep(5)
    except:
        print("Elemento 'Mais eventos' não encontrado.")
        return False

    return True

# Função para inserir os dados das partidas no banco de dados
def inserir_dados(conexao, data_partida, partidas):
    print("Inserindo dados no banco de dados...")
    cursor = conexao.cursor()
    # Itera sobre cada partida
    for partida in partidas:
        numero_partida, times, odd_casa, odd_visitante = partida
        time_casa, time_visitante = times.split(' vs ')
        # Substitui vírgulas por pontos nas odds
        odd_casa = odd_casa.replace(',', '.')
        odd_visitante = odd_visitante.replace(',', '.')
        # Define a query SQL para inserir os dados
        query = "INSERT INTO Partidas (data_partida, numero_partida, time_casa, time_visitante, odd_casa, odd_visitante) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (data_partida, numero_partida, time_casa, time_visitante, odd_casa, odd_visitante)
        # Executa a query
        try:
            cursor.execute(query, valores)
            print(f"Dados inseridos com sucesso para a partida {numero_partida}")
        except Exception as e:
            print(f"Erro ao inserir dados para a partida {numero_partida}: {e}")
    # Confirma as alterações no banco de dados
    conexao.commit()

# Função principal que coordena todas as operações
def principal():
    # Cria conexão com o banco de dados
    conexao = criar_conexao()
    # Inicializa o navegador
    driver = inicializar_navegador()
    # Obtém a data atual
    data_partida = obter_data_partida()
    partida_num = 1
    ultimo_numero_eventos = 0
    while True:
        # Rola até o último participante visível
        rolar_ate_ultimo_participante(driver, obter_participantes_e_times(driver))
        time.sleep(5)
        # Clica em "Mais eventos" até que não haja mais eventos para carregar
        while clicar_mais_eventos(driver):
            pass
        # Obtém os participantes e times
        participantes = obter_participantes_e_times(driver)
        # Verifica se o número de eventos aumentou
        time.sleep(5)
        if len(participantes) == ultimo_numero_eventos:
            break
        ultimo_numero_eventos = len(participantes)
        # Imprime as partidas e obtém os detalhes
        partida_num, partidas = imprimir_partidas(driver, partida_num, participantes)
        # Insere os dados das partidas no banco de dados
        time.sleep(5)
        inserir_dados(conexao, data_partida, partidas)
    # Fecha o navegador
    driver.quit()
    # Fecha a conexão com o banco de dados
    conexao.close()

# Executa a função principal se este script for executado diretamente
if __name__ == "__main__":
    principal()
