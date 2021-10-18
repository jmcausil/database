
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
    for k, v in ami.items(): 
        print(f"{k}:{v}")


def inicio():
    amigos = cargar()
    imprimir(amigos)

if __name__== "__main__": #inicio del programa 
    inicio()