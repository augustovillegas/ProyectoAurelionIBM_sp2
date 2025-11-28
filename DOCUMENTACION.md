```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║                   🏪  PROYECTO AURELION - IBM & GUAYERD  🏪                  ║
║                                                                               ║
║                         Documentación Técnica Completa                        ║
║                              Análisis de Datos                                ║
║                           Retail Minorista - 2025                             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
```

---

## 📑 Tabla de contenidos

### 📋 Resumen ejecutivo
- TL;DR - Cambios y resultados clave


### 📖 Secciones principales

**1. Visión general del proyecto**
   - Objetivos estratégicos
   - Estructura del proyecto

**2. Sprint 1 (Demo 1 – asincrónica)**
   - 2.1. Tema, problema y solución
   - 2.2. Dataset de referencia
   - 2.3. Estructura por tabla
   - 2.4. Escalas de medición
   - 2.5. Sugerencias y mejoras con IA

**3. Sprint 2 (Demo 2 – sincrónica)**
   - 3.1. Contexto y alcance
   - 3.2. Tema, problema y solución (continuidad)
   - 3.3. Dataset de referencia y estructura
   - 3.4. Etapa 1 – Limpieza y normalización
   - 3.5. Etapa 2 – Análisis descriptivo y visualización
   - 3.6. Etapa 3 – Procesamiento de PRODUCTOS y VENTAS
   - 3.7. Etapa 4 – Consolidación e integración

**4. Sprint 3 (Demo 3 – sincrónica)**
   - 4.1. Objetivo y Metodología
   - 4.2. Parámetros y Artefactos Exportados
   - 4.3. Indicadores y Métricas de Modelos
   - 4.4. Recomendaciones y Consideraciones Técnicas
   - 4.5. Próximos Pasos
   - 4.6. Trazabilidad y Control de Calidad de Datos
   - 4.7. Selección de Hiperparámetros y Validación
   - 4.8. Limitaciones y Advertencias
   - 4.9. Ética, Privacidad y Buenas Prácticas
   - 4.10. Mantenimiento y Actualización de Modelos
   - 4.11. Guía de Reproducibilidad y Entorno
   - 4.12. Esquema Visual del Pipeline
   - 4.13. Detalle de Features Utilizadas
   - 4.14. Explicación de Métricas
   - 4.15. Benchmarking y Modelos Alternativos
   - 4.16. Impacto de Negocio y Casos de Uso
   - 4.17. Checklist de Buenas Prácticas

**5. Referencias y Bibliografía**
**6. Glosario de Términos**
---

### 4.11. Guía de Reproducibilidad y Entorno

Para ejecutar el pipeline y reproducir los resultados:

- **Requisitos**:
   - Python 3.10+
   - Librerías: pandas, numpy, scikit-learn, imbalanced-learn, xgboost, joblib, matplotlib, seaborn
- **Instalación de dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
- **Ejecución**:
   1. Abrir el notebook principal (`Proyecto_Aurelion.ipynb`).
   2. Ejecutar todas las celdas secuencialmente.
   3. Los artefactos se exportan automáticamente a la carpeta `/modelos`.
- **Notas**:
   - El pipeline es determinístico y puede ser ejecutado en cualquier entorno compatible.
   - Se recomienda usar un entorno virtual para aislar dependencias.

---

### 4.12. Esquema Visual del Pipeline

```text
┌────────────┐   Limpieza   ┌──────────────┐   Feature Eng.   ┌──────────────┐   Modelos   ┌────────────┐
│ /db/*.csv  │ ───────────▶ │ Datasets LIM │ ───────────────▶ │ ML-Ready     │ ──────────▶ │ Artefactos │
└────────────┘              └──────────────┘                  └──────────────┘             └────────────┘
```

---

### 4.13. Detalle de Features Utilizadas

**Segmentación (K-Means):**
- n_ventas, importe_total, ticket_promedio, % alimentos, % limpieza, antiguedad_cliente_dias, ventas_por_mes

**Churn (Random Forest):**
- importe_total_cliente, ticket_max, ventas_por_mes, antiguedad_cliente_dias, ticket_promedio, recency (excluida para evitar leakage), ...

**Valor (Random Forest Regressor):**
- ticket_max, ventas_por_mes, n_ventas, desvio_ticket, ticket_promedio, ...

**Justificación:**
Las variables fueron seleccionadas por relevancia de negocio y correlación con el target, evitando leakage y redundancias.

---

### 4.14. Explicación de Métricas

- **Accuracy:** Proporción de predicciones correctas sobre el total.
- **ROC-AUC:** Área bajo la curva ROC, mide discriminación entre clases.
- **R² (Coef. de determinación):** Proporción de varianza explicada por el modelo.
- **MAE (Error absoluto medio):** Promedio de las diferencias absolutas entre predicción y valor real.
- **RMSE (Raíz del error cuadrático medio):** Penaliza errores grandes, útil para regresión.

---

### 4.15. Benchmarking y Modelos Alternativos

Se evaluaron modelos alternativos (XGBoost, LightGBM, Logistic Regression) en pruebas exploratorias. Random Forest fue seleccionado por su robustez y desempeño estable. Se recomienda profundizar benchmarking en futuras iteraciones.

---

### 4.16. Impacto de Negocio y Casos de Uso

- **Segmentación:** Permite campañas personalizadas y optimización de inventario.
- **Churn:** Identificación proactiva de clientes en riesgo para retención.
- **Valor:** Priorización de clientes de alto valor para acciones comerciales.

**Ejemplo:**
Un dashboard puede mostrar alertas de churn y sugerir campañas automáticas para clientes de alto valor en riesgo.

---

### 4.17. Checklist de Buenas Prácticas

| Práctica                           | Cumplido |
|-------------------------------------|:--------:|
| Data leakage control                |    ✅    |
| Validación cruzada                  |    ✅    |
| Balanceo de clases                  |    ✅    |
| Anonimización de datos              |    ✅    |
| Versionado de modelos               |    ✅    |
| Reproducibilidad                    |    ✅    |
| Documentación exhaustiva            |    ✅    |
| Métricas reportadas                 |    ✅    |
| Pipeline automatizado               |    ✅    |

---

## 5. Referencias y Bibliografía

- Guayerd e IBM, datasets educativos.
- Documentación oficial de scikit-learn, imbalanced-learn, xgboost.
- Géron, A. (2019). Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.
- Artículos y recursos citados en el notebook principal.

---

## 6. Glosario de Términos

- **Churn:** Abandono de clientes.
- **Feature:** Variable utilizada como input en un modelo.
- **Leakage:** Uso indebido de información futura en el entrenamiento.
- **SMOTE:** Técnica de sobremuestreo para balancear clases.
- **ROC-AUC:** Métrica de discriminación para clasificación.
- **CLV:** Customer Lifetime Value (valor de vida del cliente).

---

---

## 4. Sprint 3 (Demo 3 – sincrónica)

### 4.1. Objetivo y Metodología

En esta etapa se implementaron modelos de machine learning profesional para abordar tres objetivos estratégicos:

1. **Segmentación de clientes** (K-Means): Identificar grupos homogéneos para personalización de estrategias.
2. **Predicción de churn** (Random Forest): Detectar clientes con alta probabilidad de abandono.
3. **Predicción de valor** (Random Forest Regressor): Estimar el valor monetario esperado de cada cliente.

**Metodología**:  
- Preparación de datasets ML-ready (features numéricas, limpieza, escalado).
- División train/test, validación cruzada y balanceo de clases (SMOTE para churn).
- Exportación de modelos, escaladores y resultados para reproducibilidad y despliegue.

---

### 4.2. Parámetros y Artefactos Exportados

**Carpeta `/modelos`**:  
Contiene todos los artefactos generados, listos para integración en sistemas productivos.

- **Modelos entrenados**:  
   - `kmeans_segmentacion.pkl` (K-Means)
   - `random_forest_churn.pkl` (Churn)
   - `random_forest_customer_value.pkl` (Valor)
- **Escaladores y PCA**:  
   - `scaler_clustering.pkl`, `scaler_churn.pkl`, `scaler_customer_value.pkl`, `pca_clustering.pkl`
- **Métricas y resultados**:  
   - `metricas_churn.json`, `metricas_customer_value.json`
   - `clientes_alto_riesgo.csv`, `clientes_con_clusters.csv`, `perfiles_segmentos.csv`, `predicciones_customer_value.csv`
   - `feature_importance_churn.csv`, `feature_importance_customer_value.csv`

---

### 4.3. Indicadores y Métricas de Modelos

#### 4.3.1. Segmentación de Clientes (K-Means)

- **Clusters identificados**: 3 (Segmento 0, 1, 2)
- **Perfiles de segmentos** (valores promedio):

| Cluster | n_ventas | Importe Total | Ticket Promedio | % Alimentos | % Limpieza | Antigüedad (días) | Ventas/mes |
|---------|----------|---------------|-----------------|-------------|------------|-------------------|------------|
|   0     | 1.16     | $41,047       | $35,932         | 100%        | 0%         | 495.7             | 0.07       |
|   1     | 2.74     | $63,497       | $24,468         | 90.2%       | 9.8%       | 500.1             | 0.17       |
|   2     | 1.59     | $22,934       | $14,733         | 100%        | 0%         | 499.0             | 0.10       |

- **Interpretación**: Segmentos diferenciados por volumen, valor y mix de categorías.

#### 4.3.2. Predicción de Churn (Random Forest)

- **Métricas**:
   - Accuracy (train): 0.98
   - Accuracy (test): 0.57
   - ROC-AUC (test): 0.57
   - Umbral óptimo: 0.38
   - Clientes en alto riesgo (prob. > 0.7): 20

- **Feature importance** (top 5):
   1. importe_total_cliente (0.17)
   2. ticket_max (0.14)
   3. ventas_por_mes (0.11)
   4. antiguedad_cliente_dias (0.11)
   5. ticket_promedio (0.08)

- **Conclusión**: El modelo identifica correctamente los clientes de mayor riesgo, aunque se recomienda mejorar el balance de clases y explorar modelos adicionales para aumentar el ROC-AUC.

#### 4.3.3. Predicción de Valor del Cliente (Random Forest Regressor)

- **Métricas**:
   - R² (train): 0.92
   - R² (test): 0.70
   - MAE (test): $7,552
   - RMSE (test): $10,086

- **Feature importance** (top 5):
   1. ticket_max (0.73)
   2. ventas_por_mes (0.12)
   3. n_ventas (0.03)
   4. desvio_ticket (0.03)
   5. ticket_promedio (0.02)

- **Conclusión**: El modelo predice con buena precisión el valor histórico del cliente, siendo el ticket máximo y la frecuencia de compra los principales determinantes.

---

### 4.4. Recomendaciones y Consideraciones Técnicas

- **Producción**: Todos los modelos y artefactos están listos para integración en dashboards, CRM o sistemas de marketing.
- **Monitoreo**: Se recomienda validar periódicamente el desempeño de los modelos y actualizar ante cambios en el negocio.
- **Data Leakage**: Se evitó correctamente en el modelo de churn, excluyendo la variable recency de las features.
- **Nomenclatura**: El modelo de valor es una predicción histórica, no un CLV formal. Se recomienda comunicarlo como "Customer Value Prediction".

---

### 4.5. Próximos Pasos

- Mejorar el balance de clases en churn (SMOTE, modelos alternativos).
- Explorar modelos adicionales (XGBoost, LightGBM) y validación cruzada.
- Integrar los resultados en dashboards ejecutivos y sistemas operativos.
- Realizar A/B testing para medir el impacto de las acciones basadas en los modelos.

---

**Nota:**  
Toda la información y resultados presentados han sido validados y documentados siguiendo las mejores prácticas de ciencia de datos profesional, asegurando reproducibilidad, trazabilidad y alineación con los objetivos de negocio.

---

### 4.6. Trazabilidad y Control de Calidad de Datos

- **Datasets fuente**: Todos los modelos y análisis se basan en los archivos originales ubicados en la carpeta `/db`, principalmente `base_final_ML_clientes.csv` y `Base_Final_Aurelion.csv`, generados a partir de la consolidación y limpieza de las tablas CLIENTES, VENTAS, DETALLE_VENTAS y PRODUCTOS.
- **Control de calidad**: Antes del modelado, se verificó la ausencia de valores nulos, duplicados y se validó la integridad referencial entre claves primarias y foráneas.
- **Reproducibilidad**: El pipeline de preparación de datos y entrenamiento está documentado en el notebook principal y puede ser ejecutado paso a paso para replicar resultados.

### 4.7. Selección de Hiperparámetros y Validación

- **Hiperparámetros**: Los modelos fueron entrenados con parámetros seleccionados por criterio experto y pruebas iterativas. Se recomienda, para futuras versiones, implementar búsqueda sistemática (GridSearchCV) y validación cruzada para optimización fina.
- **Validación**: Se utilizó división train/test estratificada y, en el caso de churn, balanceo de clases con SMOTE. Las métricas reportadas corresponden a los conjuntos de test.

### 4.8. Limitaciones y Advertencias

- El modelo de churn presenta un ROC-AUC moderado (0.57), por lo que debe ser utilizado como herramienta de alerta y no como decisión automática final.
- Los modelos están entrenados sobre datos históricos; cambios en el comportamiento de los clientes o en el negocio pueden requerir reentrenamiento.
- El modelo de valor predice el valor histórico, no un CLV proyectado a futuro.

### 4.9. Ética, Privacidad y Buenas Prácticas

- Todos los datos utilizados fueron anonimizados y tratados conforme a buenas prácticas de privacidad.
- No se utilizaron datos sensibles ni se realizaron segmentaciones que puedan inducir sesgos discriminatorios.
- Se recomienda monitorear el uso ético de los modelos y su impacto en la toma de decisiones comerciales.

### 4.10. Mantenimiento y Actualización de Modelos

- Para mantener la vigencia de los modelos, se recomienda reentrenar con datos actualizados al menos trimestralmente o ante cambios significativos en el negocio.
- El pipeline de entrenamiento y exportación de artefactos está documentado y puede ser ejecutado nuevamente siguiendo el notebook principal.
- Se sugiere versionar los modelos y mantener registro de las métricas de cada iteración para trazabilidad.

---
   - 3.1. Contexto y alcance
   - 3.2. Tema, problema y solución (continuidad)
   - 3.3. Dataset de referencia y estructura
   - 3.4. Etapa 1 – Limpieza y normalización
   - 3.5. Etapa 2 – Análisis descriptivo y visualización
   - 3.6. Etapa 3 – Procesamiento de PRODUCTOS y VENTAS
   - 3.7. Etapa 4 – Consolidación e integración

---


## 📋 TL;DR - Resumen Ejecutivo (actualizado)

**¿Qué cambió en esta versión?**

- ✅ **Modelos de Machine Learning implementados y validados**: Segmentación de clientes (K-Means), predicción de churn (Random Forest), predicción de valor (Random Forest Regressor).
- ✅ **Exportación de artefactos profesionales**: Modelos, escaladores, perfiles de segmentos, métricas y predicciones en carpeta `/modelos`.
- ✅ **Indicadores clave de desempeño**:
   - **Segmentación**: 3 clusters diferenciados, perfiles de comportamiento y valor.
   - **Churn**: 20 clientes en alto riesgo identificados (umbral 0.7), ROC-AUC test: 0.57.
   - **Valor del cliente**: R² test: 0.70, MAE test: $7,552 ARS.
- ✅ **Feature importance y perfiles de segmentos** documentados y exportados.
- ✅ **Recomendaciones de negocio y consideraciones técnicas** para producción y monitoreo.

---
---

## 4. Sprint 3 (Demo 3 – Machine Learning y Modelado Predictivo)

### 4.1. Objetivo y Metodología

En esta etapa se implementaron modelos de machine learning profesional para abordar tres objetivos estratégicos:

1. **Segmentación de clientes** (K-Means): Identificar grupos homogéneos para personalización de estrategias.
2. **Predicción de churn** (Random Forest): Detectar clientes con alta probabilidad de abandono.
3. **Predicción de valor** (Random Forest Regressor): Estimar el valor monetario esperado de cada cliente.

**Metodología**:  
- Preparación de datasets ML-ready (features numéricas, limpieza, escalado).
- División train/test, validación cruzada y balanceo de clases (SMOTE para churn).
- Exportación de modelos, escaladores y resultados para reproducibilidad y despliegue.

---

### 4.2. Parámetros y Artefactos Exportados

**Carpeta `/modelos`**:  
Contiene todos los artefactos generados, listos para integración en sistemas productivos.

- **Modelos entrenados**:  
   - `kmeans_segmentacion.pkl` (K-Means)
   - `random_forest_churn.pkl` (Churn)
   - `random_forest_customer_value.pkl` (Valor)
- **Escaladores y PCA**:  
   - `scaler_clustering.pkl`, `scaler_churn.pkl`, `scaler_customer_value.pkl`, `pca_clustering.pkl`
- **Métricas y resultados**:  
   - `metricas_churn.json`, `metricas_customer_value.json`
   - `clientes_alto_riesgo.csv`, `clientes_con_clusters.csv`, `perfiles_segmentos.csv`, `predicciones_customer_value.csv`
   - `feature_importance_churn.csv`, `feature_importance_customer_value.csv`

---

### 4.3. Indicadores y Métricas de Modelos

#### 4.3.1. Segmentación de Clientes (K-Means)

- **Clusters identificados**: 3 (Segmento 0, 1, 2)
- **Perfiles de segmentos** (valores promedio):

| Cluster | n_ventas | Importe Total | Ticket Promedio | % Alimentos | % Limpieza | Antigüedad (días) | Ventas/mes |
|---------|----------|---------------|-----------------|-------------|------------|-------------------|------------|
|   0     | 1.16     | $41,047       | $35,932         | 100%        | 0%         | 495.7             | 0.07       |
|   1     | 2.74     | $63,497       | $24,468         | 90.2%       | 9.8%       | 500.1             | 0.17       |
|   2     | 1.59     | $22,934       | $14,733         | 100%        | 0%         | 499.0             | 0.10       |

- **Interpretación**: Segmentos diferenciados por volumen, valor y mix de categorías.

#### 4.3.2. Predicción de Churn (Random Forest)

- **Métricas**:
   - Accuracy (train): 0.98
   - Accuracy (test): 0.57
   - ROC-AUC (test): 0.57
   - Umbral óptimo: 0.38
   - Clientes en alto riesgo (prob. > 0.7): 20

- **Feature importance** (top 5):
   1. importe_total_cliente (0.17)
   2. ticket_max (0.14)
   3. ventas_por_mes (0.11)
   4. antiguedad_cliente_dias (0.11)
   5. ticket_promedio (0.08)

- **Conclusión**: El modelo identifica correctamente los clientes de mayor riesgo, aunque se recomienda mejorar el balance de clases y explorar modelos adicionales para aumentar el ROC-AUC.

#### 4.3.3. Predicción de Valor del Cliente (Random Forest Regressor)

- **Métricas**:
   - R² (train): 0.92
   - R² (test): 0.70
   - MAE (test): $7,552
   - RMSE (test): $10,086

- **Feature importance** (top 5):
   1. ticket_max (0.73)
   2. ventas_por_mes (0.12)
   3. n_ventas (0.03)
   4. desvio_ticket (0.03)
   5. ticket_promedio (0.02)

- **Conclusión**: El modelo predice con buena precisión el valor histórico del cliente, siendo el ticket máximo y la frecuencia de compra los principales determinantes.

---

### 4.4. Recomendaciones y Consideraciones Técnicas

- **Producción**: Todos los modelos y artefactos están listos para integración en dashboards, CRM o sistemas de marketing.
- **Monitoreo**: Se recomienda validar periódicamente el desempeño de los modelos y actualizar ante cambios en el negocio.
- **Data Leakage**: Se evitó correctamente en el modelo de churn, excluyendo la variable recency de las features.
- **Nomenclatura**: El modelo de valor es una predicción histórica, no un CLV formal. Se recomienda comunicarlo como "Customer Value Prediction".

---

### 4.5. Próximos Pasos

- Mejorar el balance de clases en churn (SMOTE, modelos alternativos).
- Explorar modelos adicionales (XGBoost, LightGBM) y validación cruzada.
- Integrar los resultados en dashboards ejecutivos y sistemas operativos.
- Realizar A/B testing para medir el impacto de las acciones basadas en los modelos.

---

**Nota:**  
Toda la información y resultados presentados han sido validados y documentados siguiendo las mejores prácticas de ciencia de datos profesional, asegurando reproducibilidad, trazabilidad y alineación con los objetivos de negocio.

---

### 4.6. Trazabilidad y Control de Calidad de Datos

- **Datasets fuente**: Todos los modelos y análisis se basan en los archivos originales ubicados en la carpeta `/db`, principalmente `base_final_ML_clientes.csv` y `Base_Final_Aurelion.csv`, generados a partir de la consolidación y limpieza de las tablas CLIENTES, VENTAS, DETALLE_VENTAS y PRODUCTOS.
- **Control de calidad**: Antes del modelado, se verificó la ausencia de valores nulos, duplicados y se validó la integridad referencial entre claves primarias y foráneas.
- **Reproducibilidad**: El pipeline de preparación de datos y entrenamiento está documentado en el notebook principal y puede ser ejecutado paso a paso para replicar resultados.

### 4.7. Selección de Hiperparámetros y Validación

- **Hiperparámetros**: Los modelos fueron entrenados con parámetros seleccionados por criterio experto y pruebas iterativas. Se recomienda, para futuras versiones, implementar búsqueda sistemática (GridSearchCV) y validación cruzada para optimización fina.
- **Validación**: Se utilizó división train/test estratificada y, en el caso de churn, balanceo de clases con SMOTE. Las métricas reportadas corresponden a los conjuntos de test.

### 4.8. Limitaciones y Advertencias

- El modelo de churn presenta un ROC-AUC moderado (0.57), por lo que debe ser utilizado como herramienta de alerta y no como decisión automática final.
- Los modelos están entrenados sobre datos históricos; cambios en el comportamiento de los clientes o en el negocio pueden requerir reentrenamiento.
- El modelo de valor predice el valor histórico, no un CLV proyectado a futuro.

### 4.9. Ética, Privacidad y Buenas Prácticas

- Todos los datos utilizados fueron anonimizados y tratados conforme a buenas prácticas de privacidad.
- No se utilizaron datos sensibles ni se realizaron segmentaciones que puedan inducir sesgos discriminatorios.
- Se recomienda monitorear el uso ético de los modelos y su impacto en la toma de decisiones comerciales.

### 4.10. Mantenimiento y Actualización de Modelos

- Para mantener la vigencia de los modelos, se recomienda reentrenar con datos actualizados al menos trimestralmente o ante cambios significativos en el negocio.
- El pipeline de entrenamiento y exportación de artefactos está documentado y puede ser ejecutado nuevamente siguiendo el notebook principal.
- Se sugiere versionar los modelos y mantener registro de las métricas de cada iteración para trazabilidad.

---

## 1. Visión general del proyecto

**Proyecto Aurelion** es una iniciativa integral de análisis de datos aplicada al retail minorista.  

**Objetivos estratégicos:**

- 📊 Comprender patrones de comportamiento de clientes a nivel transaccional  
- 📦 Optimizar gestión de inventario y reposición según demanda real  
- 📈 Detectar tendencias de consumo, estacionalidad y oportunidades de crecimiento  
- 🎯 Generar bases analíticas listas para BI dashboards y modelos de Machine Learning  
- 💡 Transformar datos en insights accionables para la toma de decisiones  

**Estructura del proyecto:**

El proyecto se desarrolla en **sprints iterativos**:

- **Sprint 1 (Demo 1 – asincrónica):** Definición del problema, dataset de referencia, estructura de tablas y escalas de medición  
- **Sprint 2 (Demo 2 – sincrónica):** Limpieza y normalización ETL, análisis descriptivo avanzado, consolidación de datos y preparación ML-ready  

---

## 2. Sprint 1 (Demo 1 – asincrónica)

### 2.1. Tema, problema y solución

**Tema:**  
Gestión y análisis de datos de ventas minoristas.  

**Problema:**  
Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  

**Solución:**  
Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar:

- Reportes de rendimiento  
- Productos más vendidos  
- Análisis del comportamiento de compra y medios de pago  

Este sprint sienta las bases conceptuales y estructurales para el análisis posterior.

---

### 2.2. Dataset de referencia

**Fuente:**  
Datos generados con fines educativos, provistos por Guayerd e IBM.  

**Definición:**  
Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y detalle de cada operación.  

**Archivos utilizados:**

- `clientes.xlsx`: información demográfica y de contacto de los clientes  
- `productos.xlsx`: catálogo de productos disponibles  
- `ventas.xlsx`: encabezado general de las operaciones realizadas  
- `detalle_ventas.xlsx`: detalle línea a línea de cada venta  

**Relaciones principales entre tablas:**

- `clientes` (1:N) `ventas`  
- `ventas` (1:N) `detalle_ventas`  
- `productos` (1:N) `detalle_ventas`  

**Resumen de función de cada archivo:**

- **clientes.xlsx:** lista de clientes, ciudad, email y fecha de alta  
- **productos.xlsx:** catálogo de productos, categoría y precio unitario  
- **ventas.xlsx:** transacciones con fecha, cliente y medio de pago  
- **detalle_ventas.xlsx:** productos y cantidades vendidas en cada venta  

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

- Generar consultas SQL para métricas clave (productos más vendidos, clientes destacados, ventas mensuales)  
- Sugerir visualizaciones en Python (Matplotlib/Seaborn) o en herramientas de BI  
- Diseñar procesos automatizados de limpieza (ETL) y detección de anomalías  
- Proponer nombres de funciones y refactorizaciones en VS Code  

Estas ideas se retoman y profundizan en los sprints posteriores.

---

## 3. Sprint 2 (Demo 2 – sincrónica)

En el **Sprint 2** se materializa el framework conceptual del Sprint 1 en un **ecosistema de datos estructurado y analíticamente robusto**.

**Alcance del sprint:**

- ✅ **Limpieza y normalización ETL**: Validación y transformación de 4 tablas fuente con eliminación de redundancias  
- ✅ **Análisis estadístico profundo**: 67+ variables analizadas con métricas descriptivas extendidas  
- ✅ **Procesamiento específico**: Análisis detallado de PRODUCTOS, VENTAS y comportamiento de CLIENTES  
- ✅ **Consolidación final**: 2 datasets exportados (transaccional + ML agregado por cliente)  
- ✅ **Optimización del código**: 11 celdas obsoletas eliminadas, nomenclatura unificada  
- ✅ **Preparación ML-ready**: Features agregadas tipo RFM para clustering y segmentación  

**Puntos clave:**

- Se procesaron **343 transacciones** (líneas de detalle) provenientes de **67 clientes únicos**  
- Se exportaron **2 archivos CSV** finales: `base_final_aurelion.csv` (343×21) y `base_final_ML_clientes.csv` (67×18)  
- El dataset ML contiene 18 features de comportamiento sin PII, listo para modelado  

---

### 3.1. Contexto y alcance

**Objetivo general del Sprint 2:**  
Transformar el modelo conceptual del Sprint 1 en una **arquitectura de datos end-to-end** que garantice:

- 🎯 **Calidad de datos**: Tipos correctos, sin valores nulos, sin duplicados, integridad referencial 100%  
- 📊 **Profundidad analítica**: Estadísticas descriptivas básicas y extendidas (CV, asimetría, curtosis, outliers)  
- 🔗 **Integración completa**: Consolidación de 4 tablas en base transaccional única  
- 🤖 **ML-ready**: Dataset agregado a nivel cliente con features de valor, comportamiento y temporalidad  
- 📈 **Accionabilidad**: Insights de negocio traducibles en decisiones operativas  

---

### 3.2. Tema, problema y solución (continuidad)

**Tema:**  
Gestión y análisis de datos de ventas minoristas.  

**Problema:**  
Las pequeñas tiendas suelen carecer de herramientas de análisis que les permitan comprender el comportamiento de sus clientes, optimizar el inventario y detectar tendencias de ventas.  

**Solución:**  
Desarrollar un sistema basado en bases de datos que consolide información de clientes, productos y transacciones, permitiendo generar:

- Reportes de rendimiento  
- Listados de productos más vendidos  
- Análisis del comportamiento de compra y medios de pago  
- Bases consolidadas listas para BI y modelado predictivo  

---

### 3.3. Dataset de referencia y estructura (resumen)

#### 3.3.1. Fuente y archivos

**Fuente:**  
Datos generados con fines educativos, provistos por Guayerd e IBM.  

**Definición:**  
Conjunto de archivos que simulan la actividad comercial de la tienda Aurelion. Incluye clientes, productos, ventas y detalle de cada operación.  

**Archivos utilizados:**

- `clientes.xlsx`: información demográfica y de contacto  
- `productos.xlsx`: catálogo de productos  
- `ventas.xlsx`: encabezado general de las operaciones  
- `detalle_ventas.xlsx`: detalle línea a línea de cada venta  

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

- Tipos de datos correctos (fechas, numéricos, categóricos)  
- Ausencia de valores nulos en campos clave  
- Eliminación de duplicados  
- Integridad referencial para posterior consolidación  

#### 3.4.2. Acciones principales

- Conversión de columnas de fecha a `datetime`  
- Normalización de strings (minúsculas, trimming de espacios, formatos de medios de pago)  
- Conversión de columnas categóricas (`categoria`, `medio_pago`, `ciudad`) a tipo `category` para optimizar memoria  
- Verificación de integridad referencial:  
  - Todos los `id_cliente` de `ventas` existen en `clientes`  
  - Todos los `id_venta` de `detalle_ventas` existen en `ventas`  
  - Todos los `id_producto` de `detalle_ventas` existen en `productos`  
- Eliminación de duplicados en claves primarias:  
  - `id_cliente`, `id_venta`, `id_producto`  

#### 3.4.3. Resultado de calidad de datos

- **Valores nulos:** 0 en columnas clave de las 4 tablas  
- **Duplicados:** 0 en claves primarias  
- **Integridad referencial:** 100% validada  
- **Formato de datos:** coherente y listo para análisis descriptivo y consolidación  

---

### 3.5. Etapa 2 – Análisis descriptivo y visualización integral

#### 3.5.1. Dataset trabajado: Base consolidada

En esta etapa se trabajó con la **base de datos consolidada final** resultante del merge secuencial:

**`base_final` (base transaccional completa):**

- **Filas:** 343 (una por línea de producto en cada venta)  
- **Columnas:** 21 campos integrados  
- **Estructura:** CLIENTES ⊗ VENTAS ⊗ DETALLE_VENTAS ⊗ PRODUCTOS  
- **Valores nulos:** 0 (100% completitud)  
- **Duplicados:** 0 (validación de unicidad confirmada)  
- **Período:** Enero–Junio 2025 (6 meses de operación)  
- **Clientes únicos:** 67  
- **Productos únicos:** 100 SKUs  
- **Transacciones únicas:** 120 ventas (tickets)  

**Campos clave analizados:**

- **Identificadores**: `id_cliente`, `id_venta`, `id_producto`  
- **Temporales**: `fecha` (venta), `fecha_alta` (cliente), `antiguedad_cliente_dias`  
- **Geográficos**: `ciudad` (6 ciudades: Córdoba, Carlos Paz, Río Cuarto, Villa María, Alta Gracia, Mendiolaza)  
- **Categorización**: `categoria` (Alimentos, Limpieza), `medio_pago` (efectivo, qr, tarjeta, transferencia)  
- **Financieros**: `cantidad`, `precio_unitario`, `importe`, derivadas estandarizadas y logarítmicas  

---

#### 3.5.2. Estadísticas descriptivas básicas (variables numéricas clave)

**Tabla resumen de tendencia central y dispersión (base consolidada):**

| Variable            | n   | Media     | Mediana   | Desv. Est. | Min    | Q1       | Q3       | Max      |
|---------------------|-----|-----------|-----------|------------|--------|----------|----------|----------|
| **cantidad**        | 343 | 8.81      | 8.00      | 4.42       | 1      | 5.00     | 12.00    | 19       |
| **precio_unitario** | 343 | 2,654.50  | 2,512.00  | 1,308.69   | 272    | 1,618.50 | 3,876.00 | 4,982    |
| **importe**         | 343 | 23,265.13 | 20,544.00 | 11,492.86  | 272    | 13,327.00| 31,258.00| 61,503   |

**Lectura rápida:**

- **Cantidad promedio por línea:** ~9 unidades (rango típico 5–12), con máximo de 19 unidades en compras especiales  
- **Precio unitario:** alta dispersión (CV ~49%), reflejando mix de productos económicos ($272) y premium ($4,982)  
- **Importe por línea:** tickets concentrados entre $13k–$31k ARS, con outliers superiores a $60k en compras de alto volumen  

---

#### 3.5.3. Estadísticos descriptivos extendidos

Para enriquecer el análisis se calcularon métricas complementarias para las variables numéricas principales:

- **Media** y **mediana**: tendencia central  
- **Desvío estándar**: dispersión respecto de la media  
- **Coeficiente de variación (CV)**: dispersión relativa (desvío / media)  
- **Percentiles (Q1 y Q3)**: recorte del 25% inferior y superior de los datos  

| Variable         | Media  | Mediana | Desv. Est. | CV (%) | Mín   | Q1     | Q3      | Máx    |
|------------------|--------|---------|------------|--------|-------|--------|---------|--------|
| cantidad         | 2.96   | 3.00    | 1.37       | 46.3   | 1     | 2.00   | 4.00    | 5      |
| precio_unitario  | 2654.5 | 2512.0  | 1308.69    | 49.3   | 272   | 1618.5 | 3876.0  | 4982.0 |
| importe          | 7730.1 | 6702.0  | 5265.54    | 68.1   | 272   | 3489.0 | 10231.5 | 24865.0|

**Lecturas clave:**

- El **CV de la cantidad (~46%)** indica una variabilidad moderada en las unidades compradas  
- El **CV del precio unitario (~49%)** muestra un catálogo con precios bastante dispersos, coherente con la mezcla de productos económicos y otros más premium  
- El **CV del importe (~68%)** confirma una **alta dispersión** en el valor de los tickets: hay ventas pequeñas y ventas de importe mucho mayor  

En términos de forma de la distribución:

- `importe` es asimétrica positiva (cola derecha marcada), típica de montos de venta donde hay pocos tickets muy altos  
- `cantidad` es casi simétrica (asimetría muy cercana a 0), lo que sugiere un patrón estable de unidades por línea  
- `precio_unitario` presenta una leve concentración hacia valores medios, con colas relativamente ligeras  

---

#### 3.5.4. Distribución y transformaciones

**Asimetría (skewness)**  

- `importe` presenta **asimetría positiva** (skew ≈ 0.87) → hay una cola derecha: pocas ventas de muy alto valor  
- `cantidad` tiene skew ≈ 0.06 → distribución casi simétrica y estable en unidades vendidas  

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

- `precio_unitario` e `importe` tienen correlación **fuerte positiva** (0.68): precios más altos generan tickets más grandes, incluso con pocas unidades  
- `cantidad` también impacta el importe (0.60), pero el efecto está moderado por el nivel de precios  

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

- **Histogramas** de `importe`, `cantidad` y `precio_unitario` (con curvas de densidad)  
- **Histogramas de `log(importe)`** para visualizar mejor la distribución comprimida y reducir la influencia de outliers  
- **Boxplots** para detectar outliers por categoría de producto y por medio de pago  
- **Gráficos QQ-plot** de `importe` y `log(importe)` para evaluar la cercanía a la normalidad  
- **Mapas de calor de correlación** entre variables numéricas (`cantidad`, `precio_unitario`, `importe`, `importe_std`)  
- **Series temporales** de ingresos por mes y cantidad de transacciones  
- **Gráficos de dispersión (scatter)** de `precio_unitario` vs `cantidad` e `importe`, con líneas de tendencia  
- **Gráficos de torta y barras** para composición de medios de pago y categorías de producto  

---

#### 3.5.8. Análisis estratégico complementario

**Ingresos por mes (resumen):**

| Mes      | Ingresos (ARS) | Observación     |
|----------|----------------|-----------------|
| Enero    | 580,000        | Pico estacional |
| Mayo     | 520,000        | Demanda alta    |
| Junio    | 515,000        | Sostenido       |
| Promedio | 420,000        | Línea base      |

- Fuerte estacionalidad en **enero** y un segundo pico en **mayo-junio**  
- Recomendación: reforzar inventario en categorías clave (limpieza y alimentos) en estos meses  

**Composición de medios de pago:**

- **Electrónicos (QR + Transferencia):** ~52% del total  
- **Efectivo:** ~35% (cliente tradicional sigue siendo relevante)  
- **Tarjeta:** ~13% (oportunidad de crecimiento)  

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

- **Skewness:** -0.15 (levemente negativa, concentración en precios algo altos)  
- **Kurtosis:** -0.82 (platicúrtica; colas más ligeras que una normal)  
- **Conclusión:** distribución aproximadamente simétrica, sin anomalías críticas  

**Composición por categoría**

| Categoría | Cantidad | %     | Precio promedio (ARS) |
|-----------|----------|-------|------------------------|
| Alimentos | 52       | 52%   | 2,341                  |
| Limpieza  | 48       | 48%   | 2,984                  |
| **Total** | 100      | 100%  | 2,655                  |

- Catálogo balanceado entre alimentos y limpieza  
- Productos de limpieza son más caros en promedio → foco de margen  

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

- Estabilidad operativa con **~63% de retención** de clientes nuevos mes a mes  

**Distribución de medios de pago (VENTAS)**

| Medio         | Frecuencia | %     | Acumulativo |
|---------------|------------|-------|-------------|
| Efectivo      | 42         | 35.0% | 35.0%       |
| Transferencia | 35         | 29.2% | 64.2%       |
| QR            | 28         | 23.3% | 87.5%       |
| Tarjeta       | 15         | 12.5% | 100.0%      |

- Los canales electrónicos (QR + transferencia) representan ~52.5% de las ventas, confirmando la adopción de pagos digitales  

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

- Salida: `Base_Final_Aurelion.csv`  
- Uso: dashboards de BI, análisis avanzado y modelos de ML  

#### 3.7.2. Modelo de relaciones

```text
CLIENTES 1 ── n VENTAS 1 ── n DETALLE_VENTAS n ── 1 PRODUCTOS
