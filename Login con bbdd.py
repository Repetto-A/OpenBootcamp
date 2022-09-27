import sqlite3
import getpass
import os
from colorama import init, Fore, Back, Style

rutabbdd = r"D:\Ale\Programación\Cursos\OpenBootcamp\Python\BBDD\primerbbdd.db"

def verifica_credenciales(username,password):
    conn = sqlite3.connect(rutabbdd)
    cursor = conn.cursor()
    rows = cursor.execute(f'SELECT id FROM users WHERE username="{username}" and password="{password}"')
    data = rows.fetchone() # Devuelve un elemento o todos los coincidentes
    cursor.close()
    conn.close()
    if data == None:
        return False
    return True

def login():

    print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 1 - Login
-------------------------------{Style.RESET_ALL}
''')
    user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su ususario: ")
    if user.upper()!='V':
        password = getpass.getpass(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su contraseña: ")
        while not verifica_credenciales(user,password):
            if(password.upper()!='V') and (user.upper()!='V'):
                print()
                print(f"{Fore.RED+Style.BRIGHT}Datos incorrectos!")
                print()
                input(f'{Fore.RED+Style.BRIGHT}<Enter para intentarlo nuevamente>')
                os.system('cls')
                print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 1 - Login
-------------------------------{Style.RESET_ALL}
''')
                user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su ususario: ")
                if(user.upper()=='V'):
                    break
                password = getpass.getpass(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su contraseña: ")
            else:
                break
        if(password.upper()!='V') and (user.upper()!='V'):
            print()
            print(f"{Fore.CYAN+Style.BRIGHT}Login exitoso!")
            input(f"<Enter para volver al menú principal>{Style.RESET_ALL}")

def screen():
	os.system('cls')
	print(f'''{Fore.CYAN+Style.BRIGHT}---------------MENÚ PRINCIPAL---------------''')
	print(f'''{Style.RESET_ALL}\n 1- Login
 2- Register
 3- Delete
 0- Exit

{Fore.CYAN+Style.BRIGHT}--------------------------------------------{Style.RESET_ALL}''')

def valida(x,min,max):
    if len(x) >= min and len(x) <= max:
            return False
    else:
        return True

def delete(): # Podría pedir que sean usuarios "autorizados, para mejorarlo"

    print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 3 - Borrado de usuarios
-------------------------------{Style.RESET_ALL}
''')
    user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su ususario: ")
    while not already_exists(user):
        if(user.upper()=='V'):
            break
        print(f"{Fore.RED+Style.BRIGHT}Usuario no encontrado, inténtelo nuevamente!")
        print()
        user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] - Ingrese su ususario: ")
    if(user.upper()!='V'):
        password = getpass.getpass(f"{Fore.CYAN+Style.BRIGHT}[V - para salir] Ingrese su contraseña: ")
        while not verifica_credenciales(user,password):
            if(password.upper()=='V'):
                break
            password = getpass.getpass("[V - para salir] Ingrese su contraseña: ")
        if(password.upper()!='V'):
            print()
            res =input("¿Está seguro que desea eliminar su cuenta? Y/N: ").upper()
            while res!='Y' and res!='N':
                res =input("¿Está seguro que desea eliminar su cuenta? Y/N: ").upper()
            if res=='Y':
                conn = sqlite3.connect(rutabbdd, isolation_level=None)
                cursor = conn.cursor()
                tmp = cursor.execute(f'DELETE FROM users WHERE username="{user}" and password="{password}"')
                cursor.close()
                conn.close()
                print("Cuenta eliminada correctamente!")
                input("<Enter para volver al menú principal>")

def already_exists(user):
    conn = sqlite3.connect(rutabbdd)
    cursor = conn.cursor()
    exists = cursor.execute(f'SELECT * FROM users WHERE username="{user}"')
    data = exists.fetchone()
    cursor.close()
    conn.close()
    if data == None:
        return False
    return True

def register():

    print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 2 - Pánel de registro
-------------------------------{Style.RESET_ALL}
''')    
    # Validación de username y password
    user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] <6-20 chars> | Ingrese un ususario: ")
    while already_exists(user) or valida(user,6,20) and (user.upper()!='V'):
        if already_exists(user):
            print(f"{Fore.RED+Style.BRIGHT}El usuario ya existe!")
            input('<Enter para intentarlo nuevamente>')
            os.system('cls')
            print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 2 - Pánel de registro
-------------------------------{Style.RESET_ALL}
''')
        else:
            print()
            print(f"{Fore.RED+Style.BRIGHT}Longitud incorrecta, recuerda que debe tener entre 6 y 20 carácteres!")
            print()
            input(f'{Fore.CYAN+Style.BRIGHT}<Enter para intentarlo nuevamente>')
            os.system('cls')
            print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 2 - Pánel de registro
-------------------------------{Style.RESET_ALL}
''')
            user = input(f"{Fore.CYAN+Style.BRIGHT}[V para salir] <6-20 chars> | Ingrese un ususario: ")

    if(user.upper()!='V'):
        password = getpass.getpass(f"{Fore.CYAN+Style.BRIGHT}[V para salir] <8-20 chars> | Ingrese una contraseña: ")
        while (valida(password,8,20)) and (password.upper()!='V'):
            os.system("cls")
            print(f'''{Fore.CYAN+Style.BRIGHT}-------------------------------
OPCION 2 - Pánel de registro
-------------------------------{Style.RESET_ALL}
''')
            print(f"{Fore.RED+Style.BRIGHT}Longitud incorrecta, recuerda que debe tener entre 8 y 20 carácteres!")
            print()
            password = getpass.getpass(f"{Fore.CYAN+Style.BRIGHT}[V para salir] <8-20 chars> | Ingrese una contraseña: ")
        if(password.upper()!='V'):
            # Selección del id
            conn = sqlite3.connect(rutabbdd)
            cursor = conn.cursor()
            ultimo_id = cursor.execute('SELECT id FROM users')
            data = ultimo_id.fetchall()
            ultimo_id = str(data[len(data)-1])
            chars = '(),'
            ultimo_id = ''.join( x for x in ultimo_id if x not in chars)
            ultimo_id = int(ultimo_id)+1
            print()
            rows = cursor.execute(f'INSERT INTO users(id,username,password) VALUES ({ultimo_id},"{user}","{password}")')
            conn.commit()
            cursor.close()
            conn.close()
            print(f"{Fore.CYAN+Style.BRIGHT}Usuario registrado exitosamente!")
            print()
            input(f"{Fore.CYAN+Style.BRIGHT}<Enter para volver al menú principal>")

def menu():
    Opc = ''
    while Opc != '0':
        os.system("cls")
        screen()
        Opc=input(Fore.CYAN+Style.BRIGHT+'\n Ingrese una opción: ')
        while Opc!='0' and Opc!='1' and Opc!='2' and Opc!='3':
            Opc=input(Fore.CYAN+Style.BRIGHT+'\n Error, ingrese una opción válida: ')
        os.system('cls')
        if Opc=='1':
            login()
        elif Opc=='2':
            register()
        elif(Opc=='3'):
            delete()
        else:
            Opc='0'

def main():
    init(autoreset=True)
    menu()

if __name__ == '__main__':
    main()

# Si al hacer la conexión ponemos "isolation_level" = None se mandan al ejecutarse, si no hay que hacer conn.commit()

#rows = cursor.execute('SELECT * FROM users')                                # Toda la bbdd
#rows = cursor.execute('SELECT * FROM users WHERE username="repettoale"')    # Filtrando por usuario

#for row in rows:
#    print(row)