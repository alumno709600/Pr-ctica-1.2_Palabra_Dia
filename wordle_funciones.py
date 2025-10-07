import random

GREEN_BG = "\033[42m"
YELLOW_BG = "\033[43m"
GRAY_BG = "\033[47m"
RESET = "\033[0m"

def colorear_letra(letra: str, estado: str) -> str:
    """Devuelve la letra coloreada según su estado."""
    if estado == "verde":
        return f"{GREEN_BG} {letra.upper()} {RESET}"
    elif estado == "amarillo":
        return f"{YELLOW_BG} {letra.upper()} {RESET}"
    else:
        return f"{GRAY_BG} {letra.upper()} {RESET}"


def elegir_palabra(palabras: list[str]) -> str:
    """
    Selecciona aleatoriamente la palabra del día de la lista de palabras.
    """
    return random.choice(palabras)


def comprobar_intento(palabra_secreta: str, intento: str) -> list[str]:
    """
    Compara el intento con la palabra secreta y devuelve una lista indicando
    para cada letra si es:
        - "verde" -> letra correcta y en la posición correcta
        - "amarillo" -> letra presente en otra posición
        - "gris" -> letra no presente
    """
    palabra_secreta = palabra_secreta.upper()
    intento = intento.upper()

    resultado = ["gris"] * len(intento)
    letras_restantes = list(palabra_secreta)

    # Primero marcamos los verdes
    for i in range(len(intento)):
        if intento[i] == palabra_secreta[i]:
            resultado[i] = "verde"
            letras_restantes[i] = None  # quitamos la letra usada

    # Luego marcamos los amarillos
    for i in range(len(intento)):
        if resultado[i] == "gris" and intento[i] in letras_restantes:
            resultado[i] = "amarillo"
            letras_restantes[letras_restantes.index(intento[i])] = None

    return resultado


def mostrar_feedback(intento: str, resultado: list[str]) -> None:
    """
    Muestra el intento en la consola con feedback de colores.
    """
    colores = [colorear_letra(letra, estado) for letra, estado in zip(intento, resultado)]
    print("".join(colores))


def validar_intento(intento: str, palabras: list[str]) -> bool:
    """
    Valida que el intento:
      - tenga 5 letras
      - esté en la lista de palabras cargadas
    """
    intento = intento.strip().upper()
    if len(intento) != 5:
        print("Error: la palabra debe tener 5 letras.")
        return False
    if intento not in palabras:
        print("Error: la palabra no está en la lista de palabras válidas.")
        return False
    return True


# Ejemplo de prueba manual
if __name__ == "__main__":
    palabra = "carta"
    intento = "inten"

    resultado = comprobar_intento(palabra, intento)
    mostrar_feedback(intento, resultado)



