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

| Componente                              | Resultado / Metrica clave                                    |
|-----------------------------------------|--------------------------------------------------------------|
| Base transaccional `Base_Final_Aurelion.csv` | 343 filas x 21 columnas, 67 clientes, 120 ventas, 95 productos; 0 nulos y 0 duplicados. |
| Medios de pago (one-hot)                | Efectivo 32.4%, QR 26.5%, Tarjeta 20.1%, Transferencia 21.0%. |
| Mix de categorias                       | Alimentos 97.1%, Limpieza 2.9%.                              |
| Dataset ML `base_final_ML_clientes.csv` | 67 clientes x 18 columnas (16 features numericas + id + ciudad). |
| Clustering K-Means (K=3)                | Silhouette 0.1985; Calinski-Harabasz 16.49; Davies-Bouldin 1.65; Inertia 707.51; clusters 19 / 19 / 29. |
| Modelo Churn (Random Forest)            | Accuracy train 0.9811 / test 0.5714; ROC-AUC 0.5714; umbral optimo 0.3790; 20 clientes en alto riesgo (umbral accion 0.70). |
| Modelo Valor Cliente (Random Forest Regressor) | MAE 3,882.5 / 7,552.5; RMSE 6,869.7 / 10,086.2; R2 0.9242 / 0.6998; media target 39,573; mediana 34,326 ARS. |
| Artefactos exportados                  | Modelos y scalers (.pkl), metricas (.json), feature importance (.csv), segmentos y riesgos (.csv), predicciones (.csv). |

---

## Como ejecutar el visor

Requisitos: Python 3.10+.

1) Abrir una consola con soporte UTF-8 (en Windows: `chcp 65001` o usar Windows Terminal/VS Code).
2) Ejecutar desde la carpeta del proyecto:

```
python programa.py
```

- Para modo demo sin entrada interactiva: `python programa.py --demo`
- El archivo `DOCUMENTACION.md` debe estar en la misma carpeta que `programa.py`.

---

## 1. Vision general del proyecto

Objetivo: transformar datos de ventas minoristas en insights accionables y bases listas para BI/ML.

Tablas fuente: `clientes`, `productos`, `ventas`, `detalle_ventas` (relaciones 1:N entre clientes-ventas y ventas-detalle, productos-detalle).

Metodologia: ETL (lectura desde `db/`), limpieza y normalizacion por tabla, consolidacion relacional, analisis descriptivo y generacion de datasets derivados (ticket y cliente) para modelado.

---

## 2. Sprint 1 (Demo 1 asincronica)

### 2.1 Tema, problema y solucion
- Gestion y analisis de ventas minoristas para detectar patrones y optimizar inventario.

### 2.2 Dataset de referencia
- Datos educativos provistos por Guayerd e IBM: clientes, productos, ventas, detalle_ventas.

### 2.3 Estructura por tabla
- Clientes: id_cliente, nombre, email, ciudad, fecha_alta.
- Productos: id_producto, nombre_producto, categoria, precio_unitario.
- Ventas: id_venta, fecha, id_cliente, nombre_cliente, email, medio_pago.
- Detalle_ventas: id_venta, id_producto, nombre_producto, cantidad, precio_unitario, importe.

### 2.4 Escalas de medicion
- Nominal, ordinal, intervalo, razon, segun variable.

### 2.5 Sugerencias con IA
- Generar consultas y visualizaciones, automatizar limpieza y deteccion de anomalías.

---

## 3. Sprint 2 (Demo 2 sincronica)

### 3.1 Contexto y alcance
- Implementacion ETL y analisis descriptivo avanzado sobre 4 tablas.

### 3.2 Tema, problema y solucion (continuidad)
- Consolidar informacion para reportes, productos mas vendidos y comportamiento de compra.

### 3.3 Dataset de referencia y estructura (resumen)
- Mismas fuentes del Sprint 1; relaciones 1:N y tipificacion coherente.

### 3.4 Etapa 1 - Limpieza y normalizacion de datos
- Conversion de fechas a datetime, normalizacion de texto, conversion de categorias, control de duplicados y claves.
- Resultado: 0 nulos, 0 duplicados, integridad referencial completa.

### 3.5 Etapa 2 - Analisis descriptivo y visualizacion integral
- Base consolidada: 343 filas x 21 columnas (enero-junio 2024).
- Estadisticas (detalle):
  - cantidad: media 2.96, mediana 3, min 1, max 5, CV 46%.
  - precio_unitario: media 2,654.50, mediana 2,512, min 272, max 4,982, CV 49%.
  - importe: media 7,730.08, mediana 6,702, min 272, max 24,865, CV 68%.
- Transformaciones: Z-score (`importe_std`), log1p(importe), correlacion importe vs precio_unitario 0.68, importe vs cantidad 0.60.
- Outliers (IQR) concentrados en tickets de 5 unidades.

### 3.6 Etapa 3 - Procesamiento de PRODUCTOS y VENTAS
- Productos: 100 SKUs, sin nulos ni duplicados; precios min 272, max 4,982; categorias balanceadas.
- Ventas: 120 cabeceras; medios de pago normalizados con one-hot.

### 3.7 Etapa 4 - Consolidacion e integracion
- Exportaciones: `Base_Final_Aurelion.csv` (343x21), `base_final_ML_clientes.csv` (67x18), `df_ticket_ml` generado en notebook.
- Validaciones finales: sin PII sensible en datasets ML, integridad referencial 100%.

---

## 4. Sprint 3 (Demo 3 - Machine Learning y modelado predictivo)

### 4.1 Objetivo y metodologia
- Segmentar clientes, predecir churn y estimar valor historico; evitar data leakage y exportar artefactos listos para BI/CRM.

### 4.2 Parametros y artefactos exportados
- Dataset ML: `base_final_ML_clientes.csv` con 16 features numericas mas id y ciudad.
- Artefactos: modelos y scalers (.pkl), metricas (.json), feature importance (.csv), segmentos y riesgos (.csv), predicciones (.csv).

### 4.3 Indicadores y metricas de modelos

#### 4.3.1 Segmentacion de clientes (K-Means)
- Pipeline: StandardScaler -> KMeans (K=3, n_init=20, max_iter=500).
- Metricas: Silhouette 0.1985; Calinski-Harabasz 16.49; Davies-Bouldin 1.65; Inertia 707.51.
- Distribucion: 19 / 19 / 29 clientes.
- Perfiles medios (perfiles_segmentos.csv):
  - Cluster 0: n_ventas 1.16; importe_total 41,046; ticket_promedio 35,932; efectivo 60.5%; transferencia 18.4%; lineas/venta 3.97; cantidad_promedio 13.34.
  - Cluster 1: n_ventas 2.74; importe_total 63,497; ticket_promedio 24,468; efectivo 42.7%; tarjeta 16.3%; QR 27.6%; lineas/venta 3.00; cantidad_promedio 8.61.
  - Cluster 2: n_ventas 1.59; importe_total 22,934; ticket_promedio 14,733; tarjeta 32.8%; transferencia 35.6%; lineas/venta 2.32; cantidad_promedio 6.34.

#### 4.3.2 Prediccion de churn (Random Forest)
- Target: recency > 60 dias (base: 35 positivos / 32 negativos; churn rate 52.2%).
- Preproceso: split, escalado, SMOTE.
- Metricas: accuracy train 0.9811 / test 0.5714; ROC-AUC 0.5714; umbral optimo 0.3790; 20 clientes alto riesgo con umbral 0.70.
- Top 5 variables (feature_importance_churn.csv): importe_total_cliente 0.171; ticket_max 0.141; ventas_por_mes 0.110; antiguedad_cliente_dias 0.106; ticket_promedio 0.081.

#### 4.3.3 Prediccion de valor del cliente (Random Forest Regressor)
- Target: importe_total_cliente (valor historico).
- Metricas: MAE 3,882.5 / 7,552.5; RMSE 6,869.7 / 10,086.2; R2 0.9242 / 0.6998.
- Top 5 variables (feature_importance_customer_value.csv): ticket_max 0.733; ventas_por_mes 0.125; n_ventas 0.033; desvio_ticket 0.031; ticket_promedio 0.016.
- Estadistica target: media 39,573; mediana 34,326; std 23,945.

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
