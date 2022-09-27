import sqlite3
import os

def crea_tabla(nombre):
    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    rows = cursor.execute(f'CREATE TABLE {nombre} (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);')
    cursor.close()
    conn.close

def valida(x,min,max):
    if len(x) >= min and len(x) <= max:
            return False
    else:
        return True

def agrega_alumno():

    nombre = input("[4-20 chars] | Ingrese el nombre del alumno: ").capitalize()
    apellido = input("[4-20 chars] | Ingrese el apellido del alumno: ").capitalize()
    while already_exists(nombre,apellido) or valida(nombre,4,20) or valida(apellido,4,20):
        if(already_exists(nombre,apellido)):
            print("El alumno que intenta cargar ya existe!")
        else:
            print("Longitud incorrecta!")
        nombre = input("[4-20 chars] | Ingrese el nombre del alumno: ")
        apellido = input("[4-20 chars] | Ingrese el apellido del alumno: ")
            
    id = ult_id()
    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    tmp = cursor.execute(f'INSERT INTO Alumnos (id,nombre,apellido) VALUES ({id},"{nombre}","{apellido}")')
    conn.commit()
    cursor.close()
    conn.close()
    print()
    print("Alumno cargado correctamente!")
    print()
    input("<Enter para volver al menú principal>")

def ult_id():
    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    ultimo_id = cursor.execute('SELECT id FROM Alumnos')
    data = ultimo_id.fetchall()
    cursor.close()
    conn.close()
    if(len(data)==0):
        id=1
    else:
        id = str(data[len(data)-1])
        chars = '(),'
        id = ''.join( x for x in id if x not in chars)
        id = int(id)+1
    
    return id

def already_exists(nombre, apellido):
    global data

    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    exists = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre="{nombre}" and apellido="{apellido}"')
    data = exists.fetchone()
    cursor.close()
    conn.close()
    if data == None:
        return False
    return True

def busqueda():

    nombre = input("Ingrese el nombre del alumno a buscar: ").capitalize()
    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    exists = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre="{nombre}"')
    data = exists.fetchall()
    cursor.close()
    conn.close()
    print(f"Lista de todos los alumos llamados {nombre}: ")
    for alumno in data:
        print()
        print(f"Id: {alumno[0]}")
        print(f"Nombre: {alumno[1]}")
        print(f"Apellido: {alumno[2]}")
    print()
    input("<Enter para volver al menú principal>")

def screen():
	os.system('cls')
	print('''---------------MENÚ PRINCIPAL---------------''')
	print('''\n 1- Cargar alumno
 2- Busqueda de un alumno
 0- Exit

--------------------------------------------''')

def menu():
    Opc = ''
    while Opc != '0':
        os.system("cls")
        screen()
        Opc=input('\n Ingrese una opción: ')
        while Opc!='0' and Opc!='1' and Opc!='2' and Opc!='3':
            Opc=input('\n Error, ingrese una opción válida: ')
        os.system('cls')
        if Opc=='1':
            agrega_alumno()
        elif Opc=='2':
            busqueda()

def Carga_directa(nombre,apellido):
    id = ult_id()
    conn = sqlite3.connect('bbdd.db')
    cursor = conn.cursor()
    tmp = cursor.execute(f'INSERT INTO Alumnos (id,nombre,apellido) VALUES ({id},"{nombre}","{apellido}")')
    conn.commit()
    cursor.close()
    conn.close()

def main():
    crea_tabla('Alumnos')
    Carga_directa('Juancito','Perez') # Para cargar directamente por parametros (solo para probarlo, obviamente no es la idea evitar las validaciones)
    Carga_directa('Rodrigo','Fantasio') # Cargo varios Rodrigo para que prueben la busqueda por nombre
    Carga_directa('Ramiro','Magnesio')
    Carga_directa('Mequede','Sinideas')
    Carga_directa('Gimena','Quevedo')
    Carga_directa('Rodrigo','Pernuzzi')
    Carga_directa('Daniel','Rodriguez')
    Carga_directa('Rodrigo','Guardatti')
    menu()





if __name__ == '__main__':
    main()