class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        # el -inf de la posición 0 frena la subida en la raíz
        while self.arreglo[i // 2] > self.arreglo[i]:
            self.arreglo[i // 2], self.arreglo[i] = self.arreglo[i], self.arreglo[i // 2]
            i //= 2
        if imagen:
            self._mostrar()

    def remove_smallest(self, imagen=False):
        minimo = None
        if len(self.arreglo) > 1:
            minimo = self.arreglo[1]
            ultimo = self.arreglo.pop()
            if len(self.arreglo) > 1:
                self.arreglo[1] = ultimo
                self._bajar(1)
        if imagen:
            self._mostrar()
        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range(len(lista) // 2, 0, -1):
            self._bajar(i)
        if imagen:
            self._mostrar()


    def _bajar(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            hijo = 2 * i
            if hijo + 1 <= n and self.arreglo[hijo + 1] < self.arreglo[hijo]:
                hijo += 1
            if self.arreglo[hijo] < self.arreglo[i]:
                self.arreglo[hijo], self.arreglo[i] = self.arreglo[i], self.arreglo[hijo]
                i = hijo
            else:
                break

    def _mostrar(self):
        import matplotlib.pyplot as plt

        n = len(self.arreglo) - 1
        if n == 0:
            print("El heap está vacío")
            return

        niveles = n.bit_length()
        fig, ax = plt.subplots(figsize=(max(4, 0.7 * 2 ** (niveles - 1)), 1.3 * niveles))

        pos = {}
        for i in range(1, n + 1):
            nivel = i.bit_length() - 1
            k = i - 2 ** nivel
            pos[i] = ((k + 0.5) / 2 ** nivel, -nivel)

        for i in range(2, n + 1):
            x1, y1 = pos[i // 2]
            x2, y2 = pos[i]
            ax.plot([x1, x2], [y1, y2], color='black', zorder=1)

        for i in range(1, n + 1):
            x, y = pos[i]
            ax.text(x, y, str(self.arreglo[i]), ha='center', va='center',
                    bbox=dict(boxstyle='circle', fc='lightblue', ec='black'), zorder=2)

        ax.set_xlim(0, 1)
        ax.set_ylim(-niveles + 0.5, 0.5)
        ax.axis('off')
        plt.show()


if __name__ == "__main__":
    H = Heap()
    H.insert(10)
    H.insert(4)
    H.insert(7)
    print(H.arreglo)        # [-inf, 4, 10, 7]
    H.remove_smallest()
    print(H.arreglo)        # [-inf, 7, 10]
    H.build_heap(list(range(31, 0, -1)))
    print(H.arreglo)
