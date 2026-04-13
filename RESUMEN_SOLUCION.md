# SOLUCIÓN: Análisis de Ingresos - Proyecto PTAR y Cloacas

## Información General del Proyecto
- **Proyecto**: Programa de Optimización y Ampliación de Tratamiento de Aguas Residuales
- **Ciudad**: Sapinda
- **Población (2018)**: 89,600 personas
- **Hogares en la ciudad**: 28,264 hogares (promedio 3.17 personas/hogar)
- **Hogares directamente beneficiados (Cloacas)**: 572 hogares
- **Horizonte de evaluación**: 30 años
- **Tasa de descuento**: 5%
- **Tipo de cambio**: 100 ARS/USD

---

## TAREA 1: ANÁLISIS DE ESTADÍSTICA DESCRIPTIVA

### Encuesta de Cloaca (Nuevas redes de alcantarillado)

**Estadísticas Generales:**
- **Media (Promedio)**: $1,441.67 ARS
- **Mediana**: $1,000.00 ARS
- **Desviación Estándar**: $1,770.98 ARS
- **Rango**: $200 - $10,000 ARS
- **N (respuestas válidas)**: 60 hogares

### Encuesta de PTAR (Planta de Tratamiento de Aguas Residuales)

**Estadísticas Generales:**
- **Media (Promedio)**: $166.81 ARS
- **Mediana**: $175.00 ARS
- **Desviación Estándar**: $104.04 ARS
- **Rango**: $5 - $375 ARS
- **N (respuestas válidas)**: 142 hogares

### Distribución de DAP

Se generó un gráfico (`distribucion_dap.png`) que muestra:
- Distribución de la disposición a pagar para Cloaca
- Distribución de la disposición a pagar para PTAR
- Líneas de media y mediana en ambos gráficos

---

## TAREA 2: ESTIMACIÓN DE INGRESO ANUAL AGREGADO

### SIN DISCRIMINACIÓN DE PRECIOS - CLOACA

| Método | DAP/Hogar | Hogares | Ingreso Anual ARS | Ingreso Anual USD |
|--------|-----------|---------|-------------------|-------------------|
| **Media** | $1,441.67 | 572 | $824,633.33 | $8,246.33 |
| **Mediana** | $1,000.00 | 572 | $572,000.00 | $5,720.00 |

### SIN DISCRIMINACIÓN DE PRECIOS - PTAR

| Método | DAP/Hogar | Hogares | Ingreso Anual ARS | Ingreso Anual USD |
|--------|-----------|---------|-------------------|-------------------|
| **Media** | $166.81 | 28,264 | $4,714,813.38 | $47,148.13 |
| **Mediana** | $175.00 | 28,264 | $4,946,200.00 | $49,462.00 |

---

## TAREA 3: DISCRIMINACIÓN DE PRECIOS POR NIVEL DE INGRESO

**Hallazgo Importante**: Los datos de nivel de ingreso en las encuestas no fueron completamente capturados en el archivo Excel. La base de datos muestra principalmente valores vacíos o '''' en las columnas de ingreso, lo que impide identificar claramente qué respondentes pertenecen a cada categoría de ingreso.

**Categorías de Ingreso Disponibles** (según documento):
1. Menos de $20,000
2. Entre $20,000 y $30,000
3. Entre $30,000 y $40,000
4. Entre $40,000 y $60,000
5. $60,000 o más

**Recomendación**: Para realizar un análisis completo de discriminación de precios, se requiere:
- Revisar la base de datos original para completar los datos de ingresos
- Realizar una limpieza de datos más exhaustiva
- O solicitar una versión corregida del archivo Excel

---

## TAREA 4: COMPARACIÓN - CON Y SIN DISCRIMINACIÓN

Debido a la limitación en los datos de ingreso mencionada en la Tarea 3, no fue posible completar el análisis de discriminación de precios. Sin embargo, la lógica del modelo está implementada y puede ejecutarse una vez que se corrijan los datos de ingreso.

**Conclusión Esperada**: Los análisis de discriminación de precios permitirían:
- Aumentar ingresos cobrando más a hogares con mayores ingresos
- Reducir carga a hogares con menores ingresos (efecto progresivo)
- Evaluar trade-off entre equidad y sostenibilidad financiera del proyecto

---

## TAREA 5: BENEFICIO POR REDUCCIÓN DE CONSUMO DE AGUA EN BOTELLAS

### Cambios en el Consumo:
- **Consumo anterior**: 10 litros/mes por hogar
- **Consumo actual**: 5 litros/mes por hogar
- **Reducción**: 5 litros/mes (50%)
- **Precio promedio agua embotellada**: $0.50 USD/litro

### Beneficio Anual por Hogar:
- **Ahorro**: $30.00 USD/año
- **Ahorro**: $3,000 ARS/año

### Beneficio Total de la Ciudad (28,264 hogares):
- **Ahorro anual**: $847,920 USD
- **Ahorro anual**: $84,792,000 ARS

**Interpretation**: Todos los habitantes de la ciudad se benefician porque mejora la calidad del agua corriente y reducen su dependencia de agua embotellada.

---

## TAREA 6: BENEFICIO POR ELIMINACIÓN DE COSTOS DE VACIADO DE POZOS

### Situación Actual:
- Hogares sin conexión a cloacas utilizan **pozos negros**
- **Costo de vaciado**: $50 USD/hogar/año

### Beneficio por Hogar que se Conecte:
- **Ahorro anual**: $50 USD/hogar
- **Ahorro anual**: $5,000 ARS/hogar

### Beneficio Total (572 hogares que se conectan):
- **Ahorro anual**: $28,600 USD
- **Ahorro anual**: $2,860,000 ARS

**Interpretation**: Solo los 572 hogares que se conecten a las nuevas redes de cloaca se benefician de la eliminación de este costo recurrente.

---

## TAREA 7: PROYECCIÓN DE INGRESOS DAP (30 AÑOS)

### Supuestos:
- **Inicio de beneficios**: Año 3 (después de conclusión de obras)
- **Conectividad en año 3**: 80%
- **Conectividad alcanzada año 6**: 100%
- **Crecimiento poblacional**: 1% anual
- **DAP constante** en el tiempo (sin ajustes inflacionarios)

### CLOACA - Valor Presente de Ingresos DAP

| Componente | Valor (ARS) | Valor (USD) |
|------------|-------------|------------|
| **VP Total (30 años)** | $12,118,787 | $121,188 |
| **Promedio anual** | $872,089 | $8,721 |

**Cronograma de Conectividad:**
- Año 1-2: 0% (construcción)
- Año 3: 80%
- Año 4: 87%
- Año 5: 93%
- Año 6+: 100% (con crecimiento poblacional)

### PTAR - Valor Presente de Ingresos DAP

| Componente | Valor (ARS) | Valor (USD) |
|------------|-------------|------------|
| **VP Total (30 años)** | $69,288,758 | $692,888 |
| **Promedio anual** | $4,986,139 | $49,861 |

---

## TAREA 8: PROYECCIÓN DE BENEFICIOS POR AHORRO DE COSTOS (30 AÑOS)

### A. Reducción de Consumo de Agua en Botellas

| Componente | Valor (ARS) | Valor (USD) |
|------------|-------------|------------|
| **VP Total (30 años)** | $1,274,662,334 | $12,746,623 |
| **Promedio anual** | $84,977,489 | $849,775 |

**Nota**: Este es el beneficio más significativo del proyecto, ya que beneficia a toda la población urbana (28,264 hogares).

### B. Eliminación de Costos de Pozos Negros

| Componente | Valor (ARS) | Valor (USD) |
|------------|-------------|------------|
| **VP Total (30 años)** | $42,993,847 | $429,938 |
| **Promedio anual** | $2,933,263 | $29,333 |

**Nota**: Solo beneficia a los 572 hogares que se conectan a la nueva red de cloacas.

---

## TAREA 9: PROPUESTAS PARA BENEFICIOS EN SECTOR PESQUERO Y TURISMO

### 1. BENEFICIOS EN EL SECTOR PESQUERO

#### A. Incremento de Biomasa de Peces
- Realizar estudios de biomonitoreo antes y después del proyecto
- Medir densidad y biomasa de poblaciones de peces
- Multiplicar biomasa adicional por precio de mercado
- Usar modelos de dinámica poblacional (stock assessment)

#### B. Reducción de Pérdidas Actuales
- Estudiar pérdida actual de pesca por contaminación
- Analizar datos de pescadores (CPUE = Captura Por Unidad de Esfuerzo)
- Comparar CPUE pre y post proyecto
- Estimar disminución de contaminación en costas

#### C. Precios Hedónicos
- Valores de permisos de pesca comercial
- Precios de cuotas de pesca
- Renta económica de la mejora ambiental

### 2. BENEFICIOS EN EL SECTOR TURISMO

#### A. Uso Recreativo de Playas y Ríos
- Encuestas de visitantes (similar a DAP)
- Preguntar disposición a pagar por playas limpias
- Estimar número de visitantes actuales vs. potenciales
- Calcular días-visitante pre y post proyecto

#### B. Metodología de Costo de Viaje
- Identificar sitios similares en la región
- Medir costo de transporte para visitantes
- Usar regresión para estimar demanda recreativa
- Calcular beneficio del cambio de calidad ambiental

#### C. Valor de Propiedades (Precios Hedónicos)
- Estudiar hoteles, restaurantes, comercios cercanos
- Estimar aumento de valor de propiedad costera
- Usar precios hedónicos de propiedad
- Relacionar con distancia a ríos/playas contaminados

#### D. Empleo Generado
- Guías turísticos, operadores de excursiones
- Empleados en hoteles y restaurantes
- Salarios promedio del sector
- Multiplicador económico (3-5x según ruralidad)

### 3. METODOLOGÍA INTEGRADA RECOMENDADA

#### Línea Base (Año 0-1):
- Estudios de calidad de agua y sedimentos
- Conteos de peces y especies
- Encuestas de turismo existente
- Ingresos actuales de pescadores

#### Monitoreo (Años 3, 6, 10, 15, 20, 30):
- Repetir todos los estudios de línea base
- Documentar cambios ambientales observados
- Documentar cambios en ingresos de pescadores

#### Análisis de Contrafáctico:
- Estimar escenario "sin proyecto"
- Usar ciudades similares como comparación (método diff-in-diff)
- Controlar por otras variables macroeconómicas

#### Análisis de Sensibilidad:
- Escenarios optimista/pesimista
- Variar tasas de recuperación de peces
- Variar elasticidad precio de demanda turística

### 4. ESTIMACIÓN PRELIMINAR (CONSERVADORA)

#### Pesca:
- Supuesto: Recuperación de 20% de biomasa perdida
- Captura actual: datos locales necesarios
- Precio promedio: $5-10 USD/kg
- **Resultado**: análisis caso a caso

#### Turismo:
- Incremento de visitantes: 50% con playas limpias (hipótesis)
- Gasto promedio visitante: $50-100 USD
- Ocupación actual de hoteles: datos de INDEC
- **Resultado**: análisis caso a caso

### 5. NOTAS IMPORTANTES

⚠️ **Crítico**: 
- Beneficios en pesca y turismo podrían ser 30-50% de beneficios totales para ciudades costeras
- NO incluirlos en análisis oficial hasta tener datos sólidos (sesgo conservador actual es apropiado)
- Ejecutar estudios de línea base ANTES de invertir
- Coordinar con universidades locales y asociaciones de pesca para monitoreo participativo

---

## RESUMEN FINANCIERO: VALOR PRESENTE (30 AÑOS, TASA DESCUENTO 5%)

| Componente | Valor (ARS) | Valor (USD) |
|------------|-------------|------------|
| **PTAR (DAP)** | $69,288,758 | $692,888 |
| **Cloaca (DAP)** | $12,118,787 | $121,188 |
| **Reducción Agua Botellas** | $1,274,662,334 | $12,746,623 |
| **Eliminación Pozos Negros** | $42,993,847 | $429,938 |
| **TOTAL** | **$1,399,064,000** | **$13,990,638** |

### Análisis de Importancia Relativa:

```
Reducción de Agua Botellas:        91.1% de beneficios
Eliminación de Pozos Negros:       3.1% de beneficios
PTAR (DAP):                         5.0% de beneficios
Cloaca (DAP):                       0.9% de beneficios
```

**Interpretation**: El beneficio **más importante** del proyecto proviene de la mejora en calidad del agua corriente (menos necesidad de agua embotellada), no de los ingresos por DAP. Esto sugiere que el proyecto tiene un fuerte componente de bienestar para la población.

---

## ARCHIVOS GENERADOS

1. **solucion_tp.py**: Script Python completo con todo el análisis
2. **distribucion_dap.png**: Gráficos de distribución de DAP para Cloaca y PTAR
3. **RESUMEN_SOLUCION.md**: Este documento (resumen en Markdown)

---

## RECOMENDACIONES PARA MEJORAS FUTURAS

1. **Completar datos de ingresos** en la base de datos para análisis de discriminación de precios
2. **Realizar estudios de línea base** para pesca y turismo (recomendado)
3. **Actualizar tasas de crecimiento** con proyecciones demográficas oficiales del INDEC
4. **Considerar inflación** en los valores de DAP para proyecciones
5. **Análisis de sensibilidad** con diferentes tasas de descuento (3%, 5%, 8%, 10%)
6. **Evaluación ambiental** completa de impactos en recursos pesqueros y ecosistemas costeros

---

**Análisis completado**: [Fecha de ejecución]
**Herramientas utilizadas**: Python 3.14, pandas, openpyxl, python-docx, matplotlib
