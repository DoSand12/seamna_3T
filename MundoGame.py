import math
import random



print ("____________Ciruclo____________")
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def AreaCirculo(self):
        return math.pi * self.radio**2

    def PerimetroCirculo(self):
        return 2 * math.pi * self.radio

    def ElegirRadio(self, nuevo_radio):
        self.radio = nuevo_radio

circuloCal = Circulo(6)

areaCir = circuloCal.AreaCirculo()
print(f"El area del circulo es: {areaCir}")

perimetroCir = circuloCal.PerimetroCirculo()
print(f"El perimetro del circulo es: {perimetroCir}")

print ("----------------------------------------------")

print ("____________Rectangulo____________")
class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def AreaRectangulo(self):
        return self.longitud * self.ancho

    def PerimetroRectangulo(self):
        return 2 * (self.longitud + self.ancho)


    def LongitudRectangulo(self, nueva_longitud):
        self.longitud = nueva_longitud

    def AnchoRectatangulo(self, nuevo_ancho):
        self.ancho = nuevo_ancho

rectanguloCal = Rectangulo(5, 3)


arearec = rectanguloCal.AreaRectangulo()
print(f"El area del rectangulo es: {arearec}")


perimetrorec = rectanguloCal.PerimetroRectangulo()
print(f"El perimetro del rectangulo es: {perimetrorec}")









print ("______________________Caciones_____________________________")










class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []                                      # cinseramente no C como poder guardar lo solicitado si no es atrabes de una lista que las pueda almacenar
        self.estado = "Pausado"
        self.indice_actual = -1

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def eliminar_cancion(self, cancion):
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            if self.indice_actual >= len(self.canciones):
                self.indice_actual = -1

    def mostrar_canciones(self):
        print("Canciones en la lista de reproduccion actual:")
        for i, cancion in enumerate(self.canciones):
            print(f"{i + 1}. {cancion}")

    def reproducir(self):
        if self.estado == "Pausado" and self.canciones:
            self.estado = "reproduciendo"
            self.indice_actual = 0
            print(f"Reproduciendo: {self.canciones[self.indice_actual]}")

    def seleccionar_cancion(self, indice):
        if 0 <= indice < len(self.canciones):
            self.indice_actual = indice
            self.estado = "reproduciendo"
            print(f"Reproduciendo: {self.canciones[self.indice_actual]}")

    def pausar(self):
        if self.estado == "reproduciendo":
            self.estado = "pausa"
            print("Pausa")

    def detener(self):
        if self.estado != "Pausado":
            self.estado = "Pausado"
            print("La cacion esta Pausada")

    def siguiente_cancion(self):
        if self.estado == "reproduciendo" and self.indice_actual < len(self.canciones) - 1:
            self.indice_actual += 1
            print(f"Reproduciendo siguiente: {self.canciones[self.indice_actual]}")

    def cancion_anterior(self):
        if self.estado == "reproduciendo" and self.indice_actual > 0:
            self.indice_actual -= 1
            print(f"Reproduciendo anterior: {self.canciones[self.indice_actual]}")

    def canciones_aleatorio(self):
        if self.estado != "reproduciendo" and self.canciones:
            indice_aleatorio = random.randint(0, len(self.canciones) - 1)
            while indice_aleatorio == self.indice_actual:
                indice_aleatorio = random.randint(0, len(self.canciones) - 1)
            self.indice_actual = indice_aleatorio
            self.estado = "reproduciendo"
            print(f"Reproduciendo de manera aleatoria: {self.canciones[self.indice_actual]}")

    def ver_estado(self):
        print(f"Estado: {self.estado}")

    def ver_cancion_actual(self):
        if self.indice_actual != -1:
            print(f"Canción actual: {self.canciones[self.indice_actual]}")
        else:
            print("No hay nada en la lista de reproduccion actualmente")

mi_playlist = Playlist("Mi Lista de Reproduccion")

while True:
    print("\n----- Menu de Playlist -----")
    print("1. Agregar una Cancion")
    print("2. Eliminar una Cancion")
    print("3. Mostrar una Canciones")
    print("4. Reproducir una cancion")
    print("5. Seleccionar Cancion")
    print("6. Pausar")
    print("7. Detener reproduccion")
    print("8. Siguiente Cancion")
    print("9. Cancion Anterior")
    print("10. Reproducir de manera Aleatoria")
    print("11. Ver Estado")
    print("12. Ver Cancion Actual")
    print("13. Salir")

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        cancion = input("Ingrese el nombre de la cancion que quiere agregar: ")
        mi_playlist.agregar_cancion(cancion)
    elif opcion == 2:
        cancion = input("Ingrese el nombre de la cancion por eliminar: ")
        mi_playlist.eliminar_cancion(cancion)
    elif opcion == 3:
        mi_playlist.mostrar_canciones()
    elif opcion == 4:
        mi_playlist.reproducir()
    elif opcion == 5:
        indice = int(input("Ingrese el indice de la canción a seleccionar: "))
        mi_playlist.seleccionar_cancion(indice - 1)
    elif opcion == 6:
        mi_playlist.pausar()
    elif opcion == 7:
        mi_playlist.detener()
    elif opcion == 8:
        mi_playlist.siguiente_cancion()
    elif opcion == 9:
        mi_playlist.cancion_anterior()
    elif opcion == 10:
        mi_playlist.reproducir_aleatorio()
    elif opcion == 11:
        mi_playlist.ver_estado()
    elif opcion == 12:
        mi_playlist.ver_cancion_actual()
    elif opcion == 13:
        print("Operaciones terminadas esta la proxima")
        break





