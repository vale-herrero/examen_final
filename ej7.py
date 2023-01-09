
def main():
    frecuencias= {'A': 0.2, 'F': 0.17, '1': 0.13, '3': 0.21, '0': 0.05, 'M': 0.09, 'T': 0.15}

    frecuencias_ordenadas=sorted(frecuencias.items(), key=lambda x: x[1], reverse=False)

    class nodoArbol():
        def __init__(self, izq=None, der=None):
            self.izq= izq
            self.der=der
        
        def children(self):
            return self.izq, self.der
        
    def crear_arbol(frecuencias_ordenadas_dict):
        frecuencias_ordenadas_lista= list(frecuencias_ordenadas_dict)
        print(frecuencias_ordenadas_lista)
        while len(frecuencias_ordenadas_lista) > 1:
            let1, freq1 =frecuencias_ordenadas_lista[0]
            let2, freq2 =frecuencias_ordenadas_lista[1]
            nodo=nodoArbol(let1, let2)
            frecuencias_ordenadas_lista.append((nodo, freq1+freq2))
            frecuencias_ordenadas_lista= sorted(frecuencias_ordenadas_lista, key=lambda x: x[1], reverse=False)
            frecuencias_ordenadas_lista= frecuencias_ordenadas_lista[2:]
            print(frecuencias_ordenadas_lista)
        return frecuencias_ordenadas_lista[0]

    arbol= crear_arbol(frecuencias_ordenadas)

    def huffman_tabla_codificacion(arbol, codigo=''):
        if type(arbol) is str:
            return {arbol: codigo}

        izq, der = arbol.children()
        dic_codificacion = dict()
        dic_codificacion.update(huffman_tabla_codificacion(izq, codigo + '0'))
        dic_codificacion.update(huffman_tabla_codificacion(der, codigo + '1'))
        return dic_codificacion

    tabla_codificada= huffman_tabla_codificacion(arbol[0])
    print(tabla_codificada)

    def codificar(cadena, tabla_codif):
        mensaje=''
        for letra in cadena:
            mensaje= mensaje + tabla_codif[letra]
        return mensaje


    def decodificar(mensaje_cod, nodo_raiz, nodo_actual, mensaje_decodificado=''):
        for bit in mensaje_cod:
            if bit == '0':
                nodo_actual= nodo_actual.izq
            else:
                nodo_actual= nodo_actual.der
            if type(nodo_actual) is str:
                mensaje_decodificado= mensaje_decodificado + nodo_actual
                nodo_actual= nodo_raiz
        return mensaje_decodificado

if __name__ == "__main__":
    main()
 