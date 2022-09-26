import os
import pickle

class Vehículo:
    Color = ""
    _Ruedas = 0
    _Puertas = 0

    def __init__(self,Color,Ruedas,Puertas):
        self.Color = Color
        self._Ruedas = Ruedas
        self._Puertas = Puertas

    def __str__(self):
        return f'''El coche es de color {self.Color}, tiene {self._Ruedas} ruedas y {self._Puertas} puertas.'''

class Coche(Vehículo):
    _Velocidad = 0
    _Cilindrada = 0

    def __init__(self,Vel,Cc):
        super().__init__("Rojo",4,5)
        self._Velocidad = Vel
        self._Cilindrada = Cc

    def __str__(self):
        return f'''El coche es de color {self.Color}, tiene {self._Ruedas} ruedas y {self._Puertas} puertas.
Además alcanza una velocidad de {self._Velocidad} en autopista (legalmente). El motor es de {self._Cilindrada} cc'''

class lista_Vehiculos:
    lista=[]

    def __init__(self):
        f = open('ext_file.dat', 'ab+')
        f.seek(0)

        try:
            self.lista=pickle.load(f)
            print(f'Se cargaron {len(self.lista)} vehículos del fichero externo')
        except:
            print('El fichero está vacío!')
        finally:
            f.close()
            del(f)
    
    def save_changes(self):
        f = open('ext_file.dat', 'wb+')
        pickle.dump(self.lista,f)
        f.close()
        del(f)

    def add(self,vehiculo):
        self.lista.append(vehiculo)
        self.save_changes()

    def listar_vehículos(self):
        print('La información del fichero externo es la siguiente:')
        print()
        for vehiculo in self.lista:
            print(vehiculo)


Lista_V=lista_Vehiculos()

#c = Coche(130,2000)
#Lista_V.add(c)
Lista_V.listar_vehículos()