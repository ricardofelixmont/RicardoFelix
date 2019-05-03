''' Pega o caminho absoluto e gera o arquivo .ini '''
import os

absolute_path = os.path.abspath("crypto_crawler.py")

path_list = absolute_path.split("/")[:-3]

path = ''
for dir_ in path_list:
    path += dir_ + '/'

caminho_ini = path +  'ricardoFelix/bin/programa.ini'

string = '[path]\n\n' + 'path_name = ' + path

with open(caminho_ini, 'w') as f:
    f.write(string)    
