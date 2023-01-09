def main():
    def busca_objeto(mochila, numero_obj=0):
        if not mochila:
            return False, numero_obj

        objeto = mochila[0]
        mochila = mochila[1:]

        if objeto == "sable de luz":
            return True, numero_obj

        return busca_objeto(mochila, numero_obj + 1)
        
    mochila = ["Valeria",'ejemplo1',"sable de luz","lapiz","ejemplo2"]
    print(busca_objeto(mochila))

if __name__=="main_":
    main()