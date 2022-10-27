#sistema de loguin e senha usando if  e else


print("bem vido a sistema, faça loguin para continuar")


a = str(input("loguin:  "))
b = int(input("Senha:   "))

if a == "python" and b ==123:
    print("logado com sucesso")
else:
    print("usuario invalido")
