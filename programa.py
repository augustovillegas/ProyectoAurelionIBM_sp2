# Proyecto Aurelion - Menú interactivo de documentación
"""
Este programa de consola permite navegar de forma interactiva
por la documentación completa del Proyecto Aurelion.

La documentación se encuentra en el archivo:
    DOCUMENTACION.md

El programa lee ese archivo y lo divide en secciones lógicas:
- Visión general del proyecto
- Sprint 1 (Demo 1 – asincrónica)
- Sprint 2 (Demo 2 – sincrónica)

De esta manera, cualquier actualización en DOCUMENTACION.md
se verá reflejada automáticamente en el menú.
"""

import os

RUTA_DOC = "DOCUMENTACION.md"


def cargar_documentacion(ruta: str) -> str:
    """Lee el archivo de documentación completo y lo devuelve como string."""
    if not os.path.exists(ruta):
        print(f"\n[ERROR] No se encontró el archivo '{ruta}'.")
        print("Asegúrate de que DOCUMENTACION.md esté en la misma carpeta que programa.py\n")
        return ""
    with open(ruta, "r", encoding="utf-8") as f:
        return f.read()


def dividir_secciones(md: str) -> dict:
    """
    Divide la documentación en secciones usando los encabezados principales.
    Se basa en los títulos tal como están definidos en DOCUMENTACION.md:
    - '## 1. Visión general del proyecto'
    - '## 2. Sprint 1 (Demo 1 – asincrónica)'
    - '## 3. Sprint 2 (Demo 2 – sincrónica)'
    """
    secciones = {
        "completa": md.strip()
    }

    if not md:
        return secciones

    # Buscar los índices de los encabezados
    idx_s1 = md.find("## 2. Sprint 1")
    idx_s2 = md.find("## 3. Sprint 2")

    # Visión general: desde el inicio hasta justo antes del Sprint 1
    if idx_s1 != -1:
        secciones["vision"] = md[:idx_s1].strip()
    else:
        secciones["vision"] = md.strip()

    # Sprint 1: desde su encabezado hasta justo antes del Sprint 2
    if idx_s1 != -1 and idx_s2 != -1:
        secciones["sprint1"] = md[idx_s1:idx_s2].strip()
    elif idx_s1 != -1:
        secciones["sprint1"] = md[idx_s1:].strip()
    else:
        secciones["sprint1"] = "No se pudo identificar claramente la sección de Sprint 1 en el archivo."

    # Sprint 2: desde su encabezado hasta el final
    if idx_s2 != -1:
        secciones["sprint2"] = md[idx_s2:].strip()
    else:
        secciones["sprint2"] = "No se pudo identificar claramente la sección de Sprint 2 en el archivo."

    return secciones


def mostrar_menu():
    print("\n===== MENÚ DOCUMENTACIÓN AURELION =====")
    print("1. Ver documentación COMPLETA")
    print("2. Ver VISIÓN GENERAL del proyecto")
    print("3. Ver SPRINT 1 (Demo 1 – asincrónica)")
    print("4. Ver SPRINT 2 (Demo 2 – sincrónica)")
    print("8. Recargar DOCUMENTACION.md")
    print("9. Salir")


def mostrar_seccion(titulo: str, contenido: str):
    print("\n" + "=" * 80)
    print(f"{titulo}")
    print("=" * 80 + "\n")
    print(contenido)
    print("\n" + "=" * 80 + "\n")


def main():
    md = cargar_documentacion(RUTA_DOC)
    secciones = dividir_secciones(md)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if not opcion.isdigit():
            print("Por favor, ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            mostrar_seccion("DOCUMENTACIÓN COMPLETA", secciones.get("completa", ""))
        elif opcion == 2:
            mostrar_seccion("VISIÓN GENERAL DEL PROYECTO", secciones.get("vision", ""))
        elif opcion == 3:
            mostrar_seccion("SPRINT 1 (Demo 1 – asincrónica)", secciones.get("sprint1", ""))
        elif opcion == 4:
            mostrar_seccion("SPRINT 2 (Demo 2 – sincrónica)", secciones.get("sprint2", ""))
        elif opcion == 8:
            print("\nRecargando DOCUMENTACION.md...\n")
            md = cargar_documentacion(RUTA_DOC)
            secciones = dividir_secciones(md)
        elif opcion == 9:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
