acesso = False

senha = " "

entrada = input("Digite sua senha de entrada: ")
#pode conter letras, números e símbolos


if entrada == senha:
   acesso = True
   print("Senha correta.")
else:
   print("errou")

if acesso:
   print("Bem vindo ao sistema!")
