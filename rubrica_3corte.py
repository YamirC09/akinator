class Nodo:
    def __init__(self, dato, respuesta):
        self.respuesta = respuesta
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, dato, respuesta):
        self.raiz = Nodo(dato, respuesta)


    def __agregar(self, nodo:Nodo, nuevo_valor:str, respuesta:bool):
        if respuesta == False:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(nuevo_valor,respuesta)
            else:
                self.__agregar(nodo.izquierda, nuevo_valor, respuesta)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(nuevo_valor, respuesta)
            else:
                self.__agregar(nodo.derecha, nuevo_valor, respuesta)

    def agregar(self, nuevo_valor:str,respuesta:bool):
        nodo_nuevo = self.__agregar(self.raiz, nuevo_valor, respuesta)
        return nodo_nuevo

    def __inorden(self, nodo:Nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.__inorden(nodo.derecha)

    def inorden(self):
        self.__inorden(self.raiz)

    def __buscar(self, nodo, valor):
        if nodo is None:
            return None
        if nodo.dato == valor:
            return nodo

        if valor < nodo.dato:
            return self.__buscar(nodo.izquierda, valor)
        else:
            return self.__buscar(nodo.derecha, valor)

    def buscar(self, valor):
        nodoTMP = self.__buscar(self.raiz, valor)
        return nodoTMP


class JuegoAdivinanza:
    def __init__(self):
        self.arbol_animales = Arbol("Pajaro",True)
        self.arbol_personaje = Arbol("Messi",True)
        self.arbol_flores = Arbol("Orquidea",True)

    def obtenerCategoria(self):
        print("Juguemos a adivinar")
        print("1. Animales")
        print("2. Personajes")
        print("3. Flores")
        opcion = input("Elige una categoría (1-3): ")

        if opcion == "1":
            categoria = "Animales"
            arbol_actual = self.arbol_animales
        elif opcion == "2":
            categoria = "Personajes"
            arbol_actual = self.arbol_personaje
        elif opcion == "3":
            categoria = "Flores"
            arbol_actual = self.arbol_flores
        else:
            print("Opción inválida. Por favor, elige una categoría válida.")
            # Devolver None para indicar que no se ha seleccionado una categoría válida
            return None, None

        return categoria, arbol_actual

    def jugar(self):
        print("Bienvenido al juego de adivinanzas")
        vuelta = 1
        while True:
            if vuelta == 1:
                categoria, arbol_actual = self.obtenerCategoria()

                print("Juguemos a adivinar", categoria)
                vuelta = 2
                

            nodo_actual = arbol_actual.raiz
            
            while nodo_actual.izquierda is not None and nodo_actual.derecha is not None:
                respuesta = input("¿" + nodo_actual.dato + "? (si/no): ")
                if respuesta.lower() == "si":
                    nodo_actual = nodo_actual.derecha
                else:
                    nodo_actual = nodo_actual.izquierda
            
            print("Ya sé, es", nodo_actual.dato,)
            respuesta = input()
            if respuesta.lower() == "si":
                print("¡He adivinado!")
            else:
                print("¿Cuál es tu " + categoria[:-1] + "?: ")
                nuevo_elemento = input()
                print("Qué diferencia a " + nuevo_elemento + " de " + nodo_actual.dato + ": ")
                diferencia = input()
                print("Para " + nuevo_elemento + " la respuesta es si/no?: ")
                respuesta = input()
                if respuesta.lower() == "si":
                    nodo_actual.izquierda = Nodo(nodo_actual.dato,False)
                    nodo_actual.dato = diferencia
                    nodo_actual.derecha = Nodo(nuevo_elemento,True)
                else:
                    nodo_actual.derecha = Nodo(nodo_actual.dato,True)
                    nodo_actual.dato = diferencia
                    nodo_actual.derecha = Nodo(nuevo_elemento,True)


            print("¿Jugamos otra vez? (si/no): ")
            jugar_nuevamente = input()
            if jugar_nuevamente.lower() != "si":
                break

    


juego = JuegoAdivinanza()
juego.jugar()