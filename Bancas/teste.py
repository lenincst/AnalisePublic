from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Importe Keys para usar Keys.RETURN
from selenium.common.exceptions import NoSuchElementException  # Importe NoSuchElementException para lidar com exceções
import time

# Inicialize o driver do navegador (por exemplo, Chrome)
driver = webdriver.Chrome()
driver.maximize_window()
participante1 = "Mirassol"
participante2 = "Guarani"
print("--------------------------------")
print("Alterando página para buscar ODDs...")
print("--------------------------------")
driver.get('https://sports.sportingbet.com/pt-br/sports/futebol-4/amanh%C3%A3?popup=betfinder')
time.sleep(15)
search_field = driver.find_element(By.CSS_SELECTOR,'body > div.cdk-overlay-container > ms-modal-window > div > div > div.modal-body > ms-modal-dialog > ms-popup-proxy > ms-betfinder > ms-autocomplete > div.search-bar > ms-autocomplete-input > form > input')
time.sleep(2)
print("--------------------------------")
print("coletando ODDs...")
print("--------------------------------")
search_field.clear()  # Limpa o campo de entrada
search_field.send_keys(f"{participante1} - {participante2}")  # Preenche o campo de entrada com o jogo atual
search_field.send_keys(Keys.RETURN)
time.sleep(7)
try:
        odds = driver.find_elements(By.CSS_SELECTOR, 'body > div.cdk-overlay-container > ms-modal-window > div > div > div.modal-body > ms-modal-dialog > ms-popup-proxy > ms-betfinder > ms-autocomplete > div.popular-recent-search-suggestion > div.events.popup-body.ng-star-inserted > div > ms-grid-search-result-card > div.competition-search-result-card > ms-grid > div > ms-event-group > ms-event > div > div')
        
        print("Todos os valores na lista 'textos':", {odds})
        time.sleep(10)
        lista = textos[0].split('\n')  # Separa o primeiro elemento da lista 'textos' em uma nova lista
        odd_casa = lista[0]  # Obtém o texto do primeiro elemento da lista
        odd_visitante = lista[2]  # Obtém o texto do terceiro elemento da lista
        print(f"{participante1} ({odd_casa}) - {participante2} ({odd_visitante})")
except NoSuchElementException:
        print(f"Não foi possível encontrar as odds para o jogo {participante1} - {participante2}. Passando para o próximo jogo.")
