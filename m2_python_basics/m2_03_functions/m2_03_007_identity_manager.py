import os

os.system("clear")

users = {"admin": ["admin", "admin", "password123"]}


korisnik_admin = users["admin"]
print(korisnik_admin[2])


# def enter_username():
#     username = input("Upisite svoje korisnicko ime: ")
#     while username not in users:
#         print(f"Korisnicko ime '{username}' ne postoji u sustavu, pokusajte ponovno")
#         username = input("Upisite svoje korisnicko ime: ")
#     return username


# def enter_password():
#     password = input("Upisite svoju lozinku (minimalno 10 znakova): ")
#     while len(password) < 10:
#         print("Lozinka je prekratka, mora biti minimalno 10 znakova dugacka")
#         password = input("Upisite svoju lozinku (minimalno 10 znakova): ")
#     return password


# def validate_password(user):
#     user = users[username]
#     counter = 3
#     while counter > 0:
#         password = enter_password()
#         if user[2] == password:
#             print(f"Dobro dosli {user[0]} {user[1]}")
#             return
#         else:
#             print(f"Unijeli ste krivu lozinku! Preostali broj pokusaja: {counter-1}")
#             counter -= 1
#     print("Previse puta upisana kriva lozinka, gasim sustav")
#     exit()


# username = enter_username()
# validate_password(username)
# if username == "admin":
#     pass
