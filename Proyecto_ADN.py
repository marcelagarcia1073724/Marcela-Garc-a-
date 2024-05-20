def registrar_sujeto(sujetos):
    nombre = input("Ingrese el nombre completo del sujeto de prueba (apellido incluido): ")
    if len(nombre.split()) < 2:
        print("El nombre debe contener al menos un nombre y un apellido.")
        return
    sujetos[nombre] = ""  # Agregar el sujeto al diccionario de sujetos con cadena de ADN vacía
    print(f"Sujeto {nombre} registrado correctamente.")

def ingresar_cadena_adn(sujetos):
    nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
    if nombre not in sujetos:
        print("El sujeto de prueba no está registrado.")
        return
    cadena_adn = input("Ingrese la cadena de ADN del sujeto de prueba: ")
    if len(cadena_adn) < 13 or not cadena_adn.replace('A', '').replace('C', '').replace('G', '').replace('T', ''):
        print("La cadena de ADN debe tener al menos 13 caracteres y contener solo bases A, C, G, T.")
        return
    sujetos[nombre] = cadena_adn
    print(f"Cadena de ADN del sujeto {nombre} registrada correctamente.")

def contenido_gc(cadena_adn):
    total_bases = len(cadena_adn)
    gc_count = cadena_adn.count('G') + cadena_adn.count('C')
    if total_bases == 0:
        return 0
    return (gc_count / total_bases) * 100

def resumen_secuencia_adn(sujetos):
    nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
    if nombre not in sujetos:
        print("El sujeto de prueba no está registrado.")
        return
    cadena_adn = sujetos[nombre]
    bases_count = {base: cadena_adn.count(base) / len(cadena_adn) * 100 for base in 'ACGT'}
    print(f"Resumen de secuencia de ADN para {nombre}:")
    for base, percentage in bases_count.items():
        print(f"{base} = {percentage:.2f}%")

def secuencia_mas_larga(sujetos):
    nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
    if nombre not in sujetos:
        print("El sujeto de prueba no está registrado.")
        return
    cadena_adn = sujetos[nombre]
    if not cadena_adn:
        print("La cadena de ADN del sujeto está vacía.")
        return
    max_length = 0
    max_sequence = ""
    current_length = 1
    current_sequence = cadena_adn[0]
    for i in range(1, len(cadena_adn)):
        if cadena_adn[i] == cadena_adn[i - 1]:
            current_length += 1
            current_sequence += cadena_adn[i]
        else:
            if current_length > max_length:
                max_length = current_length
                max_sequence = current_sequence
            current_length = 1
            current_sequence = cadena_adn[i]
    if current_length > max_length:
        max_length = current_length
        max_sequence = current_sequence
    start_index = cadena_adn.find(max_sequence)
    print(f"Secuencia más larga para {nombre}: {max_sequence}, posición: {start_index}")

    nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
    if nombre not in sujetos:
        print("El sujeto de prueba no está registrado.")
        return
    cadena_adn = sujetos[nombre]
    max_length = 0
    max_sequence = ""
    current_length = 1
    current_sequence = cadena_adn[0]
    for i in range(1, len(cadena_adn)):
        if cadena_adn[i] == cadena_adn[i - 1]:
            current_length += 1
            current_sequence += cadena_adn[i]
        else:
            if current_length > max_length:
                max_length = current_length
                max_sequence = current_sequence
            current_length = 1
            current_sequence = cadena_adn[i]
    if current_length > max_length:
        max_length = current_length
        max_sequence = current_sequence
    start_index = cadena_adn.find(max_sequence)
    print(f"Secuencia más larga para {nombre}: {max_sequence}, posición: {start_index}")

def porcentaje_similitud(sujetos):
    nombre1 = input("Ingrese el nombre completo del primer sujeto de prueba: ")
    nombre2 = input("Ingrese el nombre completo del segundo sujeto de prueba: ")
    if nombre1 not in sujetos or nombre2 not in sujetos:
        print("Al menos uno de los sujetos de prueba no está registrado.")
        return
    cadena_adn1 = sujetos[nombre1]
    cadena_adn2 = sujetos[nombre2]
    total_bases = len(cadena_adn1)
    coincidencias = sum(1 for base1, base2 in zip(cadena_adn1, cadena_adn2) if base1 == base2)
    porcentaje = (coincidencias / total_bases) * 100
    print(f"Porcentaje de similitud entre {nombre1} y {nombre2}: {porcentaje:.2f}%")
    if porcentaje == 100:
        print("Tienen una relación muy cercana (posiblemente la misma persona).")
    elif porcentaje >= 92.5:
        print("Probablemente son padres/hijos.")
    elif porcentaje >= 75:
        print("Podrían ser abuelos/nietos, tíos/tías, sobrinos/sobrinas, o medio hermanos.")
    elif porcentaje >= 37.5:
        print("Podrían ser primos hermanos, bisabuelos/bisnietos, tíos/tías abuelos(as), sobrinos(as) abuelos(as), medio tíos/tías, medio sobrinos(as).")
    else:
        print("No se encontraron similitudes significativas, no hay una relación clara.")

def resumen_sujetos(sujetos):
    print("Resumen de sujetos de prueba:")
    for nombre, cadena_adn in sujetos.items():
        print(f"Nombre: {nombre}, Cadena de ADN: {cadena_adn}")

def main():
    sujetos = {}
    while True:
        print("\nMenú:")
        print("1. Registrar sujeto de prueba")
        print("2. Ingresar cadena de ADN")
        print("3. Calcular contenido de GC")
        print("4. Generar resumen de secuencia de ADN")
        print("5. Encontrar secuencia más larga")
        print("6. Calcular porcentaje de similitud")
        print("7. Mostrar resumen de sujetos de prueba")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_sujeto(sujetos)
        elif opcion == '2':
            ingresar_cadena_adn(sujetos)
        elif opcion == '3':
            nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
            if nombre in sujetos:
                gc = contenido_gc(sujetos[nombre])
                print(f"Contenido de GC para {nombre}: {gc:.2f}%")
            else:
                print("El sujeto de prueba no está registrado.")
        elif opcion == '4':
            resumen_secuencia_adn(sujetos)
        elif opcion == '5':
            secuencia_mas_larga(sujetos)
        elif opcion == '6':
            porcentaje_similitud(sujetos)
        elif opcion == '7':
            resumen_sujetos(sujetos)
        elif opcion == '8':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
