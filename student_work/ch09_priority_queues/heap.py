class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        indice_hijo=len(self.arreglo)-1
        hijo=self.arreglo[indice_hijo]
        indice_padre= indice_hijo//2
        padre= self.arreglo[indice_padre]
        while hijo < padre:
            self.arreglo[indice_hijo],self.arreglo[indice_padre]= self.arreglo[indice_padre],self.arreglo[indice_hijo]
            indice_hijo=indice_padre
            indice_padre=indice_hijo//2
            hijo=self.arreglo[indice_hijo]
            padre=self.arreglo[indice_hijo]

    def remove_smallest(self):
        if len(self.arreglo) == 1:
            return None

        minimo = self.arreglo[1]             

        ultimo = self.arreglo.pop()         
        if len(self.arreglo) > 1:             
            self.arreglo[1] = ultimo       

            indice_padre = 1
            while True:
                hijo_izq = indice_padre * 2
                hijo_der = indice_padre * 2 + 1
                mas_chico = indice_padre

                if hijo_izq < len(self.arreglo) and self.arreglo[hijo_izq] < self.arreglo[mas_chico]:
                    mas_chico = hijo_izq
                if hijo_der < len(self.arreglo) and self.arreglo[hijo_der] < self.arreglo[mas_chico]:
                    mas_chico = hijo_der

                if mas_chico == indice_padre: 
                    break

                self.arreglo[indice_padre], self.arreglo[mas_chico] = self.arreglo[mas_chico], self.arreglo[indice_padre]
                indice_padre = mas_chico

        return minimo

    def build_heap(self, lista):
        """Construye el heap a partir de una lista, usando downheap desde el final hacia el principio."""
        self.arreglo = [float('-inf')] + list(lista)

        ultimo_padre = (len(self.arreglo) - 1) // 2

        for indice_padre in range(ultimo_padre, 0, -1):
            actual = indice_padre
            while True:
                hijo_izq = actual * 2
                hijo_der = actual * 2 + 1
                mas_chico = actual

                if hijo_izq < len(self.arreglo) and self.arreglo[hijo_izq] < self.arreglo[mas_chico]:
                    mas_chico = hijo_izq
                if hijo_der < len(self.arreglo) and self.arreglo[hijo_der] < self.arreglo[mas_chico]:
                    mas_chico = hijo_der

                if mas_chico == actual:
                    break

                self.arreglo[actual], self.arreglo[mas_chico] = self.arreglo[mas_chico], self.arreglo[actual]
                actual = mas_chico
