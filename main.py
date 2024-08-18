import secrets
import string

def generar_contraseña(longitud):
    """
    Genera una contraseña segura de la longitud especificada.
    
    Args:
        longitud (int): La longitud deseada para la contraseña.
        
    Returns:
        str: Contraseña generada de longitud 'longitud'.
    """
    # Definir el conjunto de caracteres permitidos (letras, dígitos y puntuación)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar una contraseña segura eligiendo aleatoriamente caracteres del conjunto
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    return contraseña

if __name__ == "__main__":
    while True:
        try:
            nombreAplicacion = """

######     ###     #####    #####   ##   ##   #####   ######   #####              #####   #######  ##   ##  #######  ######     ###     # #####  #####   ######   
 ##  ##   ## ##   ##   ##  ##   ##  ##   ##  ### ###   ##  ##   ## ##            ##   ##   ##   #  ###  ##   ##   #   ##  ##   ## ##   ## ## ## ### ###   ##  ##  
 ##  ##  ##   ##  ##       ##       ##   ##  ##   ##   ##  ##   ##  ##           ##        ##      #### ##   ##       ##  ##  ##   ##     ##    ##   ##   ##  ##  
 #####   ##   ##   #####    #####   ## # ##  ##   ##   #####    ##  ##           ## ####   ####    #######   ####     #####   ##   ##     ##    ##   ##   #####   
 ##      #######       ##       ##  #######  ##   ##   ## ##    ##  ##           ##   ##   ##      ## ####   ##       ## ##   #######     ##    ##   ##   ## ##   
 ##      ##   ##  ##   ##  ##   ##  ### ###  ### ###   ## ##    ## ##            ##   ##   ##   #  ##  ###   ##   #   ## ##   ##   ##     ##    ### ###   ## ##   
####     ##   ##   #####    #####   ##   ##   #####   #### ##  #####              #####   #######  ##   ##  #######  #### ##  ##   ##    ####    #####   #### ##  
                                                                                                                                                                  

"""
            print(nombreAplicacion)
            # Solicitar al usuario la longitud de la contraseña
            longitud = int(input("Introduce la longitud de la contraseña: "))
            
            # Verificar que la longitud sea un número positivo
            if longitud < 1:
                raise ValueError("La longitud debe ser un número positivo.")
        except ValueError as e:
            # Mostrar mensaje de error y volver a solicitar la longitud
            print(e)
            continue
        
        # Generar una contraseña segura
        while True:
            contraseña_segura = generar_contraseña(longitud)
            print(f"Contraseña segura generada: {contraseña_segura}")
            
            # Preguntar al usuario si está satisfecho con la contraseña
            satisfecho = input("¿Está satisfecho con la contraseña? (y/n): ").strip().lower()
            if satisfecho == 'y':
                print("\n¡Gracias por usar el generador de contraseñas!\n")
                break
            elif satisfecho == 'n':
                print("Vamos a generar una nueva contraseña...")
                break
            else:
                print("Entrada no válida, por favor ingrese 'y' o 'n'.")
        
        # Salir del bucle principal si el usuario está satisfecho
        if satisfecho == 'y':
            break