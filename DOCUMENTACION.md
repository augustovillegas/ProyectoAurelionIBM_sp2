# PROYECTO AURELION - DOCUMENTACION TECNICA

Retail minorista | IBM & Guayerd | Noviembre 2025

---

## Tabla de contenidos

- Resumen ejecutivo (TL;DR)
- Cómo ejecutar el visor
- 1. Vision general del proyecto
- 2. Sprint 1 (Demo 1 asincronica)
- 3. Sprint 2 (Demo 2 sincronica)
- 4. Sprint 3 (Demo 3 - Machine Learning y modelado predictivo)
- 5. Referencias y Bibliografia
- 6. Glosario de Terminos

---

## TLDR - Resumen ejecutivo

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📊 DATOS TRANSACCIONALES                                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Base Transaccional:          Base_Final_Aurelion.csv                         │
│   • Dimensión:                343 filas × 21 columnas                        │
│   • Clientes únicos:          67 clientes                                    │
│   • Ventas registradas:       120 transacciones                              │
│   • Productos:                95 SKUs                                        │
│   • Calidad de datos:         0 nulos, 0 duplicados                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Medios de Pago:                                                              │
│   • Efectivo:                 32.4%                                          │
│   • QR:                       26.5%                                          │
│   • Tarjeta:                  20.1%                                          │
│   • Transferencia:            21.0%                                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Mix de Categorías:                                                           │
│   • Alimentos:                97.1%                                          │
│   • Limpieza:                 2.9%                                           │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🤖 MACHINE LEARNING                                                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Dataset ML:                  base_final_ML_clientes.csv                      │
│   • Dimensión:                67 clientes × 18 columnas                      │
│   • Features numéricas:      16 variables predictoras                        │
│   • Otras columnas:           id_cliente + ciudad                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Clustering K-Means (K=3):                                                    │
│   • Silhouette Score:        0.1985                                          │
│   • Calinski-Harabasz:       16.49                                           │
│   • Davies-Bouldin:          1.65                                            │
│   • Inertia:                 707.51                                          │
│   • Distribución clusters:    19 / 19 / 29 clientes                          │
├──────────────────────────────────────────────────────────────────────────────┤
│ Modelo de Churn (Random Forest):                                             │
│   • Accuracy Train/Test:     98.11% / 57.14%                                 │
│   • ROC-AUC:                 0.5714                                          │
│   • Umbral óptimo:           0.3790                                          │
│   • Clientes alto riesgo:    20 clientes (umbral acción: 0.70)               │
├──────────────────────────────────────────────────────────────────────────────┤
│ Modelo Valor del Cliente (Random Forest Regressor):                          │
│   • MAE Train/Test:          $3,882.50 / $7,552.50                           │
│   • RMSE Train/Test:         $6,869.72 / $10,086.19                          │
│   • R² Train/Test:            0.9242 / 0.6998                                │
│   • Media del target:        $39,573 ARS                                     │
│   • Mediana del target:      $34,326 ARS                                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📦 ARTEFACTOS EXPORTADOS                                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ • Modelos entrenados:        .pkl (Random Forest + Scalers)                  │
│ • Métricas de evaluación:     .json (Churn, Valor Cliente)                   │
│ • Importancia de features:    .csv (Top features por modelo)                 │
│ • Segmentos y riesgos:        .csv (Clusters, Alto riesgo)                   │
│ • Predicciones:               .csv (Valores predichos)                       │
└──────────────────────────────────────────────────────────────────────────────┘

---

## Cómo ejecutar el visor

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🛠️ REQUISITOS                                                                │
├──────────────────────────────────────────────────────────────────────────────┤
│ • Python:                    Versión 3.10 o superior                         │
│ • Consola:                   Soporte UTF-8                                   │
│ • Windows:                   Ejecutar `chcp 65001` o usar Windows Terminal   │
│ • Archivo requerido:         DOCUMENTACION.md (misma carpeta)                │  
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🚀 INSTRUCCIÓNES DE EJECUCIÓN                                                │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│ 1️⃣  Abrir terminal en la carpeta del proyecto                                │
│                                                                              │
│ 2️⃣  Ejecutar el comando:                                                     │
│                                                                              │
│     ```                                                                      │
│     python programa.py                                                       │
│     ```                                                                      │
│                                                                              │
│ 3️⃣  Modo Demo (opcional):                                                    │
│                                                                              │
│     ```                                                                      │
│     python programa.py --demo                                                │
│     ```                                                                      │
│                                                                              │
│     (Sin entrada interactiva, muestra solo resumen ejecutivo)                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

---

## 1. Visión general del proyecto

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🎯 OBJETIVO DEL PROYECTO                                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│ Transformar datos de ventas minoristas en insights accionables y bases    │
│ listas para Business Intelligence y Machine Learning.                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📊 TABLAS FUENTE                                                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ • clientes                                                                   │
│ • productos                                                                  │
│ • ventas                                                                     │
│ • detalle_ventas                                                             │
│                                                                              │
│ Relaciones:                                                                  │
│   - 1:N entre clientes y ventas                                              │
│   - 1:N entre ventas y detalle_ventas                                        │
│   - 1:N entre productos y detalle_ventas                                     │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ ⚙️ METODOLOGÍA                                                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. ETL (Extracción, Transformación, Carga)                                   │
│    • Lectura de tablas desde directorio `db/`                                │
│                                                                              │
│ 2. Limpieza y Normalización                                                  │
│    • Procesamiento individual por tabla                                      │
│                                                                              │
│ 3. Consolidación Relacional                                                  │
│    • Integración de tablas con validación de integridad                      │
│                                                                              │
│ 4. Análisis Descriptivo                                                      │
│    • Estadísticas, visualizaciones y transformaciones                        │
│                                                                              │
│ 5. Generación de Datasets Derivados                                          │
│    • Vistas a nivel ticket y cliente para modelado ML                        │
└──────────────────────────────────────────────────────────────────────────────┘

---

## 2. Sprint 1 (Demo 1 asincrónica)

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📝 TEMA, PROBLEMA Y SOLUCIÓN                                                 │
├──────────────────────────────────────────────────────────────────────────────┤
│ Gestión y análisis de ventas minoristas para detectar patrones y             │
│ optimizar inventario.                                                        │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📂 DATASET DE REFERENCIA                                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Datos educativos provistos por Guayerd e IBM                                 │
│                                                                              │
│ Tablas:                                                                      │
│   • clientes                                                                 │
│   • productos                                                                │
│   • ventas                                                                   │
│   • detalle_ventas                                                           │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🗃️ ESTRUCTURA POR TABLA                                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Clientes:                                                                    │
│   • id_cliente, nombre, email, ciudad, fecha_alta                            │
│                                                                              │
│ Productos:                                                                   │
│   • id_producto, nombre_producto, categoria, precio_unitario                 │
│                                                                              │
│ Ventas:                                                                      │
│   • id_venta, fecha, id_cliente, nombre_cliente, email, medio_pago           │
│                                                                              │
│ Detalle_ventas:                                                              │
│   • id_venta, id_producto, nombre_producto, cantidad,                        │
│     precio_unitario, importe                                                 │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📊 ESCALAS DE MEDICIÓN                                                       │
├──────────────────────────────────────────────────────────────────────────────┤
│ Las variables del dataset utilizan diferentes escalas según su naturaleza:  │
│                                                                              │
│   • Nominal (categóricas sin orden)                                          │
│   • Ordinal (categóricas con orden)                                          │
│   • Intervalo (numéricas con distancias)                                     │
│   • Razón (numéricas con cero absoluto)                                      │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🤖 SUGERENCIAS CON IA                                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│ • Generar consultas y visualizaciones automatizadas                          │
│ • Automatizar limpieza y detección de anomalías                              │
│ • Optimizar workflows de análisis exploratorio                               │
└──────────────────────────────────────────────────────────────────────────────┘

---

## 3. Sprint 2 (Demo 2 sincrónica)

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🎯 CONTEXTO Y ALCANCE                                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│ Implementación ETL y análisis descriptivo avanzado sobre 4 tablas.           │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📋 TEMA, PROBLEMA Y SOLUCIÓN (Continuidad)                                   │
├──────────────────────────────────────────────────────────────────────────────┤
│ Consolidar información para reportes, productos más vendidos y               │
│ comportamiento de compra.                                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🗄️ DATASET DE REFERENCIA Y ESTRUCTURA                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│ Mismas fuentes del Sprint 1                                                  │
│                                                                              │
│ Características:                                                             │
│   • Relaciones 1:N validadas                                                 │
│   • Tipificación coherente entre tablas                                      │
│   • Integridad referencial completa                                          │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🧹 ETAPA 1 - Limpieza y Normalización de Datos                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ Procesos aplicados:                                                          │
│   • Conversión de fechas a datetime                                          │
│   • Normalización de texto (mayúsculas, espacios)                            │
│   • Conversión de categorías a tipos apropiados                              │
│   • Control de duplicados y validación de claves                             │
│                                                                              │
│ Resultado:                                                                   │
│   ✅ 0 nulos detectados                                                      │
│   ✅ 0 duplicados encontrados                                                │
│   ✅ Integridad referencial 100%                                             │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📊 ETAPA 2 - Análisis Descriptivo y Visualización Integral                   │
├──────────────────────────────────────────────────────────────────────────────┤
│ Base Consolidada:                                                            │
│   • Dimensión:              343 filas × 21 columnas                          │
│   • Período:                Enero - Junio 2024                               │
│                                                                              │
│ Estadísticas por Variable:                                                   │
│                                                                              │
│ Cantidad:                                                                    │
│   • Media:                  2.96 unidades                                    │
│   • Mediana:                3 unidades                                       │
│   • Rango:                  1 - 5 unidades                                   │
│   • CV:                     46%                                              │
│                                                                              │
│ Precio Unitario:                                                             │
│   • Media:                  $ 2,654.50                                       │
│   • Mediana:                $ 2,512.00                                       │
│   • Rango:                  $ 272 - $ 4,982                                  │
│   • CV:                     49%                                              │
│                                                                              │
│ Importe:                                                                     │
│   • Media:                  $ 7,730.08                                       │
│   • Mediana:                $ 6,702.00                                       │
│   • Rango:                  $ 272 - $ 24,865                                 │
│   • CV:                     68%                                              │
│                                                                              │
│ Transformaciones Aplicadas:                                                  │
│   • Z-score (importe_std)                                                    │
│   • log1p(importe)                                                           │
│                                                                              │
│ Correlaciones Principales:                                                   │
│   • importe vs precio_unitario:     0.68                                     │
│   • importe vs cantidad:            0.60                                     │
│                                                                              │
│ Outliers:                                                                    │
│   • Concentrados en tickets de 5 unidades (método IQR)                       │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📦 ETAPA 3 - Procesamiento de PRODUCTOS y VENTAS                             │
├──────────────────────────────────────────────────────────────────────────────┤
│ Productos:                                                                   │
│   • Total SKUs:             100 productos                                    │
│   • Calidad:                Sin nulos ni duplicados                          │
│   • Rango de precios:       $ 272 - $ 4,982                                  │
│   • Categorías:             Balanceadas                                      │
│                                                                              │
│ Ventas:                                                                      │
│   • Total cabeceras:        120 transacciones                                │
│   • Medios de pago:         Normalizados con one-hot encoding                │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🔗 ETAPA 4 - Consolidación e Integración                                     │
├──────────────────────────────────────────────────────────────────────────────┤
│ Exportaciones Generadas:                                                     │
│   • Base_Final_Aurelion.csv           343 × 21 columnas                      │
│   • base_final_ML_clientes.csv        67 × 18 columnas                       │
│   • df_ticket_ml                      (generado en notebook)                 │
│                                                                              │
│ Validaciones Finales:                                                        │
│   ✅ Sin PII sensible en datasets ML                                        │
│   ✅ Integridad referencial 100%                                            │
│   ✅ Formatos listos para BI y ML                                           │
└──────────────────────────────────────────────────────────────────────────────┘

---

## 4. Sprint 3 (Demo 3 - Machine Learning y modelado predictivo)

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🎯 OBJETIVO Y METODOLOGÍA                                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│ Objetivos:                                                                   │
│   • Segmentar clientes en grupos homógeneos                                  │
│   • Predecir churn (riesgo de pérdida de clientes)                           │
│   • Estimar valor histórico del cliente                                      │
│                                                                              │
│ Principios:                                                                  │
│   • Evitar data leakage en todas las etapas                                  │
│   • Exportar artefactos listos para BI/CRM                                   │
│   • Documentar y versionar todos los modelos                                 │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 📊 PARÁMETROS Y ARTEFACTOS EXPORTADOS                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│ Dataset ML:              base_final_ML_clientes.csv                          │
│   • Columnas:             67 clientes × 18 columnas                          │
│   • Features numéricas:   16 variables predictoras                           │
│   • Otras:                id_cliente + ciudad                                │
│                                                                              │
│ Artefactos Generados:                                                        │
│   • Modelos y scalers:    .pkl (binarios serializados)                       │
│   • Métricas:             .json (resultados de evaluación)                   │
│   • Feature importance:   .csv (ranking de variables)                        │
│   • Segmentos y riesgos:  .csv (clusters, alto riesgo)                       │
│   • Predicciones:         .csv (valores estimados)                           │
└──────────────────────────────────────────────────────────────────────────────┘

### 4.3 Indicadores y métricas de modelos

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🔹 SEGMENTACIÓN DE CLIENTES (K-Means)                                        │
├──────────────────────────────────────────────────────────────────────────────┤
│ Pipeline:                                                                    │
│   StandardScaler → KMeans(K=3, n_init=20, max_iter=500)                      │
│                                                                              │
│ Métricas de Calidad:                                                         │
│   • Silhouette Score:             0.1985                                     │
│   • Calinski-Harabasz Index:      16.49                                      │
│   • Davies-Bouldin Index:         1.65                                       │
│   • Inertia:                      707.51                                     │
│                                                                              │
│ Distribución de Clientes:                                                    │
│   • Cluster 0:                    19 clientes                                │
│   • Cluster 1:                    19 clientes                                │
│   • Cluster 2:                    29 clientes                                │
├──────────────────────────────────────────────────────────────────────────────┤
│ Perfiles Promedio por Cluster (ver perfiles_segmentos.csv):                  │
│                                                                              │
│ Cluster 0 - Alto valor, baja frecuencia:                                     │
│   • Ventas promedio:              1.16 transacciones                         │
│   • Importe total:                $ 41,046                                   │
│   • Ticket promedio:              $ 35,932                                   │
│   • Medios de pago:               60.5% efectivo, 18.4% transferencia        │
│   • Líneas/venta:                 3.97                                       │
│   • Cantidad promedio:            13.34 unidades                             │
│                                                                              │
│ Cluster 1 - Alto valor, alta frecuencia:                                     │
│   • Ventas promedio:              2.74 transacciones                         │
│   • Importe total:                $ 63,497                                   │
│   • Ticket promedio:              $ 24,468                                   │
│   • Medios de pago:               42.7% efectivo, 16.3% tarjeta,             │
│                                    27.6% QR                                  │
│   • Líneas/venta:                 3.00                                       │
│   • Cantidad promedio:            8.61 unidades                              │
│                                                                              │
│ Cluster 2 - Bajo valor:                                                      │
│   • Ventas promedio:              1.59 transacciones                         │
│   • Importe total:                $ 22,934                                   │
│   • Ticket promedio:              $ 14,733                                   │
│   • Medios de pago:               32.8% tarjeta, 35.6% transferencia         │
│   • Líneas/venta:                 2.32                                       │
│   • Cantidad promedio:            6.34 unidades                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 🔺 PREDICCIÓN DE CHURN (Random Forest Classifier)                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Variable Target:                                                             │
│   • Definición:                 recency > 60 días                            │
│   • Distribución base:          35 positivos / 32 negativos                  │
│   • Churn rate:                 52.2%                                        │
│                                                                              │
│ Preprocesamiento:                                                            │
│   • Train/Test split                                                         │
│   • Escalado con StandardScaler                                              │
│   • SMOTE para balanceo de clases                                            │
│                                                                              │
│ Métricas de Desempeño:                                                       │
│   • Accuracy Train:             98.11%                                       │
│   • Accuracy Test:              57.14%                                       │
│   • ROC-AUC:                    0.5714                                       │
│   • Umbral óptimo:              0.3790                                       │
│                                                                              │
│ Clientes de Alto Riesgo:                                                     │
│   • Total detectados:           20 clientes                                  │
│   • Umbral de acción:           0.70 (70% probabilidad)                      │
│                                                                              │
│ Top 5 Variables (feature_importance_churn.csv):                              │
│   1. importe_total_cliente        0.171 (17.1%)                              │
│   2. ticket_max                   0.141 (14.1%)                              │
│   3. ventas_por_mes               0.110 (11.0%)                              │
│   4. antiguedad_cliente_dias      0.106 (10.6%)                              │
│   5. ticket_promedio              0.081 (8.1%)                               │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ 💰 PREDICCIÓN DE VALOR DEL CLIENTE (Random Forest Regressor)                │
├──────────────────────────────────────────────────────────────────────────────┤
│ Variable Target:                                                             │
│   • importe_total_cliente (valor histórico acumulado)                        │
│                                                                              │
│ Métricas de Error:                                                           │
│   • MAE Train/Test:             $ 3,882.50 / $ 7,552.50                      │
│   • RMSE Train/Test:            $ 6,869.72 / $ 10,086.19                     │
│   • R² Train/Test:               0.9242 / 0.6998                             │
│                                                                              │
│ Estadísticas del Target:                                                     │
│   • Media:                      $ 39,573                                     │
│   • Mediana:                    $ 34,326                                     │
│   • Desviación estándar:        $ 23,945                                     │
│                                                                              │
│ Top 5 Variables (feature_importance_customer_value.csv):                     │
│   1. ticket_max                   0.733 (73.3%)                              │
│   2. ventas_por_mes               0.125 (12.5%)                              │
│   3. n_ventas                     0.033 (3.3%)                               │
│   4. desvio_ticket                0.031 (3.1%)                               │
│   5. ticket_promedio              0.016 (1.6%)                               │
└──────────────────────────────────────────────────────────────────────────────┘

### 4.4 Recomendaciones y consideraciones tecnicas
- Churn: mantener exclusion de recency en features; considerar definir churn futuro (no compra en 90 dias) y calibrar threshold segun precision/recall.
- Valor: comunicar como "Customer Value Prediction" (no CLV formal); cruzar con segmentos para priorizar campañas.
- Clustering: integrar segmentos en CRM/BI; monitorear drift y recalcular mensualmente.

### 4.5 Proximos pasos
- Automatizar pipeline (ETL + reentrenamiento).
- Dashboard con segmentos, probabilidades de churn y valor estimado.
- A/B testing de campañas guiadas por modelos.

### 4.6 Trazabilidad y control de calidad de datos
- Integridad referencial validada; 0 nulos y 0 duplicados en claves; tipos correctos.

### 4.7 Seleccion de hiperparametros y validacion
- KMeans: K=3 (elbow + silhouette).
- RandomForest: 100 arboles, max_depth=10, min_samples_split=5, min_samples_leaf=2, random_state=42 para churn y valor.

### 4.8 Limitaciones y advertencias
- Silhouette moderado (0.1985) sugiere segmentos utilis pero con solapamiento.
- ROC-AUC de churn modesto (0.57) requiere iteraciones adicionales y mejor target.

### 4.9 Etica, privacidad y buenas practicas
- Datasets ML sin PII sensible; documentar supresion de emails/nombres para despliegue.
- Evitar data leakage (recency no usada como feature).

### 4.10 Mantenimiento y actualizacion de modelos
- Reentrenar trimestral o ante drift significativo; versionar artefactos en `modelos/`.

---

## 5. Referencias y Bibliografia
- Guayerd e IBM materiales educativos del curso de Data Science aplicado a retail.

---

## 6. Glosario de Terminos
- CV: Coeficiente de variacion.
- ROC-AUC: Area bajo la curva ROC.
- SMOTE: Synthetic Minority Over-sampling Technique.
- R2: Coeficiente de determinacion.
- Silhouette: medida de separacion de clusters.

---

## Mapa de artefactos (carpeta `modelos/`)
- `kmeans_segmentacion.pkl`, `scaler_clustering.pkl`, `pca_clustering.pkl`
- `random_forest_churn.pkl`, `scaler_churn.pkl`, `feature_importance_churn.csv`, `metricas_churn.json`, `clientes_alto_riesgo.csv`
- `random_forest_customer_value.pkl`, `scaler_customer_value.pkl`, `feature_importance_customer_value.csv`, `metricas_customer_value.json`, `predicciones_customer_value.csv`
- `clientes_con_clusters.csv`, `perfiles_segmentos.csv`

---

## Outputs de artefactos (muestras)

### Métricas del Modelo de Churn

```python
# Métricas de Churn (modelos/metricas_churn.json)
import json, pathlib
p = pathlib.Path("modelos/metricas_churn.json")
print(p.read_text(encoding="utf-8"))
```

```output
┌──────────────────────────────────────────────────────────────────────────────┐
│ PRECISIÓN DEL MODELO (TRAINING)                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Accuracy (Train):                                   98.11%                   │
│ Accuracy (Test):                                    57.14%                   │
├──────────────────────────────────────────────────────────────────────────────┤
│ CURVA ROC                                                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│ ROC AUC Score:                                      0.5714                   │
│ Umbral Óptimo:                                      0.3790                   │
├──────────────────────────────────────────────────────────────────────────────┤
│ CLIENTES DE ALTO RIESGO                                                      │
├──────────────────────────────────────────────────────────────────────────────┤
│ Clientes Detectados:                                20 clientes              │
│ Umbral de Riesgo:                                   0.70 (70%)               │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Importancia de Features (Churn)

```python
# Importancias de features (top 10 de modelos/feature_importance_churn.csv)
import pathlib
rows = pathlib.Path("modelos/feature_importance_churn.csv").read_text(encoding="utf-8").splitlines()
print("\n".join(rows[:11]))
```

```output
┌──────────────────────────────────────────────────────────────────────────────┐
│ TOP 10 FEATURES MÁS IMPORTANTES                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. Importe Total Cliente               17.07%  █████████████████            │
│  2. Ticket Máximo                        14.05%  ██████████████              │
│  3. Ventas por Mes                      11.02%  ███████████                  │
│  4. Antigüedad Cliente (días)           10.59%  ███████████                  │
│  5. Ticket Promedio                      8.10%  ████████                     │
│  6. Ticket Mínimo                         7.00%  ███████                     │
│  7. Cantidad Promedio por Venta          6.75%  ███████                      │
│  8. Desvío Ticket                        6.31%  ██████                       │
│  9. Líneas Promedio por Venta            5.74%  ██████                       │
│ 10. % Ventas Transferencia               5.02%  █████                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Métricas del Modelo de Valor del Cliente

```python
# Métricas de Valor del Cliente (modelos/metricas_customer_value.json)
import pathlib
print(pathlib.Path("modelos/metricas_customer_value.json").read_text(encoding="utf-8"))
```

```output
┌──────────────────────────────────────────────────────────────────────────────┐
│ ERROR ABSOLUTO MEDIO (MAE)                                                   │
├──────────────────────────────────────────────────────────────────────────────┤
│ MAE Training:                                       $ 3,882.50               │
│ MAE Test:                                           $ 7,552.50               │
├──────────────────────────────────────────────────────────────────────────────┤
│ RAÍZ DEL ERROR CUADRÁTICO MEDIO (RMSE)                                       │
├──────────────────────────────────────────────────────────────────────────────┤
│ RMSE Training:                                      $ 6,869.72               │
│ RMSE Test:                                          $ 10,086.19              │
├──────────────────────────────────────────────────────────────────────────────┤
│ COEFICIENTE DE DETERMINACIÓN (R²)                                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ R² Training:                                        0.9242 (92.42%)          │
│ R² Test:                                            0.6998 (69.98%)          │
├──────────────────────────────────────────────────────────────────────────────┤
│ ESTADÍSTICAS DESCRIPTIVAS                                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│ Media Importe Total:                                $ 39,573.39              │
│ Mediana Importe Total:                              $ 34,326.00              │
│ Desviación Estándar:                                $ 23,945.21              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Segmentación de Clientes (Clusters)

```python
# Muestra de clientes con clusters (modelos/clientes_con_clusters.csv)
import pathlib
rows = pathlib.Path("modelos/clientes_con_clusters.csv").read_text(encoding="utf-8").splitlines()
print("\n".join(rows[:11]))
```

```output
┌──────────────────────────────────────────────────────────────────────────────┐
│ CLIENTE #1                                           Segmento A              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Ubicación:          Carlos Paz                                               │
│ Cantidad Ventas:    2 ventas                                                 │
│ Importe Total:      $ 72,448.00                                              │
│ Ticket Promedio:    $ 36,224.00                                              │
│ Ticket Máximo:      $ 36,413.00                                              │
│ Antigüedad:         544 días (18.1 meses)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ CLIENTE #2                                           Segmento C              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Ubicación:          Carlos Paz                                               │
│ Cantidad Ventas:    1 venta                                                  │
│ Importe Total:      $ 22,150.00                                              │
│ Ticket Promedio:    $ 22,150.00                                              │
│ Ticket Máximo:      $ 22,150.00                                              │
│ Antigüedad:         543 días (18.1 meses)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ CLIENTE #3                                           Segmento A              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Ubicación:          Río Cuarto                                               │
│ Cantidad Ventas:    1 venta                                                  │
│ Importe Total:      $ 33,310.00                                              │
│ Ticket Promedio:    $ 33,310.00                                              │
│ Ticket Máximo:      $ 33,310.00                                              │
│ Antigüedad:         542 días (18.1 meses)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ CLIENTE #5                                           Segmento B              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Ubicación:          Córdoba                                                  │
│ Cantidad Ventas:    4 ventas                                                 │
│ Importe Total:      $ 132,158.00                                             │
│ Ticket Promedio:    $ 33,039.50                                              │
│ Ticket Máximo:      $ 45,142.00                                              │
│ Antigüedad:         540 días (18.0 meses)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ CLIENTE #6                                           Segmento B              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Ubicación:          Villa María                                              │
│ Cantidad Ventas:    2 ventas                                                 │
│ Importe Total:      $ 48,878.00                                              │
│ Ticket Promedio:    $ 24,439.00                                              │
│ Ticket Máximo:      $ 37,256.00                                              │
│ Antigüedad:         539 días (18.0 meses)                                    │
└──────────────────────────────────────────────────────────────────────────────┘

Nota: Mostrando primeras 5 filas con datos principales organizados por cliente
```
