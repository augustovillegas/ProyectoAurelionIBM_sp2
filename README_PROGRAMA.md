# 🏪 Proyecto Aurelion - Visor Interactivo de Documentación

## 📖 Descripción

Sistema de navegación multinivel para visualizar la documentación técnica del Proyecto Aurelion de forma organizada, intuitiva y profesional.

---

## ✨ Características Principales

### 🎯 Navegación Multinivel
- **Menús jerárquicos**: Accede a la información organizada en secciones, subsecciones y etapas
- **Breadcrumbs**: Siempre sabrás dónde estás gracias a las "migas de pan" de navegación
- **Vista completa o detallada**: Elige entre ver todo el contenido junto o explorar sección por sección

### 🎨 Diseño Profesional
- **Interfaz visual atractiva**: Uso de caracteres Unicode para crear bordes, separadores y estructura clara
- **Emojis descriptivos**: Cada opción tiene un icono que representa su contenido
- **Descripciones contextuales**: Cada opción muestra una breve descripción de lo que contiene

### 🧭 Navegación Intuitiva
- **[0] Volver**: En cualquier submenú, presiona `0` para volver al nivel anterior
- **[R] Recargar**: Actualiza el contenido de DOCUMENTACION.md sin reiniciar el programa
- **[Q] Salir**: Cierra el programa de forma elegante desde el menú principal

---

## 🚀 Cómo Usar

### Inicio del Programa
```bash
python programa.py
```

### Estructura de Navegación

```
🏪 Inicio (Menú Principal)
│
├── 📄 Ver Documentación Completa
│   └── Todo el documento en una sola vista
│
├── 🏠 Introducción y Tabla de Contenidos
│   └── Portada e índice del proyecto
│
├── 📋 Resumen Ejecutivo (TL;DR)
│   └── Cambios clave y resultados principales
│
├── 🎯 Visión General del Proyecto
│   └── Objetivos estratégicos
│
├── 1️⃣ Sprint 1 (Demo 1 – asincrónica) 📂
│   ├── 📖 Ver Sprint 1 Completo
│   ├── 🎯 2.1 Tema, Problema y Solución
│   ├── 📊 2.2 Dataset de Referencia
│   ├── 🗂️ 2.3 Estructura por Tabla
│   ├── 📏 2.4 Escalas de Medición
│   └── 🤖 2.5 Sugerencias con IA
│
└── 2️⃣ Sprint 2 (Demo 2 – sincrónica) 📂
    ├── 📖 Ver Sprint 2 Completo
    ├── 🎯 3.1 Contexto y Alcance
    │
    ├── 🧹 Etapa 1: Limpieza y Normalización 📂
    │   ├── 📖 Ver Etapa 1 Completa
    │   ├── 🎯 3.4.1 Objetivo
    │   ├── ⚙️ 3.4.2 Acciones Principales
    │   └── ✅ 3.4.3 Resultado de Calidad
    │
    ├── 📊 Etapa 2: Análisis Descriptivo 📂
    │   ├── 📖 Ver Etapa 2 Completa
    │   ├── 🗄️ 3.5.1 Dataset Trabajado
    │   ├── 📈 3.5.2 Estadísticas Básicas
    │   ├── 📊 3.5.3 Estadísticos Extendidos
    │   ├── 📉 3.5.4 Distribución y Transformaciones
    │   ├── 🔗 3.5.5 Correlaciones
    │   ├── 🔍 3.5.6 Detección de Outliers
    │   ├── 📊 3.5.7 Visualizaciones Clave
    │   └── 💡 3.5.8 Análisis Estratégico
    │
    ├── 🛒 Etapa 3: Procesamiento de Productos y Ventas 📂
    │   ├── 📖 Ver Etapa 3 Completa
    │   ├── 📦 3.6.1 Análisis de Productos
    │   └── 💰 3.6.2 Análisis de Ventas
    │
    └── 🔗 Etapa 4: Consolidación e Integración 📂
        ├── 📖 Ver Etapa 4 Completa
        ├── 🎯 3.7.1 Objetivo
        ├── 🔗 3.7.2 Modelo de Relaciones
        ├── 🔑 3.7.3 Claves Definidas
        └── 🔄 3.7.4 Proceso de Merge
```

---

## 🎮 Controles y Comandos

### En el Menú Principal
| Comando | Acción |
|---------|--------|
| **1-6** | Seleccionar opción del menú |
| **Q** | Salir del programa |
| **R** | Recargar DOCUMENTACION.md |

### En Submenús
| Comando | Acción |
|---------|--------|
| **1-N** | Seleccionar opción del submenú |
| **0** | ⬅️ Volver al menú anterior |
| **R** | 🔄 Recargar documentación |

### Visualizando Contenido
| Comando | Acción |
|---------|--------|
| **ENTER** | Volver al menú actual |

---

## 📊 Iconografía y Significados

### Iconos de Tipo de Contenido
- **📂** = Submenú (contiene más opciones)
- **📄** = Contenido directo (muestra texto)
- **📖** = Vista completa de una sección

### Iconos por Categoría
- **🏠** = Inicio/Introducción
- **📋** = Resumen/TL;DR
- **🎯** = Objetivos/Contexto
- **📊** = Datos/Estadísticas
- **🗂️** = Estructura/Organización
- **📏** = Clasificación/Escalas
- **🤖** = Inteligencia Artificial
- **🧹** = Limpieza de datos
- **🛒** = Ventas/Productos
- **🔗** = Integración/Relaciones
- **📦** = Productos
- **💰** = Ventas/Ingresos
- **🔑** = Claves/IDs
- **🔄** = Procesos/Flujos

### Iconos de Navegación
- **⬅️** = Volver atrás
- **🔄** = Recargar
- **🚪** = Salir
- **👉** = Seleccionar opción
- **💡** = Ayuda/Sugerencia
- **📍** = Ubicación actual (breadcrumbs)

---

## 🎨 Ejemplo de Pantalla

```
╔══════════════════════════════════════════════════════════════════════════════╗
║          🏪  PROYECTO AURELION - VISOR DE DOCUMENTACIÓN TÉCNICA  🏪          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                IBM & Guayerd · Análisis de Datos Retail · 2025               ║
╚══════════════════════════════════════════════════════════════════════════════╝

📍 Ubicación: Inicio → Sprint 2 (Demo 2 – sincrónica) → Etapa 2: Análisis Descriptivo
────────────────────────────────────────────────────────────────────────────────

┌──────────────────────────────────────────────────────────────────────────────┐
│                              MENÚ DE OPCIONES                                │
├──────────────────────────────────────────────────────────────────────────────┤
│ [ 1] 📖 Ver Etapa 2 Completa                                            📄 │
│      💬 Todo el contenido de la Etapa 2                                      │
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤
│ [ 2] 🗄️ 3.5.1 Dataset Trabajado                                        📄 │
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤
│ [ 3] 📈 3.5.2 Estadísticas Básicas                                     📄 │
├┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┤
│ [ 4] 📊 3.5.3 Estadísticos Extendidos                                  📄 │
└──────────────────────────────────────────────────────────────────────────────┘

════════════════════════════════════════════════════════════════════════════════
  [0] ⬅️  Volver al menú anterior  │  [R] 🔄 Recargar documentación
════════════════════════════════════════════════════════════════════════════════

👉 Seleccioná una opción:
```

---

## 🔧 Requisitos Técnicos

- **Python**: 3.7 o superior
- **Archivo requerido**: `DOCUMENTACION.md` en la misma carpeta que `programa.py`
- **Sistema operativo**: Windows, Linux, macOS
- **Codificación**: UTF-8 (para caracteres especiales y emojis)

---

## 💡 Consejos de Uso

### Para Exploración Rápida
1. Usa **"Ver Documentación Completa"** si quieres una vista general rápida
2. Usa **"Resumen Ejecutivo (TL;DR)"** para los puntos clave

### Para Estudio Detallado
1. Navega por los **Sprints** y sus **Etapas**
2. Lee cada subsección de forma individual
3. Usa las opciones **"Ver [Sección] Completa"** para contextualizar

### Para Presentaciones
1. Navega directamente a la sección que necesitas presentar
2. Los breadcrumbs te ayudan a ubicarte en la estructura
3. La visualización limpia facilita la lectura en pantallas compartidas

---

## 🐛 Solución de Problemas

### El programa no inicia
- Verifica que `DOCUMENTACION.md` esté en la misma carpeta que `programa.py`
- Ejecuta: `python programa.py` desde la terminal

### Los caracteres se ven mal
- Asegúrate de que tu terminal soporte UTF-8
- En Windows PowerShell: `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8`

### El contenido no se actualiza
- Presiona **[R]** para recargar DOCUMENTACION.md
- Si editaste el archivo mientras el programa estaba abierto, usa **[R]** para ver los cambios

---

## 📝 Notas del Desarrollador

### Arquitectura del Programa
- **Patrón de diseño**: Sistema de navegación con pila (stack)
- **Estructura de datos**: Árbol de menús con nodos OpcionMenu
- **Parser**: Expresiones regulares para detectar encabezados Markdown (## y ###)
- **Normalización de claves**: Conversión automática de títulos a identificadores únicos

### Extensibilidad
El programa se adapta automáticamente a cambios en `DOCUMENTACION.md`:
- Detecta nuevas secciones nivel 2 (##)
- Detecta nuevas subsecciones nivel 3 (###)
- Reorganiza el menú según la estructura del documento

---

## 👨‍💻 Autor

**Augusto Villegas**  
Proyecto Aurelion - IBM & Guayerd  
Análisis de Datos Retail - 2025

---

## 📜 Licencia

Proyecto educativo desarrollado en el marco del programa IBM & Guayerd.

---

**¡Disfrutá explorando la documentación de Proyecto Aurelion!** 🚀
