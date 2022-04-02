import re
"""x=input("introduce tu correo electronico ")
contador=0
if re.search(".*@.*\..*", x)==None and contador<2:
    contador+=1
    print("es una entrada incorrecta")
    x=input("introduce un correo electronico ")
elif re.search(".*@.*\..*", x)==None and contador==1:
    x=input("correo electronico debe tener formato xxx@xxx.xx")
    contador+=1
elif re.search(".*@.*\..*", x)==None and contador>=2:
    print("cuenta bloqueada a causa de un ataque")
else:
    for i in range(len(x)):
        if x[i]=="@":
            print(f'Bienvenido {x[:i]}')"""

class mail:
    def añadir_correo(nombre,correo):
        contador=0

        if re.search(".*@.*\..*", correo)==None:
            print("es una entrada incorrecta")
            correo=input("introduce un correo electronico: ")
            while re.search(".*@.*\..*", correo)==None:
                correo=input("correo electronico debe tener formato xxx@xxx.xx: ")
                contador+=1
                if contador==5:
                    print("cuenta bloqueada por alerta de un ataque")
                    break

            else:
                for i in range(len(correo)):
                    if correo[i]=="@":
                        if correo[:i]!=nombre:
                            print("cuenta bloqueada por alertar de un ataque")
                        else:
                            print(f'Bienvenido {correo[:i]}')
        else:
            for i in range(len(correo)):
                    if correo[i]=="@":
                        if correo[:i]!=nombre:
                            print("cuenta bloqueada por alertar de un ataque")
                        else:
                            print(f'Bienvenido {correo[:i]}')

mail.añadir_correo("dani","dani")