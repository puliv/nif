import os, random

# personas = [["99999999-MAD", "tulio triviño", 33, "chilena"]]
personas = []
edadPersona = 0


def limpiarTerminal():
    os.system("cls")


def mostrarMenu():
    print("Registro de Ciudadanos de la Unión Europea de España")
    print("1) Grabar persona")
    print("2) Buscar persona")
    print("3) Imprimir Certificados")
    print("4) Salir")


def agregarNombre():
    while True:
        nombreIngresado = input("Ingrese nombre\n").lower()
        while not nombreIngresado:
            nombreIngresado = input("Nombre no puede estar vacio\n")
        if len(nombreIngresado) >= 8:
            return nombreIngresado
        else:
            print("Nombre invalido")


def agregarNIF():
    ciudad = input("Ingrese ciudad donde reside: Madrid, Barcelona o Sevilla\n").lower()
    while ciudad not in ["madrid", "barcelona", "sevilla"]:
        ciudad = input("Ingrese ciudad válida: Madrid, Barcelona o Sevilla\n").lower()
    if ciudad == "madrid":
        sufijo = "MAD"
    elif ciudad == "barcelona":
        sufijo = "BAR"
    elif ciudad == "sevilla":
        sufijo = "SEV"

    # Generando numero aleatorio de 8 digitos para asignar a persona registtrada
    randomNum = random.randint(10000000, 99999999)
    nifPersona = f"{randomNum}-{sufijo}"
    print(nifPersona)

    return nifPersona


def agregarNacionalidad():
    while True:
        nacionalidad = input("Ingrese nacionalidad, ej: chilena\n").lower()
        while not nacionalidad:
            nacionalidad = input(
                "el campo nacionalidad no puede estar vacio, ingrese nacionalidad:\n"
            )
        return nacionalidad


def agregarEdad():
    while True:
        # verificando que edad no venga vacio
        edadS = input("Ingrese edad\n")
        while not edadS:
            edadS = input("ingrese edad válida, no debe estar vacio\n")
        try:
            edadIngresada = int(edadS)
            # confirmando que edad cumpla requisitos
            while edadIngresada >= 15:
                edadPersona = edadIngresada
                return edadIngresada
            else:
                print("Edad debe ser mayor o igual a 15 años")
        except:
            print("Para el campo edad, solo se permiten valores de tipo númerico")


def agregarCumpleaños():
    while True:
        try:
            diaInt = int(input("Ingrese día de nacimiento (1-30): "))
            if 1 < diaInt and diaInt < 30:
                break
            else:
                print("Ingrese un día válido, de 1 a 30.")
        except:
            print("Para el campo día, solo se permiten valores de tipo numérico.")

    while True:
        try:
            mesInt = int(input("Ingrese mes de nacimiento (1-12): "))
            if 1 < mesInt and mesInt < 12:
                break
            else:
                print("Ingrese un mes válido, de 1 a 12.")
        except:
            print("Para el campo mes, solo se permiten valores de tipo numérico.")

    while True:
        try:
            yearInt = int(input("Ingrese año de nacimiento: "))
            # si nace despues del 2009 tiene menos de 15 años
            if yearInt <= 2009:
                break
            else:
                print("Ingrese un año válido.")
        except:
            print("Para el campo año, solo se permiten valores de tipo numérico.")

    cumple = f"{diaInt}/{mesInt}/{yearInt}"
    return cumple


def agregarEstadoCivil():
    while True:
        estadoCivil = input("Ingrese estado civil\n").lower()
        while not estadoCivil:
            estadoCivil = input(
                "el campo estado civil no puede estar vacio, ingrese estado civil:\n"
            )
        return estadoCivil


def agregarSalario():
    return random.randint(500000, 10000000)


def registrarPersona():
    while True:
        nombre = agregarNombre()
        edad = agregarEdad()
        nif = agregarNIF()
        nacionalidad = agregarNacionalidad()
        cumple = agregarCumpleaños()
        estadoCivil = agregarEstadoCivil()
        salario = agregarSalario()
        persona = [
            nif,
            nombre,
            edad,
            nacionalidad,
            cumple,
            estadoCivil,
            salario,
        ]
        personas.append(persona)
        print(personas)
        try:
            opcion = input("Quieres grabar a otra persona? Si o No\n").lower()
            while opcion not in ["si", "no"] or not opcion:
                opcion = input(
                    "Para grabar a otra persona debe seleccionar: Si o No\n"
                ).lower()
            if opcion == "si":
                continue
            else:
                break
        except:
            print("solo se permite 'si' o 'no' para grabar otra persona")


def buscarPersona():
    nifIngresado = input("Ingrese NIF de persona a buscar\n").upper()
    while not nifIngresado:
        nifIngresado = input("Ingrese NIF válido, no puede estar vacio\n").upper()
    while len(nifIngresado.split("-")[0]) != 8:
        nifIngresado = input("Ingrese NIF válido\n").upper()
    if (
        nifIngresado.endswith("-MAD")
        or nifIngresado.endswith("-BAR")
        or nifIngresado.endswith("-SEV")
    ):
        for per in personas:
            if per[0] == nifIngresado:
                print(per)
                input("Presione enter para volver a menu principal")
            else:
                print("NIF no existe en nuestros registros")
                input("Presione enter para volver a menu principal")
    else:
        nifIngresado = input("Ingrese NIF válido\n")


def imprimirCertificado():

    # copie y pegue este codigo por que ya no me quedaba tiempo xd
    nifIngresado = input("Ingrese NIF de persona a buscar\n").upper()
    while not nifIngresado:
        nifIngresado = input("Ingrese NIF válido, no puede estar vacio\n").upper()
    while len(nifIngresado.split("-")[0]) != 8:
        nifIngresado = input("Ingrese NIF válido\n").upper()
    if (
        nifIngresado.endswith("-MAD")
        or nifIngresado.endswith("-BAR")
        or nifIngresado.endswith("-SEV")
    ):
        for per in personas:
            if per[0] == nifIngresado:
                # esta es la verdadera parte del imprimir certificado xd
                print("1) Certificado de nacimiento")
                print("2) Certificado de estado conyugal")
                print("3) Certificado de salario")
                try:
                    opcion = int(input("Ingrese opcion\n"))
                    if opcion == 1:
                        print("Certificado de nacimiento")
                        print(f"NIF: {per[0]}")
                        print(f"Nombre: {per[1]}")
                        print(f"Nacimiento: {per[4]}")
                    elif opcion == 2:
                        print("Certificado de estado conyugal")
                        print(f"NIF: {per[0]}")
                        print(f"Nombre: {per[1]}")
                        print(f"Estado conyugal: {per[5]}")
                    elif opcion == 3:
                        print("Certificado de salario")
                        print(f"NIF: {per[0]}")
                        print(f"Nombre: {per[1]}")
                        print(f"Salario: ${per[4]}")
                    else:
                        print("opcion invalida")
                except:
                    print("Solo se aceptan valores numericos")
            else:
                print("NIF no existe en nuestros registros")
                input("Presione enter para volver a menu principal")
    else:
        nifIngresado = input("Ingrese NIF válido\n")
