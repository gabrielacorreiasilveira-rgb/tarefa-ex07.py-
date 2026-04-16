#ex 17 - Login Simples
usuario = input("Usuário: ")
senha = input ("Sistema: ")

if usuario == "admin" and senha == "123":
    print("Login Realizado")
else:
    print("Usuário ou senha incorretos")