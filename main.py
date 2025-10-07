# main.py
from carga_palabras import cargar_palabras_limpias
from wordle_funciones import (
    elegir_palabra,
    comprobar_intento,
    mostrar_feedback,
    validar_intento,
)

def main():
    print("=== PALABRA DEL DÍA ===")
    print("Adivina la palabra secreta de 5 letras.")
    print("Tienes 6 intentos. ¡Suerte!\n")

    # 1️ Cargar palabras válidas desde el archivo
    palabras = cargar_palabras_limpias("palabras_5.txt")

    # 2️ Elegir palabra secreta
    palabra_secreta = elegir_palabra(palabras)

    # (Descomenta para depurar)
    # print(f"[DEBUG] Palabra secreta: {palabra_secreta}")

    intentos_max = 6
    intentos_realizados = 0

    # 3️ Bucle principal del juego
    while intentos_realizados < intentos_max:
        intento = input(f"Intento {intentos_realizados + 1}/{intentos_max}: ").strip().upper()

        # Validar intento
        if not validar_intento(intento, palabras):
            continue

        # Comprobar intento
        resultado = comprobar_intento(palabra_secreta, intento)
        mostrar_feedback(intento, resultado)

        # Comprobar si ha ganado
        if intento == palabra_secreta:
            print(f"\n ¡Felicidades! Has acertado la palabra: {palabra_secreta}")
            break

        intentos_realizados += 1

    else:
        # Se agotan los intentos
        print(f"\n Has agotado los intentos. La palabra era: {palabra_secreta}")

    print("\n ¡Gracias por jugar!")


if __name__ == "__main__":
    main()

