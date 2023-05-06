peliculas=["Mario Bross","Godzilla","Rapidos y furiosos, dom vs tanos","Gigantes de acero","Pacific rim"]



def login():
    usuario=input("Ingresa el usuario  ")
    password=input("Ingresa tu contraseña ")
    bandera=False
    if usuario=="usuario1" and password=="pass1":
        bandera=True
    return bandera

def signUp():
    print("Crear")
def menu():
    seleccion=""
    while seleccion!="y":
        seleccion=input("Ya tienes una cuenta? ")
        if seleccion=="n":
            signUp()
            seleccion="y"
        b=login()
        print(b)
menu()
    
    
