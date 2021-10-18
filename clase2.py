
def cargar():
    amigo ={}
    continua = "s"
    while continua == "s":
        codigo=int(input("ingrese su codigo"))
        nombre = input("ingrese su nombre")
        edad= int("ingrese su edad")
        amigo[codigo]=(nombre, edad)
        # amigo= {codigo, nombre, edad} igual a linea anterior
        continua=input("desea continuar s/n")
        continua=continua.lower()
        print(continua)
    return amigo



def imprimir(ami):  


def main():
    amigos = cargar()
    imprimir(amigos)




if __name__== "__main__": #inicio del programa 
    main()