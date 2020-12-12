import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="escola"
)

cursor = mydb.cursor()

def select():
    while True:
        print('\n1- ID\n2- NACIONALIDADE\n3- IDIOMA\n4- CURSO TÉCNICO\n5- VOLTAR')
        op_select = input('\nFiltrar por -> ')

        if op_select == '1':
            cond = input('\nID -> ')
            x = f'id = "{cond}"'
            cursor.execute(f'SELECT * FROM aluno where {x}')
        elif op_select == '2':
            cond = input('\nNACIONALIDADE -> ')
            x = f'nacionalidade = "{cond}"'
            cursor.execute(f'SELECT * FROM aluno where {x}')
        elif op_select == '3':
            cond = input('\nIDIOMA -> ')
            x = f'idioma = "{cond}"'
            cursor.execute(f'SELECT * FROM aluno where {x}')
        elif op_select == '4':
            cond = input('\nCURSO TÉCNICO -> ')
            x = f'cur_tec = "{cond}"'
            cursor.execute(f'SELECT * FROM aluno where {x}')
        elif op_select == '5':
            break

        print()

        myresult = cursor.fetchall()

        print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')
        print(f'|{"ID":^4}|{"NOME":^45}|{"E-MAIL":^45}|{"NACIONALIDADE":^15}|{"IDIOMA":^10}|{"CURSO TÉCNICO":^15}|')
        print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')

        for x in myresult:
            xx = str(x[2])
            xxx = str(xx[14:23])
            print(f'|{x[0]:^4}|{x[1]:^45}|{x[3]:^45}|{x[4]:^15}|{x[5]:^10}|{x[8]:^15}|')
            print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')


def select_personalizado():
    cond = input('\nCOMANDO -> ')
    cursor.execute(f'{cond}')

    print()

    myresult = cursor.fetchall()

    print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')
    print(f'|{"ID":^4}|{"NOME":^45}|{"E-MAIL":^45}|{"NACIONALIDADE":^15}|{"IDIOMA":^10}|{"CURSO TÉCNICO":^15}|')
    print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')

    for x in myresult:
        xx = str(x[2])
        xxx = str(xx[14:23])
        print(f'|{x[0]:^4}|{x[1]:^45}|{x[3]:^45}|{x[4]:^15}|{x[5]:^10}|{x[8]:^15}|')
        print('+' + '-'*4 + '+' + '-'*45 + '+' + '-'*45 + '+' + '-'*15 + '+' + '-'*10 + '+' + '-'*15 + '+')