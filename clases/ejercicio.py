import re

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



class mail_2:
    def añadir_correo(nombre,correo):


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


class entrada_incorrecta(BaseException,mail_2):
    try:
        re.search(".*@.*\..*", mail_2.correo)!=None
    except:
        print("es una entrada incorrecta")
        mail_2.correo=input("introduce un correo electronico: ")


class email_mal_formateado(BaseException,mail_2):
    try:
        re.search(".*@.*\..*", mail_2.correo)!=None
    except:
        mail_2.correo=input("correo electronico debe tener formato xxx@xxx.xx: ")



class ciberataque(BaseException,mail_2):
    try:
        re.search(".*@.*\..*",mail_2.correo)==None
    except:
        print("cuenta bloqueada por alertar de un ataque")


mail_2.añadir_correo("javi","j")