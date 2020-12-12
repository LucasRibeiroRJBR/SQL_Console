import mysql.connector
from util import select, select_personalizado


while True:
    op = input('\n1- SELECT;\n2- SELECT (Personalizado)\n3- SAIR\n\n-> ')

    if op == '1':
        select()
    if op == '2':
        select_personalizado()
    if op == '3':
        break
