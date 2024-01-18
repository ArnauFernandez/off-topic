
def retirar():
    cuenta = 5000
    cantRetrio=int(input("indique la cantidad a retirar: ")
    if cantRetrio>cuenta:
        print("error usted quiere retirar una cantidad superior a la que dispone en cuenta")
    else:
        cuenta = cuenta + cantRetrio