import re


def añadir_correo(nombre,correo):
        #contador=0

        if correo=="" or correo is None:
            print("es una entrada incorrecta")
            correo=input("introduce un correo electronico: ")
            añadir_correo(nombre,correo)

        elif re.search(".*@.*\..*", correo)==None:
            correo=input("correo electronico debe tener formato xxx@xxx.xx: ")
            añadir_correo(nombre,correo)

        else:
            for i in range(len(correo)):
                    if correo[i]=="@":
                        if correo[:i]!=nombre:
                            print("cuenta bloqueada por alerta de un ataque")
                        else:
                            print(f'Bienvenido {correo[:i]}')

añadir_correo("dani","dani")



def añadir_correo2(nombre,correo):


    if re.search(".*@.*\..*", correo)==None:
        raise email_mal_formateado

    elif correo is None or correo=="":
        raise entrada_incorrecta

    elif re.search(".*@.*\..*", correo)!=None:
        for i in range(len(correo)):
                if correo[i]=="@":
                    if correo[:i]!=nombre:
                        raise ciberataque
                    else:
                        print(f'Bienvenido {correo[:i]}')

nombre=input("nombre: ")
correo=input("correo:")

class entrada_incorrecta(BaseException):

    try:
        if correo=="" or correo is None:
            print("es una entrada incorrecta")
            correo=input("introduce un correo electronico: ")
    finally:
        pass



class email_mal_formateado(BaseException):
    try:
        if re.search(".*@.*\..*",correo)!=None:
            pass
    finally:
        correo=input("correo electronico debe tener formato xxx@xxx.xx: ")



class ciberataque(BaseException):
    try:
        if re.search(".*@.*\..*",correo)==None:
            pass
    finally:
        print("cuenta bloqueada por alertar de un ataque")


añadir_correo(nombre,correo)
