import six.moves.xmlrpc_client as xmlrpclib
from funcoes import *

'''
url = "http://xxx.com.br:8069"
db = "odoo_xxx"
username = 'xxx@xxx.com.br'
uid = 112
password = "xxxx"
'''
print("-------------------------")
print("- Entrega Contínua Odoo -")
print("-------------------------")

print("Iniciando leitura do arquivo...")
arquivo = open("modulos.txt", "r")

conteudo = arquivo.read()

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

for linha in conteudo.split('\n'):
    modulo = buscar_modulo(models, db, uid, password, linha)
    print("Atualizando módulo " + str(modulo))
    atualizar_modulo(models, db, uid, password, modulo)

print("Fechando o arquivo...")
arquivo.close()