#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                   🏪  PROYECTO AURELION - VISOR INTERACTIVO  🏪              ║
║                                                                               ║
║                         Sistema de Navegación Multinivel                      ║
║                              Documentación Técnica                            ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Características principales:
• Navegación multinivel con menús y submenús
• Breadcrumbs (migas de pan) para orientación
• Sistema intuitivo de navegación: [0] Volver, [R] Recargar, [Q] Salir
• Visualización profesional y clara de la información
• Lectura dinámica de DOCUMENTACION.md
• Secciones organizadas jerárquicamente

Autor: Augusto Villegas
Proyecto: IBM & Guayerd - Análisis de Datos Retail
"""

import os
import re
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_DOC = os.path.join(BASE_DIR, "DOCUMENTACION.md")
DEMO_MODE = False
ASCII_MODE = False


class TipoOpcion(Enum):
    """Tipos de opciones en el menú."""
    CONTENIDO = "contenido"
    SUBMENU = "submenu"
    ACCION = "accion"


@dataclass
class OpcionMenu:
    """Representa una opción del menú con metadatos completos."""
    clave: str
    etiqueta: str
    icono: str
    tipo: TipoOpcion
    descripcion: Optional[str] = None
    hijos: List['OpcionMenu'] = field(default_factory=list)


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES DE UTILIDAD Y CARGA DE DATOS
def pausar():
    """Pausa y espera que el usuario presione ENTER."""
    if DEMO_MODE:
        return
    try:
        input("\n💡 Presioná [ENTER] para continuar...")
    except EOFError:
        return

def cargar_documentacion(ruta: str) -> str:
    """Lee el archivo de documentación completo y lo devuelve como texto."""
    if not os.path.exists(ruta):
        print("\n" + "╔" + "═" * 78 + "╗")
        print("║" + " ERROR - ARCHIVO NO ENCONTRADO ".center(78) + "║")
        print("╚" + "═" * 78 + "╝")
        print(f"\n📁 Ruta esperada: {os.path.abspath(ruta)}")
        print("⚠️  Asegurate de que DOCUMENTACION.md esté en la misma carpeta que programa.py\n")
        return ""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"\n❌ Error al leer el archivo: {e}\n")
        return ""
# ═══════════════════════════════════════════════════════════════════════════════

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def parsear_secciones(md: str) -> Dict[str, str]:
    """
    Divide la documentación en secciones usando encabezados Markdown.
    
    Retorna un diccionario con:
    - Claves: títulos de secciones normalizados
    - Valores: contenido completo de cada sección
    """
    secciones: Dict[str, str] = {}
    md = md.strip()

    if not md:
        return secciones

    # Documento completo
    secciones["DOC_COMPLETA"] = md

    # Encontrar todos los encabezados de nivel 2, 3 y 4
    patron_h2 = re.compile(r"^##\s+(.+?)$", re.MULTILINE)
    patron_h3 = re.compile(r"^###\s+(.+?)$", re.MULTILINE)
    patron_h4 = re.compile(r"^####\s+(.+?)$", re.MULTILINE)
    
    matches_h2 = list(patron_h2.finditer(md))

    # Contenido antes del primer H2 (Introducción)
    if matches_h2:
        intro = md[:matches_h2[0].start()].strip()
        if intro:
            secciones["INTRO"] = intro

    # Procesar cada sección H2
    for i, match in enumerate(matches_h2):
        titulo = match.group(1).strip()
        inicio = match.start()
        fin = matches_h2[i + 1].start() if i + 1 < len(matches_h2) else len(md)
        contenido_completo = md[inicio:fin].strip()
        
        # Normalizar clave
        clave = normalizar_clave(titulo)
        secciones[clave] = contenido_completo
        
        # Buscar subsecciones H3 dentro de esta H2
        subseccion_matches = list(patron_h3.finditer(contenido_completo))
        for j, sub_match in enumerate(subseccion_matches):
            sub_titulo = sub_match.group(1).strip()
            sub_inicio = sub_match.start()
            sub_fin = subseccion_matches[j + 1].start() if j + 1 < len(subseccion_matches) else len(contenido_completo)
            sub_contenido = contenido_completo[sub_inicio:sub_fin].strip()
            
            sub_clave = f"{clave}_{normalizar_clave(sub_titulo)}"
            secciones[sub_clave] = sub_contenido
            
            # Buscar subsecciones H4 dentro de cada H3
            h4_matches = list(patron_h4.finditer(sub_contenido))
            for k, h4_match in enumerate(h4_matches):
                h4_titulo = h4_match.group(1).strip()
                h4_inicio = h4_match.start()
                h4_fin = h4_matches[k + 1].start() if k + 1 < len(h4_matches) else len(sub_contenido)
                h4_contenido = sub_contenido[h4_inicio:h4_fin].strip()
                
                h4_clave = f"{sub_clave}_{normalizar_clave(h4_titulo)}"
                secciones[h4_clave] = h4_contenido

    return secciones


def normalizar_clave(titulo: str) -> str:
    """Normaliza un título para usarlo como clave de diccionario."""
    titulo = re.sub(r'[^\w\s\-]', '', titulo)
    titulo = re.sub(r'\s+', '_', titulo.strip())
    return titulo.upper()


# ═══════════════════════════════════════════════════════════════════════════════
# CONSTRUCCIÓN DE ESTRUCTURA DE MENÚS
# ═══════════════════════════════════════════════════════════════════════════════

def _strip_accents(text: str) -> str:
    """Elimina acentos para comparaciones robustas en claves/títulos."""
    text_nfd = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in text_nfd if unicodedata.category(ch) != 'Mn')


def _normalize_for_match(text: str) -> str:
    """Normaliza texto para comparación: minúsculas, sin acentos, guiones bajos."""
    t = _strip_accents(text).lower()
    t = re.sub(r"[^a-z0-9]+", "_", t)
    return t.strip('_')


def _get_title_from_content(content: str) -> Optional[str]:
    """Extrae el título de la primera línea de encabezado del bloque (##, ###, o ####)."""
    for line in content.splitlines():
        m = re.match(r"^\s*#{2,4}\s+(.*)$", line)
        if m:
            return m.group(1).strip()
    return None


def _find_first_key_by_tokens(secciones: Dict[str, str], tokens: List[str]) -> Optional[str]:
    """Busca la primera clave cuyo nombre normalizado contenga todos los tokens."""
    toks = [_normalize_for_match(tok) for tok in tokens]
    for k in secciones.keys():
        kn = _normalize_for_match(k)
        if all(tok in kn for tok in toks):
            return k
    return None


def construir_estructura_menus(secciones: Dict[str, str]) -> OpcionMenu:
    """Construye dinámicamente el árbol de menús según las secciones detectadas."""
    menu_raiz = OpcionMenu(
        clave="RAIZ", etiqueta="Proyecto Aurelion - Documentación Técnica", icono="🏪", tipo=TipoOpcion.SUBMENU
    )

    # Opción: Ver documentación completa
    if "DOC_COMPLETA" in secciones:
        menu_raiz.hijos.append(OpcionMenu(
            clave="DOC_COMPLETA", etiqueta="Ver Documentación Completa", icono="📄", tipo=TipoOpcion.CONTENIDO,
            descripcion="Visualiza todo el documento en una sola vista"
        ))

    # Introducción / portada e índice
    if "INTRO" in secciones:
        menu_raiz.hijos.append(OpcionMenu(
            clave="INTRO", etiqueta="Introducción y Tabla de Contenidos", icono="🏠", tipo=TipoOpcion.CONTENIDO,
            descripcion="Portada, índice y organización del proyecto"
        ))

    # TL;DR (buscar clave que contenga TLDR)
    k_tldr = _find_first_key_by_tokens(secciones, ["TLDR"]) 
    if k_tldr:
        menu_raiz.hijos.append(OpcionMenu(
            clave=k_tldr, etiqueta="Resumen Ejecutivo (TL;DR)", icono="📋", tipo=TipoOpcion.CONTENIDO,
            descripcion="Cambios clave y resultados principales en formato resumido"
        ))

    # Visión general (buscar por tokens)
    k_vision = _find_first_key_by_tokens(secciones, ["vision", "general"])
    if k_vision:
        menu_raiz.hijos.append(OpcionMenu(
            clave=k_vision, etiqueta="Visión General del Proyecto", icono="🎯", tipo=TipoOpcion.CONTENIDO,
            descripcion="Objetivos estratégicos y estructura del proyecto"
        ))

    # Construir Sprint 1 usando función especializada
    sprint1 = construir_submenu_sprint1(secciones)
    if sprint1:
        menu_raiz.hijos.append(sprint1)
    
    # Construir Sprint 2 usando función especializada con etapas
    sprint2 = construir_submenu_sprint2(secciones)
    if sprint2:
        menu_raiz.hijos.append(sprint2)


    # Construir Sprint 3 (Machine Learning y Modelado Predictivo)
    sprint3 = construir_submenu_sprint3(secciones)
    if sprint3:
        menu_raiz.hijos.append(sprint3)

    # Referencias y Glosario
    k_refs = next((k for k in secciones if k.startswith("5_")), None) or _find_first_key_by_tokens(secciones, ["referencia"])
    if k_refs:
        menu_raiz.hijos.append(OpcionMenu(
            clave=k_refs, etiqueta="Referencias y Bibliograf?a", icono="??", tipo=TipoOpcion.CONTENIDO,
            descripcion="Fuentes, bibliograf?a y recursos utilizados"
        ))
    k_glos = next((k for k in secciones if k.startswith("6_")), None) or _find_first_key_by_tokens(secciones, ["glosario"])
    if k_glos:
        menu_raiz.hijos.append(OpcionMenu(
            clave=k_glos, etiqueta="Glosario de T?rminos", icono="?", tipo=TipoOpcion.CONTENIDO,
            descripcion="Definiciones de t?rminos t?cnicos y de negocio"
        ))

    if ASCII_MODE:
        aplicar_ascii_iconos(menu_raiz)
    return menu_raiz

def aplicar_ascii_iconos(menu: OpcionMenu):
    """Reemplaza iconos por ASCII simple si la consola no soporta Unicode."""
    stack = [menu]
    while stack:
        nodo = stack.pop()
        nodo.icono = "*"
        stack.extend(nodo.hijos)


def construir_submenu_sprint3(secciones: Dict[str, str]) -> Optional[OpcionMenu]:
    """Construye el submenú completo del Sprint 3 con todas las nuevas secciones y subapartados."""
    # Buscar clave base de Sprint 3
    clave_base = None
    for k in secciones:
        kn = _normalize_for_match(k)
        partes = k.split('_')
        if re.match(r"^4_.*sprint.*3", kn):
            clave_base = k
            break
    if not clave_base:
        return None

    sprint3 = OpcionMenu(
        clave=clave_base,
        etiqueta="Sprint 3 (Demo 3 – Machine Learning y Modelado Predictivo)",
        icono="3️⃣",
        tipo=TipoOpcion.SUBMENU,
        descripcion="Modelado predictivo, métricas, artefactos y mejores prácticas"
    )

    # Ver Sprint 3 completo
    sprint3.hijos.append(OpcionMenu(
        clave=clave_base,
        etiqueta="Ver Sprint 3 Completo",
        icono="📖",
        tipo=TipoOpcion.CONTENIDO,
        descripcion="Todo el contenido del Sprint 3 en una sola vista"
    ))

    # Buscar todas las subsecciones H3 de Sprint 3
    subsecciones = []
    for k in secciones:
        if k.startswith(clave_base + "_"):  # H3 subsections
            titulo = _get_title_from_content(secciones[k])
            if titulo:
                # Determinar icono
                icono = "📄"
                t = titulo.lower()
                if "objetivo" in t:
                    icono = "🎯"
                elif "parámetro" in t or "artefacto" in t:
                    icono = "🗃️"
                elif "indicador" in t or "métrica" in t:
                    icono = "📊"
                elif "recomendación" in t or "consideración" in t:
                    icono = "💡"
                elif "próximo" in t:
                    icono = "⏭️"
                elif "trazabilidad" in t or "calidad" in t:
                    icono = "🔎"
                elif "hiperparámetro" in t or "validación" in t:
                    icono = "⚙️"
                elif "limitación" in t or "advertencia" in t:
                    icono = "⚠️"
                elif "ética" in t or "privacidad" in t:
                    icono = "🔐"
                elif "mantenimiento" in t or "actualización" in t:
                    icono = "🔄"
                elif "reproducibilidad" in t or "entorno" in t:
                    icono = "🖥️"
                elif "esquema" in t:
                    icono = "🗺️"
                elif "feature" in t:
                    icono = "🧩"
                elif "explicación" in t or "métrica" in t:
                    icono = "📏"
                elif "benchmark" in t or "alternativo" in t:
                    icono = "🏁"
                elif "impacto" in t or "caso de uso" in t:
                    icono = "🚀"
                elif "checklist" in t or "práctica" in t:
                    icono = "✅"
                subsecciones.append((k, titulo, icono))

    # Ordenar por código numérico
    def _num_key(label: str) -> Tuple:
        m = re.match(r"^\s*(\d+(?:\.\d+)+)", label)
        if not m:
            return (999,)
        return tuple(int(x) for x in m.group(1).split('.'))

    subsecciones.sort(key=lambda x: _num_key(x[1]))

    # Agregar subsecciones
    for clave, etiqueta, icono in subsecciones:
        sprint3.hijos.append(OpcionMenu(
            clave=clave,
            etiqueta=etiqueta,
            icono=icono,
            tipo=TipoOpcion.CONTENIDO,
            descripcion=""
        ))

    return sprint3


def construir_submenu_sprint1(secciones: Dict[str, str]) -> Optional[OpcionMenu]:
    """Construye el submenú completo del Sprint 1 dinámicamente."""
    # Buscar clave base de Sprint 1
    clave_base = None
    for k in secciones:
        kn = _normalize_for_match(k)
        partes = k.split('_')
        if re.match(r"^2_.*sprint.*1", kn):
            clave_base = k
            break
    
    if not clave_base:
        return None
    
    sprint1 = OpcionMenu(
        clave=clave_base,
        etiqueta="Sprint 1 (Demo 1 – asincrónica)",
        icono="1️⃣",
        tipo=TipoOpcion.SUBMENU,
        descripcion="Definición del problema, datasets y estructura de tablas"
    )
    
    # Ver Sprint 1 completo
    sprint1.hijos.append(OpcionMenu(
        clave=clave_base,
        etiqueta="Ver Sprint 1 Completo",
        icono="📖",
        tipo=TipoOpcion.CONTENIDO,
        descripcion="Todo el contenido del Sprint 1 en una sola vista"
    ))
    
    # Buscar todas las subsecciones H3 de Sprint 1
    subsecciones = []
    for k in secciones:
        if k.startswith(clave_base + "_"):  # H3 subsections
            titulo = _get_title_from_content(secciones[k])
            if titulo:
                # Determinar icono
                icono = "📄"
                if "problema" in titulo.lower() or "solución" in titulo.lower():
                    icono = "🎯"
                elif "dataset" in titulo.lower():
                    icono = "📊"
                elif "estructura" in titulo.lower() or "tabla" in titulo.lower():
                    icono = "🗂️"
                elif "escala" in titulo.lower() or "medición" in titulo.lower():
                    icono = "📏"
                elif "ia" in titulo.lower() or "sugerencia" in titulo.lower():
                    icono = "🤖"
                
                subsecciones.append((k, titulo, icono))
    
    # Ordenar por código numérico
    def _num_key(label: str) -> Tuple:
        m = re.match(r"^\s*(\d+(?:\.\d+)+)", label)
        if not m:
            return (999,)
        return tuple(int(x) for x in m.group(1).split('.'))
    
    subsecciones.sort(key=lambda x: _num_key(x[1]))
    
    # Agregar subsecciones
    for clave, etiqueta, icono in subsecciones:
        sprint1.hijos.append(OpcionMenu(
            clave=clave,
            etiqueta=etiqueta,
            icono=icono,
            tipo=TipoOpcion.CONTENIDO,
            descripcion=""
        ))
    
    return sprint1


def construir_submenu_sprint2(secciones: Dict[str, str]) -> Optional[OpcionMenu]:
    """Construye el submenú completo del Sprint 2 con subsecciones agrupadas."""
    # Buscar clave base de Sprint 2 (debe tener exactamente 6 partes)
    clave_base = None
    for k in secciones:
        kn = _normalize_for_match(k)
        partes = k.split('_')
        if re.match(r"^3_.*sprint.*2", kn) and len(partes) == 6:
            clave_base = k
            break
    
    if not clave_base:
        return None
    
    sprint2 = OpcionMenu(
        clave=clave_base,
        etiqueta="Sprint 2 (Demo 2 – sincrónica)",
        icono="2️⃣",
        tipo=TipoOpcion.SUBMENU,
        descripcion="ETL, análisis descriptivo y consolidación de datos"
    )
    
    # Ver Sprint 2 completo
    sprint2.hijos.append(OpcionMenu(
        clave=clave_base,
        etiqueta="Ver Sprint 2 Completo",
        icono="📖",
        tipo=TipoOpcion.CONTENIDO,
        descripcion="Todo el contenido del Sprint 2 en una sola vista"
    ))
    
    # Submenú: Etapa 1 - Limpieza
    etapa1 = construir_submenu_etapa(secciones, clave_base, "1", "Limpieza y Normalización", "🧹",
                                      "Estandarización de datos, eliminación de duplicados e integridad referencial")
    if etapa1:
        sprint2.hijos.append(etapa1)
    
    # Submenú: Etapa 2 - Análisis Descriptivo
    etapa2 = construir_submenu_etapa(secciones, clave_base, "2", "Análisis Descriptivo", "📊",
                                      "Estadísticas, distribuciones, correlaciones y visualizaciones")
    if etapa2:
        sprint2.hijos.append(etapa2)
    
    # Submenú: Etapa 3 - Procesamiento
    etapa3 = construir_submenu_etapa(secciones, clave_base, "3", "Procesamiento de Productos y Ventas", "🛒",
                                      "Análisis detallado de productos y patrones de ventas")
    if etapa3:
        sprint2.hijos.append(etapa3)
    
    # Submenú: Etapa 4 - Consolidación
    etapa4 = construir_submenu_etapa(secciones, clave_base, "4", "Consolidación e Integración", "🔗",
                                      "Integración de tablas y generación de bases finales")
    if etapa4:
        sprint2.hijos.append(etapa4)
    
    # Agregar secciones H3 que NO son etapas (3.1, 3.2, 3.3)
    otras_secciones = []
    for k in secciones:
        if k.startswith(clave_base + "_") and k.count("_") == 9:  # H3 subsections
            titulo = _get_title_from_content(secciones[k])
            if titulo:
                # Verificar si es 3.1, 3.2 o 3.3 (no etapas)
                m = re.match(r"^\s*3\.([1-3])\s", titulo)
                if m:
                    icono = "📄"
                    if "contexto" in titulo.lower():
                        icono = "🎯"
                    elif "problema" in titulo.lower():
                        icono = "🔍"
                    elif "dataset" in titulo.lower():
                        icono = "📊"
                    otras_secciones.append((k, titulo, icono))
    
    # Ordenar por código numérico
    def _num_key(label: str) -> Tuple:
        m = re.match(r"^\s*(\d+(?:\.\d+)+)", label)
        if not m:
            return (999,)
        return tuple(int(x) for x in m.group(1).split('.'))
    
    otras_secciones.sort(key=lambda x: _num_key(x[1]))
    
    # Agregar al final del menú
    for clave, etiqueta, icono in otras_secciones:
        sprint2.hijos.append(OpcionMenu(
            clave=clave,
            etiqueta=etiqueta,
            icono=icono,
            tipo=TipoOpcion.CONTENIDO,
            descripcion=""
        ))
    
    return sprint2


def construir_submenu_etapa(secciones: Dict[str, str], clave_sprint: str, 
                            num_etapa: str, nombre_etapa: str, icono: str, 
                            descripcion: str) -> Optional[OpcionMenu]:
    """Construye submenús para las etapas del Sprint 2 detectando dinámicamente subsecciones H4."""
    
    # Mapeo de números de sección a etapas (3.4 -> Etapa 1, 3.5 -> Etapa 2, etc.)
    etapa_seccion_map = {
        "1": "34",  # 3.4
        "2": "35",  # 3.5
        "3": "36",  # 3.6
        "4": "37"   # 3.7
    }
    
    if num_etapa not in etapa_seccion_map:
        return None
    
    num_seccion = etapa_seccion_map[num_etapa]
    
    # Buscar dinámicamente la clave de la etapa principal (H3)
    # Patrón: 3_SPRINT_2_..._34_ETAPA_1_... con exactamente 13 guiones bajos
    clave_etapa = None
    for k in secciones:
        if (f"_{num_seccion}_ETAPA_{num_etapa}_" in k and 
            k.count("_") == 13):
            clave_etapa = k
            break
    
    if not clave_etapa:
        return None
    
    etapa = OpcionMenu(
        clave=clave_etapa,
        etiqueta=f"Etapa {num_etapa}: {nombre_etapa}",
        icono=icono,
        tipo=TipoOpcion.SUBMENU,
        descripcion=descripcion
    )
    
    # Ver etapa completa
    etapa.hijos.append(OpcionMenu(
        clave=clave_etapa,
        etiqueta=f"Ver Etapa {num_etapa} Completa",
        icono="📖",
        tipo=TipoOpcion.CONTENIDO,
        descripcion=f"Todo el contenido de la Etapa {num_etapa}"
    ))
    
    # Buscar dinámicamente todas las subsecciones H4 de esta etapa
    # Las H4 empiezan con la clave de etapa + "_" y tienen 15+ guiones bajos
    subsecciones_h4 = []
    for k in secciones:
        if (k.startswith(clave_etapa + "_") and 
            k.count("_") >= 15):  # H4 tiene al menos 15 guiones bajos
            # Extraer el título desde el contenido
            titulo = _get_title_from_content(secciones[k])
            if titulo:
                # Determinar icono según el contenido del título
                icono_h4 = "📄"
                titulo_lower = titulo.lower()
                
                if "objetivo" in titulo_lower:
                    icono_h4 = "🎯"
                elif "estadística" in titulo_lower or "estadístic" in titulo_lower:
                    icono_h4 = "📊"
                elif "correlac" in titulo_lower:
                    icono_h4 = "🔗"
                elif "outlier" in titulo_lower:
                    icono_h4 = "🔍"
                elif "visual" in titulo_lower:
                    icono_h4 = "📈"
                elif "dataset" in titulo_lower or "trabajado" in titulo_lower:
                    icono_h4 = "🗄️"
                elif "distribuc" in titulo_lower or "transformac" in titulo_lower:
                    icono_h4 = "📉"
                elif "acciones" in titulo_lower or "principales" in titulo_lower:
                    icono_h4 = "⚙️"
                elif "calidad" in titulo_lower or "resultado" in titulo_lower:
                    icono_h4 = "✅"
                elif "producto" in titulo_lower:
                    icono_h4 = "📦"
                elif "venta" in titulo_lower:
                    icono_h4 = "💰"
                elif "modelo" in titulo_lower or "relacion" in titulo_lower:
                    icono_h4 = "🔗"
                elif "clave" in titulo_lower and "definida" in titulo_lower:
                    icono_h4 = "🔑"
                elif "merge" in titulo_lower or "secuencial" in titulo_lower:
                    icono_h4 = "🔄"
                elif "análisis" in titulo_lower or "analisis" in titulo_lower or "estratég" in titulo_lower:
                    icono_h4 = "💡"
                
                subsecciones_h4.append((k, titulo, icono_h4))
    
    # Ordenar por clave numérica para mantener orden lógico (3.4.1, 3.4.2, etc.)
    def _num_key(item):
        k, titulo, _ = item
        m = re.search(r'_(\d+)_', k.replace(clave_etapa + "_", ""))
        return int(m.group(1)) if m else 999
    
    subsecciones_h4.sort(key=_num_key)
    
    # Agregar subsecciones al menú
    for clave, titulo, icono_sub in subsecciones_h4:
        etapa.hijos.append(OpcionMenu(
            clave=clave,
            etiqueta=titulo,
            icono=icono_sub,
            tipo=TipoOpcion.CONTENIDO,
            descripcion=""
        ))
    
    return etapa


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIONES DE VISUALIZACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

def mostrar_header():
    """Muestra el encabezado principal del programa."""
    if ASCII_MODE:
        print("\n" + "=" * 78)
        print(" PROYECTO AURELION - VISOR DE DOCUMENTACION TECNICA ".center(78, "="))
        print(" IBM & Guayerd · Analisis de Datos Retail · 2025 ".center(78))
        print("=" * 78)
        return
    print("\n" + "╔" + "═" * 78 + "╗")
    print("║" + " 🏪  PROYECTO AURELION - VISOR DE DOCUMENTACIÓN TÉCNICA  🏪 ".center(78) + "║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " IBM & Guayerd · Análisis de Datos Retail · 2025 ".center(78) + "║")
    print("╚" + "═" * 78 + "╝")


def mostrar_breadcrumbs(ruta: List[str]):
    """Muestra las migas de pan (breadcrumbs) de navegación."""
    if len(ruta) <= 1:
        return
    
    print("\n📍 Ubicación: " + " → ".join(ruta))
    print("─" * 78)


def mostrar_menu(opciones: List[OpcionMenu], ruta: List[str]):
    """
    Muestra el menú actual con las opciones disponibles.
    
    Args:
        opciones: Lista de opciones del menú actual
        ruta: Ruta de navegación (breadcrumbs)
    """
    limpiar_pantalla()
    mostrar_header()
    mostrar_breadcrumbs(ruta)
    
    print("\n" + "┌" + "─" * 78 + "┐")
    print("│" + " MENÚ DE OPCIONES ".center(78) + "│")
    print("├" + "─" * 78 + "┤")
    
    for i, opcion in enumerate(opciones, 1):
        # Indicador de tipo
        tipo_indicador = "📂" if opcion.tipo == TipoOpcion.SUBMENU else "📄"
        
        # Línea principal con número y nombre
        print(f"│ [{i:>2}] {opcion.icono} {opcion.etiqueta:<62} {tipo_indicador} │")
        
        # Descripción (si existe)
        if opcion.descripcion:
            desc_lines = [opcion.descripcion[i:i+70] for i in range(0, len(opcion.descripcion), 70)]
            for desc_line in desc_lines:
                print(f"│      💬 {desc_line:<69} │")
        
        # Separador entre opciones
        if i < len(opciones):
            print("├" + "┄" * 78 + "┤")
    
    print("└" + "─" * 78 + "┘")
    
    # Opciones de navegación
    print("\n" + "═" * 78)
    if len(ruta) > 1:
        print("  [0] ⬅️  Volver al menú anterior", end="")
    else:
        print("  [Q] 🚪 Salir del programa", end="")
    
    print("  │  [R] 🔄 Recargar documentación")
    print("═" * 78)


def mostrar_contenido(titulo: str, contenido: str, ruta: List[str]):
    """
    Muestra el contenido de una sección.
    
    Args:
        titulo: Título de la sección
        contenido: Contenido a mostrar
        ruta: Ruta de navegación (breadcrumbs)
    """
    limpiar_pantalla()
    mostrar_header()
    mostrar_breadcrumbs(ruta)
    
    if ASCII_MODE:
        print("\n" + "=" * 78)
        print(f" {titulo} ".center(78, "="))
        print("=" * 78 + "\n")
    else:
        print("\n" + "╔" + "═" * 78 + "╗")
        print("║" + f" {titulo} ".center(78) + "║")
        print("╚" + "═" * 78 + "╝\n")
    
    # Mostrar contenido con scroll y bloques de output destacados (mejorado)
    lineas = contenido.split('\n')
    in_output_block = False
    output_buffer = []
    last_section_header = None
    FRAME_WIDTH = 78  # ancho interno del marco para mejor legibilidad
    max_lines = 80
    shown = 0
    for linea in lineas:
        stripped = linea.strip()
        # Capturar el último encabezado markdown para título contextual
        if re.match(r'^#{2,4}\s+.+', stripped):
            last_section_header = re.sub(r'^#{2,4}\s+', '', stripped)

        # Detectar inicio de bloque de output
        if stripped.startswith('```output'):
            in_output_block = True
            output_buffer = []
            continue
        # Detectar fin de bloque de output
        if in_output_block and stripped == '```':
            # Construir título del bloque
            titulo_bloque = 'Resultado'
            if last_section_header:
                titulo_bloque = f"Resultado · {last_section_header}"

            # Mostrar el bloque de output con formato especial
            if ASCII_MODE:
                print('\n' + '-' * FRAME_WIDTH)
                print(f" {titulo_bloque} ".center(FRAME_WIDTH, '-'))
            else:
                print('\n' + '╔' + '═' * FRAME_WIDTH + '╗')
                print('║' + f" {titulo_bloque} ".center(FRAME_WIDTH) + '║')
                print('╠' + '═' * FRAME_WIDTH + '╣')
            for out_line in output_buffer:
                # Ajustar ancho y márgenes, envolver líneas largas
                sublines = [out_line[i:i+FRAME_WIDTH] for i in range(0, len(out_line), FRAME_WIDTH)] or ['']
                for subline in sublines:
                    if ASCII_MODE:
                        print(subline)
                    else:
                        print('║ ' + subline.ljust(FRAME_WIDTH - 2) + ' ║')
            if not ASCII_MODE:
                print('╚' + '═' * FRAME_WIDTH + '╝\n')
            in_output_block = False
            output_buffer = []
            continue
        if in_output_block:
            output_buffer.append(linea)
        else:
            print(linea)
            shown += 1
            if shown >= max_lines and not DEMO_MODE:
                try:
                    input("\n--- Continuar (ENTER) ---")
                except EOFError:
                    return
                shown = 0
    
    print("\n" + ("=" * 78 if ASCII_MODE else "═" * 78))
    pausar()


def mostrar_mensaje(mensaje: str, tipo: str = "info"):
    """
    Muestra un mensaje formateado.
    
    Args:
        mensaje: Texto del mensaje
        tipo: 'info', 'success', 'warning', 'error'
    """
    iconos = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌"
    }
    
    icono = iconos.get(tipo, "ℹ️")
    print(f"\n{icono}  {mensaje}")


# ═══════════════════════════════════════════════════════════════════════════════
# LÓGICA DE NAVEGACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

class NavegadorMenus:
    """Gestiona la navegación entre menús y secciones."""
    
    def __init__(self, menu_raiz: OpcionMenu, secciones: Dict[str, str]):
        self.menu_raiz = menu_raiz
        self.secciones = secciones
        self.ruta: List[Tuple[OpcionMenu, str]] = [(menu_raiz, "Inicio")]
    
    def obtener_menu_actual(self) -> OpcionMenu:
        """Retorna el menú actual en la pila de navegación."""
        return self.ruta[-1][0]
    
    def obtener_ruta_nombres(self) -> List[str]:
        """Retorna la ruta de navegación como lista de nombres."""
        return [nombre for _, nombre in self.ruta]
    
    def navegar_a_hijo(self, indice: int):
        """Navega a una opción hija del menú actual."""
        menu_actual = self.obtener_menu_actual()
        
        if 0 <= indice < len(menu_actual.hijos):
            opcion = menu_actual.hijos[indice]
            
            if opcion.tipo == TipoOpcion.SUBMENU:
                # Navegar a submenú
                self.ruta.append((opcion, opcion.etiqueta))
            elif opcion.tipo == TipoOpcion.CONTENIDO:
                # Mostrar contenido
                contenido = self.secciones.get(opcion.clave, "⚠️ Contenido no disponible")
                ruta_nombres = self.obtener_ruta_nombres() + [opcion.etiqueta]
                mostrar_contenido(opcion.etiqueta, contenido, ruta_nombres)
        else:
            mostrar_mensaje("Opción inválida. Intenta de nuevo.", "warning")
            pausar()
    
    def volver_atras(self):
        """Vuelve al menú anterior."""
        if len(self.ruta) > 1:
            self.ruta.pop()
    
    def recargar(self) -> bool:
        """Recarga la documentación. Retorna True si fue exitoso."""
        mostrar_mensaje("Recargando DOCUMENTACION.md...", "info")
        md = cargar_documentacion(RUTA_DOC)
        
        if not md:
            mostrar_mensaje("Error al recargar la documentación.", "error")
            pausar()
            return False
        
        nuevas_secciones = parsear_secciones(md)
        print(f"ℹ️ Secciones detectadas: {len(nuevas_secciones)}")
        if not nuevas_secciones:
            mostrar_mensaje("No se pudieron detectar secciones.", "error")
            pausar()
            return False
        
        self.secciones = nuevas_secciones
        mostrar_mensaje("Documentación recargada exitosamente.", "success")
        pausar()
        return True
    
    def ejecutar(self):
        """Loop principal de navegación."""
        while True:
            menu_actual = self.obtener_menu_actual()
            ruta_nombres = self.obtener_ruta_nombres()
            
            mostrar_menu(menu_actual.hijos, ruta_nombres)
            
            try:
                opcion = input("\n👉 Seleccioná una opción: ").strip().upper()
            except EOFError:
                mostrar_mensaje("Entrada no disponible. Saliendo del visor.", "warning")
                break
            
            # Opción: Salir
            if opcion == 'Q' and len(self.ruta) == 1:
                limpiar_pantalla()
                print("\n" + "╔" + "═" * 78 + "╗")
                print("║" + " Gracias por usar el Visor de Documentación de Aurelion ".center(78) + "║")
                print("║" + " ¡Hasta pronto! 👋 ".center(78) + "║")
                print("╚" + "═" * 78 + "╝\n")
                break
            
            # Opción: Volver
            elif opcion == '0' and len(self.ruta) > 1:
                self.volver_atras()
            
            # Opción: Recargar
            elif opcion == 'R':
                if self.recargar():
                    # Reconstruir estructura de menús
                    nuevo_menu = construir_estructura_menus(self.secciones)
                    self.menu_raiz = nuevo_menu
                    self.ruta = [(nuevo_menu, "Inicio")]
            
            # Opción numérica
            elif opcion.isdigit():
                indice = int(opcion) - 1
                self.navegar_a_hijo(indice)
            
            else:
                mostrar_mensaje("Opción no reconocida. Intentá de nuevo.", "warning")
                pausar()


# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL

def main():
    mostrar_mensaje("Cargando documentación...", "info")
    md = cargar_documentacion(RUTA_DOC)
    if not md:
        mostrar_mensaje("No se pudo cargar DOCUMENTACION.md", "error")
        return

    secciones = parsear_secciones(md)
    print(f"ℹ️ Secciones detectadas: {len(secciones)}")

    # Validar presencia de secciones clave
    requeridas = {
        "DOC_COMPLETA": secciones.get("DOC_COMPLETA"),
        "INTRO": secciones.get("INTRO"),
        "SPRINT1": _find_first_key_by_tokens(secciones, ["sprint", "1"]),
        "SPRINT2": _find_first_key_by_tokens(secciones, ["sprint", "2"]),
        "SPRINT3": _find_first_key_by_tokens(secciones, ["sprint", "3"]),
    }
    faltantes = [k for k, v in requeridas.items() if not v]
    if faltantes:
        print(f"⚠️ Secciones faltantes: {', '.join(faltantes)}")
    
    # Construir estructura de menús
    print("🏗️  Construyendo estructura de menús...")
    menu_raiz = construir_estructura_menus(secciones)
    
    # Iniciar navegador o demo
    if DEMO_MODE:
        print("✅ Sistema listo. Modo demo activado.\n")
        clave_tldr = _find_first_key_by_tokens(secciones, ["TLDR"]) or "DOC_COMPLETA"
        mostrar_contenido("DEMO - Resumen ejecutivo", secciones.get(clave_tldr, "Contenido no disponible"), ["Inicio", "Demo"])
        return

    print("✅ Sistema listo. Iniciando navegador...\n")
    pausar()
    
    navegador = NavegadorMenus(menu_raiz, secciones)
    navegador.ejecutar()


if __name__ == "__main__":
    main()
