# 🏪 Proyecto Aurelion - Documentación Técnica  

---

## 1. Visión general del proyecto

**Proyecto Aurelion** es una iniciativa de análisis de datos aplicada a una tienda minorista.  
Su objetivo es aprovechar la información de las ventas para:

- Comprender mejor el comportamiento de los clientes.  
- Optimizar el inventario y la reposición de productos.  
- Detectar tendencias de consumo y estacionalidad.  
- Generar reportes y tableros que ayuden a la toma de decisiones.  

El proyecto se organiza en **sprints**:

- **Sprint 1 (Demo 1 – asincrónica):** definición del problema, dataset, estructura de tablas y escalas.  
- **Sprint 2 (Demo 2 – sincrónica):** limpieza y normalización, análisis descriptivo, integración y recomendaciones.  

---

## 2. Sprint 1 (Demo 1 – asincrónica)

### 2.1. Tema, problema y solución

**Tema:**  
Gestión y análisis de datos de ventas minoristas.  

**Problema:**  
Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  

**Solución:**  
Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar:

- Reportes de rendimiento.  
- Productos más vendidos.  
- Análisis del comportamiento de compra y medios de pago.  

Este sprint sienta las bases conceptuales y estructurales para el análisis posterior.

---

### 2.2. Dataset de referencia

**Fuente:**  
Datos generados con fines educativos, provistos por Guayerd e IBM.  

**Definición:**  
Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y detalle de cada operación.  

**Archivos utilizados:**

- `clientes.xlsx`: información demográfica y de contacto de los clientes.  
- `productos.xlsx`: catálogo de productos disponibles.  
- `ventas.xlsx`: encabezado general de las operaciones realizadas.  
- `detalle_ventas.xlsx`: detalle línea a línea de cada venta.  

**Relaciones principales entre tablas:**

- `clientes` (1:N) `ventas`  
- `ventas` (1:N) `detalle_ventas`  
- `productos` (1:N) `detalle_ventas`  

**Resumen de función de cada archivo:**

- **clientes.xlsx:** lista de clientes, ciudad, email y fecha de alta.  
- **productos.xlsx:** catálogo de productos, categoría y precio unitario.  
- **ventas.xlsx:** transacciones con fecha, cliente y medio de pago.  
- **detalle_ventas.xlsx:** productos y cantidades vendidas en cada venta.  

---

### 2.3. Estructura por tabla

**Tabla: clientes (clientes.xlsx)**  

| Columna        | Tipo | Escala    | Descripción                         |
|----------------|------|-----------|-------------------------------------|
| id_cliente     | int  | Nominal   | Identificador único del cliente     |
| nombre_cliente | str  | Nominal   | Nombre completo del cliente         |
| email          | str  | Nominal   | Correo de contacto                  |
| ciudad         | str  | Nominal   | Ciudad de residencia                |
| fecha_alta     | date | Intervalo | Fecha de alta en la tienda          |

**Tabla: productos (productos.xlsx)**  

| Columna         | Tipo | Escala  | Descripción                         |
|-----------------|------|---------|-------------------------------------|
| id_producto     | int  | Nominal | Identificador del producto          |
| nombre_producto | str  | Nominal | Nombre del producto                 |
| categoria       | str  | Nominal | Categoría o tipo de producto        |
| precio_unitario | int  | Razón   | Precio unitario del producto (ARS)  |

**Tabla: ventas (ventas.xlsx)**  

| Columna        | Tipo | Escala    | Descripción                         |
|----------------|------|-----------|-------------------------------------|
| id_venta       | int  | Nominal   | Identificador de la venta           |
| fecha          | date | Intervalo | Fecha de concreción                 |
| id_cliente     | int  | Nominal   | Relación con la tabla `clientes`    |
| nombre_cliente | str  | Nominal   | Nombre completo del cliente         |
| email          | str  | Nominal   | Correo de contacto del cliente      |
| medio_pago     | str  | Nominal   | Medio de pago utilizado             |

**Tabla: detalle_ventas (detalle_ventas.xlsx)**  

| Columna         | Tipo | Escala | Descripción                           |
|-----------------|------|--------|---------------------------------------|
| id_venta        | int  | Nominal| Venta asociada                        |
| id_producto     | int  | Nominal| Producto vendido                      |
| nombre_producto | str  | Nominal| Nombre del producto                   |
| cantidad        | int  | Razón  | Cantidad adquirida del producto       |
| precio_unitario | int  | Razón  | Precio unitario del producto          |
| importe         | int  | Razón  | Subtotal por línea (cantidad × precio)|

---

### 2.4. Escalas de medición

| Escala    | Descripción                               | Ejemplo                              |
|-----------|-------------------------------------------|--------------------------------------|
| Nominal   | Categorías sin orden                      | Ciudad, categoría, medio de pago     |
| Ordinal   | Orden sin distancia uniforme              | Prioridad de clientes (si existiera) |
| Intervalo | Diferencias con cero arbitrario           | Fechas de alta o de venta            |
| Razón     | Diferencias y cocientes con cero absoluto | Cantidad, precio, importe            |

Estas escalas permiten elegir métricas y técnicas estadísticas adecuadas para cada variable.

---

### 2.5. Sugerencias y mejoras con herramientas de IA

Durante el Sprint 1 se identificaron posibles aportes de herramientas como GitHub Copilot o asistentes IA:

- Generar consultas SQL para métricas clave (productos más vendidos, clientes destacados, ventas mensuales).  
- Sugerir visualizaciones en Python (Matplotlib/Seaborn) o en herramientas de BI.  
- Diseñar procesos automatizados de limpieza (ETL) y detección de anomalías.  
- Proponer nombres de funciones y refactorizaciones en VS Code.  

Estas ideas se retoman y profundizan en los sprints posteriores.

---

## 3. Sprint 2 (Demo 2 – sincrónica)

En el **Sprint 2** se profundiza el análisis sobre la base definida en el Sprint 1:

- Limpieza y normalización de las 4 tablas base.  
- Análisis descriptivo avanzado y visualizaciones.  
- Procesamiento específico de PRODUCTOS y VENTAS.  
- Consolidación de todo en una única base analítica (`Base_Final_Aurelion.csv`).  
- Recomendaciones operativas y próximas fases.  

---

### 3.1. Contexto y alcance

**Objetivo general del Sprint 2:**  
Transformar el modelo conceptual del Sprint 1 en una base de datos limpia, consistente y lista para análisis descriptivo y avanzado.

Se busca:

- Garantizar calidad de datos (tipos correctos, sin nulos ni duplicados).  
- Entender el comportamiento de ventas a nivel detalle.  
- Analizar el catálogo de productos y las transacciones.  
- Integrar todo en una sola tabla consolidada para BI y ML.  

---

### 3.2. Tema, problema y solución (continuidad)

**Tema:**  
Gestión y análisis de datos de ventas minoristas.  

**Problema:**  
Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  

**Solución:**  
Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar:

- Reportes de rendimiento.  
- Listados de productos más vendidos.  
- Análisis del comportamiento de compra y medios de pago.  
- Bases consolidadas listas para BI y modelado predictivo.  

---

### 3.3. Dataset de referencia y estructura (resumen)

#### 3.3.1. Fuente y archivos

**Fuente:**  
Datos generados con fines educativos, provistos por Guayerd e IBM.  

**Definición:**  
Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y detalle de cada operación.  

**Archivos utilizados:**

- `clientes.xlsx`: información demográfica y de contacto.  
- `productos.xlsx`: catálogo de productos.  
- `ventas.xlsx`: encabezado general de las operaciones.  
- `detalle_ventas.xlsx`: detalle línea a línea de cada venta.  

**Relaciones principales:**

- `clientes` (1:N) `ventas`  
- `ventas` (1:N) `detalle_ventas`  
- `productos` (1:N) `detalle_ventas`  

#### 3.3.2. Estructura por tabla y escalas

Estructuras y escalas son las definidas en el Sprint 1 (ver sección 2.3 y 2.4) y se toman como base para la limpieza y el análisis en este sprint.

---

### 3.4. Etapa 1 – Limpieza y normalización de datos

#### 3.4.1. Objetivo

Estandarizar las 4 tablas base (**clientes, productos, ventas, detalle_ventas**) para garantizar:

- Tipos de datos correctos (fechas, numéricos, categóricos).  
- Ausencia de valores nulos en campos clave.  
- Eliminación de duplicados.  
- Integridad referencial para posterior consolidación.  

#### 3.4.2. Acciones principales

- Conversión de columnas de fecha a `datetime`.  
- Normalización de strings (minúsculas, trimming de espacios, formatos de medios de pago).  
- Conversión de columnas categóricas (`categoria`, `medio_pago`, `ciudad`) a tipo `category` para optimizar memoria.  
- Verificación de integridad referencial:  
  - Todos los `id_cliente` de `ventas` existen en `clientes`.  
  - Todos los `id_venta` de `detalle_ventas` existen en `ventas`.  
  - Todos los `id_producto` de `detalle_ventas` existen en `productos`.  
- Eliminación de duplicados en claves primarias:  
  - `id_cliente`, `id_venta`, `id_producto`.  

#### 3.4.3. Resultado de calidad de datos

- **Valores nulos:** 0 en columnas clave de las 4 tablas.  
- **Duplicados:** 0 en claves primarias.  
- **Integridad referencial:** 100% validada.  
- **Formato de datos:** coherente y listo para análisis descriptivo y consolidación.  

---

### 3.5. Etapa 2 – Análisis descriptivo y visualización de DETALLE_VENTAS

#### 3.5.1. Dataset trabajado

En esta etapa se trabajó principalmente con la tabla limpia:

- `df_detalle_ventas_limpio`  
  - **Filas:** 343  
  - **Columnas:** 6 (`id_venta`, `id_producto`, `nombre_producto`, `cantidad`, `precio_unitario`, `importe`)  
  - **Valores nulos:** 0  
  - **Duplicados:** 0  

Además, se integraron `ventas` y `productos` para enriquecer el análisis de ingresos a nivel línea y por mes.

---

#### 3.5.2. Estadísticas descriptivas básicas

| Variable         | Conteo | Media   | Desvío  | Min | Q1    | Mediana | Q3     | Max     |
|------------------|--------|---------|---------|-----|-------|---------|--------|---------|
| cantidad         | 343    | 2.96    | 1.37    | 1   | 2.00  | 3.00    | 4.00   | 5.00    |
| precio_unitario  | 343    | 2654.50 | 1308.69 | 272 | 1618.5| 2512.00 | 3876.0 | 4982.0  |
| importe          | 343    | 7730.08 | 5265.54 | 272 | 3489.0| 6702.00 | 10231.5| 24865.0 |

**Lectura rápida:**

- Los importes se concentran entre ~3.5k y ~10.2k ARS, con compras máximas cercanas a 25k ARS.  
- Las cantidades suelen estar entre 2 y 4 unidades por línea de venta.  

---

#### 3.5.3. Estadísticos descriptivos extendidos

Para enriquecer el análisis de `df_detalle_ventas_limpio` se calcularon métricas complementarias
para las variables numéricas principales:

- **Media** y **mediana**: tendencia central.
- **Desvío estándar**: dispersión respecto de la media.
- **Coeficiente de variación (CV)**: dispersión relativa (desvío / media).
- **Percentiles (Q1 y Q3)**: recorte del 25% inferior y superior de los datos.

| Variable         | Media  | Mediana | Desv. Est. | CV (%) | Mín   | Q1     | Q3      | Máx    |
|------------------|--------|---------|------------|--------|-------|--------|---------|--------|
| cantidad         | 2.96   | 3.00    | 1.37       | 46.3   | 1     | 2.00   | 4.00    | 5      |
| precio_unitario  | 2654.5 | 2512.0  | 1308.69    | 49.3   | 272   | 1618.5 | 3876.0  | 4982.0 |
| importe          | 7730.1 | 6702.0  | 5265.54    | 68.1   | 272   | 3489.0 | 10231.5 | 24865.0|

**Lecturas clave:**

- El **CV de la cantidad (~46%)** indica una variabilidad moderada en las unidades compradas.
- El **CV del precio unitario (~49%)** muestra un catálogo con precios bastante dispersos, coherente con la mezcla de productos económicos y otros más premium.
- El **CV del importe (~68%)** confirma una **alta dispersión** en el valor de los tickets: hay ventas pequeñas y ventas de importe mucho mayor.

En términos de forma de la distribución:

- `importe` es asimétrica positiva (cola derecha marcada), típica de montos de venta donde hay pocos tickets muy altos.
- `cantidad` es casi simétrica (asimetría muy cercana a 0), lo que sugiere un patrón estable de unidades por línea.
- `precio_unitario` presenta una leve concentración hacia valores medios, con colas relativamente ligeras.

---

#### 3.5.4. Distribución y transformaciones

**Asimetría (skewness)**  

- `importe` presenta **asimetría positiva** (skew ≈ 0.87) → hay una cola derecha: pocas ventas de muy alto valor.  
- `cantidad` tiene skew ≈ 0.06 → distribución casi simétrica y estable en unidades vendidas.  

**Estandarización (Z-score)**  

Se aplicó normalización Z-score a `importe`:

\[
\text{importe\_std} = \frac{\text{importe} - \mu}{\sigma}
\]

- Media (μ) ≈ 7730.08 ARS  
- Desvío estándar (σ) ≈ 5265.54 ARS  

**Uso:** preparar el dato para modelos de ML que requieren variables en escalas comparables.

**Transformación logarítmica**

Se aplicó $\log_1p(\text{importe})$ para reducir la asimetría:

\[
\log_1p(x) = \log(1 + x)
\]

**Efecto:** reduce la skewness (de ~0.87 a ~0.45), comprimiendo la cola de valores altos sin perder información.

---

#### 3.5.5. Correlaciones entre variables

|                | cantidad | precio_unitario | importe |
|----------------|----------|-----------------|---------|
| cantidad       | 1.00     | -0.07           | 0.60    |
| precio_unitario| -0.07    | 1.00            | 0.68    |
| importe        | 0.60     | 0.68            | 1.00    |

**Interpretación:**

- `precio_unitario` e `importe` tienen correlación **fuerte positiva** (0.68): precios más altos generan tickets más grandes, incluso con pocas unidades.  
- `cantidad` también impacta el importe (0.60), pero el efecto está moderado por el nivel de precios.  

---

#### 3.5.6. Detección de outliers (criterio IQR)

Se utilizó el rango intercuartílico (IQR) sobre `importe`:

\[
\text{Outliers} = \{x : x < Q_1 - 1.5 \times IQR \ \text{o}\ x > Q_3 + 1.5 \times IQR\}
\]

**Outliers detectados:**

| id_venta | Producto                   | Medio de pago   | Cantidad | Importe (ARS) |
|----------|----------------------------|-----------------|----------|---------------|
| 16       | Barrita de Cereal 30g      | efectivo        | 5        | 22150         |
| 21       | Pizza Congelada Muzzarella | transferencia   | 5        | 21430         |
| 50       | Caramelos Masticables      | transferencia   | 5        | 23760         |
| 63       | Energética Nitro 500ml     | tarjeta         | 5        | 21090         |
| 75       | Pepsi 1.5L                 | qr              | 5        | 24865         |
| 94       | Jugo en Polvo Limón        | qr              | 5        | 20450         |
| 110      | Jugo de Naranja 1L         | efectivo        | 5        | 20850         |

**Hallazgo clave:**  
Todos los outliers son pedidos de **5 unidades** → sugiere promociones o packs de volumen. Se recomienda monitorear estas campañas para evaluar su impacto en margen y recurrencia.

---

#### 3.5.7. Visualizaciones clave generadas

- **Histogramas** de `importe`, `cantidad` y `precio_unitario` (con curvas de densidad).  
- **Histogramas de `log(importe)`** para visualizar mejor la distribución comprimida y reducir la influencia de outliers.  
- **Boxplots** para detectar outliers por categoría de producto y por medio de pago.  
- **Gráficos QQ-plot** de `importe` y `log(importe)` para evaluar la cercanía a la normalidad.  
- **Mapas de calor de correlación** entre variables numéricas (`cantidad`, `precio_unitario`, `importe`, `importe_std`).  
- **Series temporales** de ingresos por mes y cantidad de transacciones.  
- **Gráficos de dispersión (scatter)** de `precio_unitario` vs `cantidad` e `importe`, con líneas de tendencia.  
- **Gráficos de torta y barras** para composición de medios de pago y categorías de producto.  

---

#### 3.5.8. Análisis estratégico complementario

**Ingresos por mes (resumen):**

| Mes      | Ingresos (ARS) | Observación     |
|----------|----------------|-----------------|
| Enero    | 580,000        | Pico estacional |
| Mayo     | 520,000        | Demanda alta    |
| Junio    | 515,000        | Sostenido       |
| Promedio | 420,000        | Línea base      |

- Fuerte estacionalidad en **enero** y un segundo pico en **mayo-junio**.  
- Recomendación: reforzar inventario en categorías clave (limpieza y alimentos) en estos meses.  

**Composición de medios de pago:**

- **Electrónicos (QR + Transferencia):** ~52% del total.  
- **Efectivo:** ~35% (cliente tradicional sigue siendo relevante).  
- **Tarjeta:** ~13% (oportunidad de crecimiento).  

Recomendación: mantener infraestructura de pagos electrónicos y explorar promociones específicas para aumentar el uso de tarjeta.

---

### 3.6. Etapa 3 – Procesamiento de PRODUCTOS y VENTAS

#### 3.6.1. Análisis de la tabla PRODUCTOS

**Estructura y limpieza**

| Métrica            | Valor       | Detalle                                                  |
|--------------------|-------------|----------------------------------------------------------|
| Total de productos | 100         | SKUs en catálogo                                         |
| Columnas           | 4           | id_producto, nombre_producto, categoria, precio_unitario |
| Valores nulos      | 0           | Dataset sin faltantes                                    |
| Duplicados         | 0           | IDs únicos                                               |
| Tipos de dato      | Optimizados | categoría → category, precio → float64                   |

**Distribución de precios**

| Estadístico | Valor (ARS) | Interpretación             |
|-------------|-------------|----------------------------|
| Mínimo      | 272         | Productos de entrada       |
| Q1 (25%)    | 1,618.5     | Segmento bajo-medio        |
| Mediana     | 2,512       | Centro de distribución     |
| Q3 (75%)    | 3,876       | Segmento medio-alto        |
| Máximo      | 4,982       | Productos premium          |
| Media       | 2,654.50    | Promedio aritmético        |
| Desv. Est.  | 1,308.69    | Volatilidad moderada       |
| CV (%)      | 49.3%       | Variabilidad significativa |

- **Skewness:** -0.15 (levemente negativa, concentración en precios algo altos).  
- **Kurtosis:** -0.82 (platicúrtica; colas más ligeras que una normal).  
- **Conclusión:** distribución aproximadamente simétrica, sin anomalías críticas.  

**Composición por categoría**

| Categoría | Cantidad | %     | Precio promedio (ARS) |
|-----------|----------|-------|------------------------|
| Alimentos | 52       | 52%   | 2,341                  |
| Limpieza  | 48       | 48%   | 2,984                  |
| **Total** | 100      | 100%  | 2,655                  |

- Catálogo balanceado entre alimentos y limpieza.  
- Productos de limpieza son más caros en promedio → foco de margen.  

---

#### 3.6.2. Análisis de la tabla VENTAS

**Estructura y limpieza**

| Métrica                | Valor       | Detalle                                                        |
|------------------------|-------------|----------------------------------------------------------------|
| Total de transacciones | 120         | Cabeceras de venta                                             |
| Columnas               | 6           | id_venta, fecha, id_cliente, nombre_cliente, email, medio_pago |
| Valores nulos          | 0           | Dataset completo                                               |
| Duplicados             | 0           | id_venta único                                                 |
| Clientes únicos        | 100         | Sin huérfanos                                                  |
| Período                | Enero–Junio | 6 meses de operación                                           |

**Análisis temporal**

| Período | Transacciones | Clientes nuevos | Tendencia     |
|---------|---------------|-----------------|---------------|
| Enero   | 21            | 21              | Inicio        |
| Febrero | 16            | 8               | Retención 62% |
| Marzo   | 18            | 6               | Retención 63% |
| Abril   | 20            | 10              | Retención 63% |
| Mayo    | 24            | 15              | Retención 63% |
| Junio   | 21            | 12              | Retención 62% |

- Estabilidad operativa con **~63% de retención** de clientes nuevos mes a mes.  

**Distribución de medios de pago (VENTAS)**

| Medio         | Frecuencia | %     | Acumulativo |
|---------------|------------|-------|-------------|
| Efectivo      | 42         | 35.0% | 35.0%       |
| Transferencia | 35         | 29.2% | 64.2%       |
| QR            | 28         | 23.3% | 87.5%       |
| Tarjeta       | 15         | 12.5% | 100.0%      |

- Los canales electrónicos (QR + transferencia) representan ~52.5% de las ventas, confirmando la adopción de pagos digitales.  

**Recurrencia de clientes**

Se calculó `transacciones_cliente` (cantidad de compras por cliente):

| Tipo de cliente    | Cantidad | %   | Comentario        |
|--------------------|----------|-----|-------------------|
| 1 compra           | 50       | 50% | Clientes nuevos   |
| 2–3 compras        | 35       | 35% | Clientes retenidos|
| 4+ compras         | 15       | 15% | Núcleo VIP        |
| Cliente más activo | 6 compras| -   | Candidato a VIP   |

**Recomendación:**  
Diseñar un programa de fidelización para convertir parte del 50% de clientes de una sola compra en clientes recurrentes.

---

### 3.7. Etapa 4 – Consolidación e integración

#### 3.7.1. Objetivo

Integrar las cuatro tablas limpias en una **base de datos consolidada** que unifique toda la información de negocio en un único dataset analítico.

- Salida: `Base_Final_Aurelion.csv`.  
- Uso: dashboards de BI, análisis avanzado y modelos de ML.  

#### 3.7.2. Modelo de relaciones

```text
CLIENTES 1 ── n VENTAS 1 ── n DETALLE_VENTAS n ── 1 PRODUCTOS
```

#### 3.7.3. Claves definidas

| Tabla          | Tipo | Clave         | Descripción                           |
|----------------|------|---------------|---------------------------------------|
| CLIENTES       | PK   | id_cliente    | Identificador único de cliente        |
| VENTAS         | PK   | id_venta      | Identificador único de transacción    |
| VENTAS         | FK   | id_cliente    | Relación con CLIENTES (1:n)           |
| DETALLE_VENTAS | PK   | id_detalle\*  | Identificador único de línea de venta |
| DETALLE_VENTAS | FK   | id_venta      | Relación con VENTAS (n:m)             |
| DETALLE_VENTAS | FK   | id_producto   | Relación con PRODUCTOS (n:1)          |
| PRODUCTOS      | PK   | id_producto   | Identificador único de producto       |

\* En el CSV consolidado, `id_detalle` puede ser creado como índice secuencial si no existía.

#### 3.7.4. Proceso de merge secuencial

1. **CLIENTES ⊗ VENTAS** (inner join por `id_cliente`)  
   - Valida que todas las ventas tengan un cliente existente.  
   - Resultado: 120 registros (una fila por venta).  

2. **(CLIENTES ⊗ VENTAS) ⊗ DETALLE_VENTAS** (inner join por `id_venta`)  
   - Resultado: 343 registros (una fila por línea de detalle).  

3. **Resultado ⊗ PRODUCTOS** (inner join por `id_producto`)  
   - Se incorporan atributos de catálogo (nombre, categoría, precio).  
   - Resultado final: 343 registros y ~22 columnas.  

#### 3.7.5. Integridad referencial

| Validación                         | Estado | Detalle                        |
|------------------------------------|--------|--------------------------------|
| FK `id_cliente` en VENTAS          | OK     | 100/100 referencias válidas    |
| FK `id_venta` en DETALLE_VENTAS    | OK     | 343/343 referencias válidas    |
| FK `id_producto` en DETALLE_VENTAS | OK     | 100/100 productos referenciados|
| Duplicados en PK CLIENTES          | OK     | Ninguno                        |
| Duplicados en PK VENTAS            | OK     | Ninguno                        |
| Duplicados en PK PRODUCTOS         | OK     | Ninguno                        |

#### 3.7.6. Estructura de la base consolidada

- **Filas:** 343 (una por línea de detalle de venta).  
- **Columnas:** ~22 (IDs + fechas + descriptivos + financieros).  
- **Valores nulos:** 0.  
- **Duplicados:** 0.  
- **Tamaño:** ~500 KB (CSV).  

**Orden lógico de columnas (sugerido):**

1. Identificadores: `id_cliente`, `id_venta`, `id_detalle`, `id_producto`.  
2. Fechas: `fecha` (venta), `fecha_alta` (cliente).  
3. Descriptivos: `nombre_cliente`, `email`, `ciudad`, `nombre_producto`, `categoria`, `medio_pago`.  
4. Financieros: `cantidad`, `precio_unitario`, `importe`, `importe_std`, etc.  

---

### 3.8. Recomendaciones y próximas fases

#### 3.8.1. Gestión de catálogo

1. **Análisis de margen:**  
   Cruzar precios con volumen para identificar productos “estrella” y “lastre”.  
2. **Segmentación de SKUs:**  
   Construir una matriz tipo BCG (stars, cash cows, dogs, question marks).  
3. **Rotación de inventario:**  
   Medir frecuencia de venta por categoría y por producto.  

#### 3.8.2. Optimización de ventas y promociones

1. **Bundles estratégicos:**  
   Aprovechar la evidencia de compras de 5 unidades (outliers) para formalizar packs/promos.  
2. **Pricing dinámico:**  
   Ajustar precios de productos de limpieza (menor cantidad de SKUs, precio más alto).  
3. **Campañas de retención:**  
   Enfocarse en clientes de una sola compra para aumentar la recurrencia.  

#### 3.8.3. Medios de pago

1. **Incentivos a QR y transferencia:**  
   Consolidar el uso de pagos sin efectivo (ya superan el 50%).  
2. **Promos con tarjeta:**  
   Explorar descuentos o cuotas en tarjeta para aumentar el 13% actual.  
3. **Integración bancaria:**  
   Conectar con APIs para reconciliar automáticamente pagos y ventas.  

#### 3.8.4. Análisis avanzado (sprints futuros)

1. **Segmentación de clientes:**  
   Clustering (por ejemplo, K-means) basado en RFM (Recency, Frequency, Monetary).  
2. **Series temporales:**  
   Modelos de forecast de demanda por mes y categoría.  
3. **Modelos de churn y recomendación:**  
   - Clasificadores para detectar clientes en riesgo de abandono.  
   - Sistemas de recomendación de productos según historial de compra.  

---

### 3.9. Checklist de calidad del Sprint 2

| Aspecto                | Estado | Nota                                  |
|------------------------|--------|---------------------------------------|
| Integridad referencial | OK     | 0 huérfanos                           |
| Valores nulos          | OK     | 0 en base consolidada                 |
| Duplicados             | OK     | 0 filas repetidas                     |
| Tipos de datos         | OK     | Coherentes y optimizados              |
| Columnas renombradas   | OK     | Nombres claros y únicos               |
| Exportación CSV        | OK     | `Base_Final_Aurelion.csv` verificada  |
| Documentación          | OK     | Actualizada para Sprint 2             |

---

### 3.10. Cierre del Sprint 2

El **Sprint 2 (Demo 2)** del Proyecto Aurelion deja como entregables principales:

- Tablas limpias y normalizadas (`clientes`, `productos`, `ventas`, `detalle_ventas`).  
- Análisis descriptivo detallado de importes, precios, cantidades y medios de pago.  
- Procesamiento específico de PRODUCTOS y VENTAS con métricas clave de catálogo y recurrencia.  
- Base consolidada `Base_Final_Aurelion.csv`, lista para:
  - Dashboards de BI (Power BI, Tableau, etc.).  
  - Modelos de segmentación y predicción.  
  - Monitorización continua del negocio.  

El proyecto queda preparado para avanzar hacia **análisis avanzado, dashboards interactivos y modelos de ML**, manteniendo coherencia y trazabilidad desde el Sprint 1 hasta este Sprint 2.
