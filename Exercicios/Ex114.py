import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print(f'\033[31mO site pudim não está acessivel no momento')
else:
    print(f'\033[32mConsegui acessar o site do Pudim com Sucesso')
    #print(site.read()) pega o conteudo html do site que está sendo lido