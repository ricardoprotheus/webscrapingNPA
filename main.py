import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Abrir o url do site
def abrirURL(url):
    option = Options()
    option.headless = True
    driver = webdriver.Chrome(options=option)  # executar em segundo plano
    driver.get(url)
    time.sleep(3)  # esperar o site abrir
    return driver

#salvar arquivo em csv
def salvarCsv(arquivo, name):
    soup = BeautifulSoup(arquivo, 'html.parser')
    table = soup.find(name='table')
    data_frame = pd.read_html(str(table))[0]
    data_frame.to_excel(f'{name}.xlsx')
    data_frame.to_csv(f'{name}.csv')

urlNBA = "https://www.nba.com/stats/leaders/"




# Cotações NBA
driver = abrirURL(urlNBA)
element = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table")
html_content = element.get_attribute('outerHTML')
salvarCsv(html_content, 'acoesNBA')


