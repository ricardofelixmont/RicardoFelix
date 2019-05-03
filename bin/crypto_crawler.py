#!/usr/bin/env python3 
# She-Bang, usando o env(procura o interpretador puthon3 nas variáveis de ambiente)

import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
import configparser

# Descobrindo o caminho do arquivo 'programa.ini'
path_ini = os.path.abspath("programa.ini")
lista_ini = path_ini.split("/")[:3]
arquivo = ''
for c in lista_ini:
    arquivo += c +'/'

# Acessando o caminho do arquivo 'p.ini'
conf_file = arquivo + 'CHALANGE/servidor/ricardoFelix/bin/programa.ini'
config = configparser.ConfigParser()
config.read(conf_file, encoding='utf8')

path = config.get('path', 'path_name') # Variavel path contem o caminho

print('programa Iniciado')
# Verifica se o arquivo .csv existe
def verificaExist(nome):
    return os.path.exists(nome)


# Data atual - o argumento é o objeto de referencia retornado pelo requests.get
def data_pronta():
    data = page.headers['Date'][:-4]
    data_pronta = datetime.datetime.strptime(data, '%a, %d %b %Y %H:%M:%S')
    return str(data_pronta)

# Requisitando a página e guardando em um objeto de referência
page = requests.get(url="https://m.investing.com/crypto/", headers={'User-Agent':'curl/7.52.1'})
# Transformando 'page' em um objeto BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Criando uma lista 'info' com objetos b4Soup que tenham o seletor CSS 'tr'
# Cada item da lista tem todas as informações de uma determinada cripto moeda
# O índice de cada moeda varia de 1 a 25
moedas = soup.select('tr')

'''Todas as informações petinentes sobre as moedas estão dentro de seletores CSS 'td',
então estou criando uma lista de objetos b4Soup com cada uma dessas informações, 
A lista tem tamanho 10, o indice varia da seguinte forma:
0 - Rank
1 - Nome da Moeda
2 - Preço em Relação ao Dolar
3 - Mudança nas últimas 24h
4 - Mudança na última semana
5 - Sigla
6 - Preço em Relação a BitCoin
7 - Market Cap - Valor total de Bitcoin no Mercado em Dorlar
8 - Volume de Movimentações nas últimas 24h
9 - Volume Total

Ex: infoMoedas[1] contem o nome da Cripto Moeda
'''

def cabecalho(moedas):
    infoMoeda = moedas[0].select('th')
    cabecalho = [dado.get_text().strip() for dado in infoMoeda]
    cabecalho.append('date_time')
    print(cabecalho)
    return cabecalho

nome_arquivo = path + 'ricardoFelix/crawler_crypto/' + 'crypto_' + data_pronta()[:10].strip()
# Se o arquivo nao existir, ele adiciona o cabeçalho
if verificaExist(nome_arquivo) == False: # Verificando se o arquivo existe
    cabecalho = cabecalho(moedas)
    ref_arquivo = csv.writer(open(nome_arquivo,'a+'), delimiter=';')
    ref_arquivo.writerow(cabecalho)

for c in range(1,26):
    infoMoeda = moedas[c].select('td')
    
    # Através de uma lista de compreensão listar todas as informações da 1° moeda
    # Adiciona a data atual ao final da lista de cada moeda
    lista = [dado.get_text().strip().replace(',','') for dado in infoMoeda]
    lista.append(data_pronta())
    
    # Grava (em append) as 25 listas em um arquivo relatorio.csv
    ref_arquivo = csv.writer(open(nome_arquivo, 'a+'), delimiter=';')
    ref_arquivo.writerow(lista)

