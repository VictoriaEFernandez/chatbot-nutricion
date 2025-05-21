def mostrar_menu():
    opciones = [
        "Información sobre alimentación saludable",
        "Consejos para perder peso",
        "Hablar con nutricionista",
        "Salir"
    ]
    return opciones


def procesar_opcion(opcion):
    if opcion == "1":
        return "La alimentación saludable incluye frutas, verduras, proteínas magras y granos integrales."
    elif opcion == "2":
        return "Para perder peso es importante combinar dieta balanceada y ejercicio regular."

    elif opcion == "3":
        return "Un nutricionista se pondrá en contacto contigo pronto."
    elif opcion == "4":
        return "Salir"
    else:
        return "Opción no válida, por favor intenta de nuevo."


def main():
    print("¡Bienvenido al Chatbot de Nutrición!")

    while True:
        opciones = mostrar_menu()
        print("\nPor favor, selecciona una opción:")
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i}. {opcion}")

        opcion = input("Ingrese el número de la opción: ")
        respuesta = procesar_opcion(opcion)
        if respuesta == "Salir":
            print("Gracias por usar el chatbot. ¡Hasta luego!")
            break
        else:
            print(respuesta)

    def saludo():
        # espacio innecesario entre función y paréntesis (flake8 lo marca)
        return "Hola"


def responder_pregunta(pregunta):
    if "color" in pregunta.lower():
        return "Rojo"  # Cambiaste esto a propósito
    return "No entiendo la pregunta."


if __name__ == "__main__":
    main()
