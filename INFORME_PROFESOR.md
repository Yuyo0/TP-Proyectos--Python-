# Informe para el Profesor - TP2 Ingresos Proyecto PTAR

## Herramientas Probadas

### 1. Python y Librerías
- **Python 3.14**: Lenguaje principal para el análisis
- **pandas**: Para manipulación de datos tabulares
- **openpyxl**: Para leer archivos Excel (.xlsx)
- **python-docx**: Para leer archivos Word (.docx)
- **matplotlib**: Para crear gráficos y visualizaciones

### 2. Entorno de Desarrollo
- **VS Code**: Editor de código con terminal integrada
- **Terminal PowerShell**: Para ejecutar comandos y scripts Python
- **pip**: Gestor de paquetes para instalar librerías

### 3. Herramientas de Análisis
- **Jupyter-like approach**: Ejecuté código en scripts Python con salidas detalladas
- **Git**: Para control de versiones (aunque no lo usé activamente en esta sesión)

## Exploración de Datos

### Sí, pude explorar los datos exitosamente:

1. **Lectura de archivos**:
   - Leí el archivo "2024 - TP2 - Ingresos.docx" para entender las consignas
   - Leí el archivo "2021 - TP2 - Ingresos.xlsx" con datos de encuestas

2. **Análisis básico**:
   - Identifiqué 60 respuestas válidas para cloaca y 142 para PTAR
   - Calculé estadísticas descriptivas (media, mediana, desviación estándar)
   - Creé histogramas para visualizar distribuciones de DAP

3. **Limpieza de datos**:
   - Eliminé respuestas vacías o inválidas
   - Convertí datos a tipos numéricos apropiados
   - Identifiqué problemas en la columna de ingresos (datos incompletos)

## Dudas que Surgieron

### 1. Problemas Técnicos
- **Codificación de caracteres**: Tuve problemas con caracteres especiales (ñ, acentos) al guardar archivos de texto
- **Instalación de librerías**: ¿Cómo manejar dependencias en diferentes entornos?
- **Gestión de archivos grandes**: Los resultados de terminal se truncaron, ¿cómo manejar salidas extensas?

### 2. Análisis de Datos
- **Datos incompletos**: La columna de ingresos familiares está mayormente vacía. ¿Cómo proceder con análisis de discriminación de precios?
- **Validez de respuestas**: ¿Cómo identificar respuestas "protesta" o no válidas en encuestas de DAP?
- **Representatividad**: ¿Son las 60/142 respuestas suficientes para representar a toda la población?

### 3. Aspectos Metodológicos
- **Proyecciones a largo plazo**: ¿Es realista asumir DAP constante por 30 años sin ajustes inflacionarios?
- **Beneficios ambientales**: ¿Cómo cuantificar beneficios en pesca y turismo sin datos específicos?
- **Tasa de descuento**: ¿Por qué usar 5%? ¿Cómo afecta esto las decisiones de inversión?

### 4. Aspectos Conceptuales
- **Valor Presente vs. Flujo Anual**: ¿Cuándo usar cada enfoque?
- **Equidad vs. Eficiencia**: ¿Cómo balancear precios uniformes vs. discriminación por ingreso?
- **Beneficios no monetarios**: ¿Cómo incluir mejoras en calidad de vida que no se miden en dinero?

## Primeras Impresiones

### Positivas
- **Python es muy poderoso**: Permite automatizar análisis complejos que serían tediosos manualmente
- **Visualizaciones ayudan**: Los gráficos hacen que los datos sean más comprensibles
- **Reproducibilidad**: El código se puede ejecutar múltiples veces con resultados consistentes

### Desafíos
- **Curva de aprendizaje**: Requiere conocimientos básicos de programación
- **Limpieza de datos toma tiempo**: La mayoría del trabajo es preparar los datos, no analizarlos
- **Errores sutiles**: Un error de sintaxis puede detener todo el análisis

### Manejo Básico de Herramientas
- **Instalé librerías**: Usé `pip install` exitosamente
- **Leí archivos**: Pude importar datos desde Excel y Word
- **Hice cálculos básicos**: Media, mediana, sumas, proyecciones
- **Creé visualizaciones**: Histogramas con matplotlib
- **Ejecuté scripts**: Desde terminal y dentro de VS Code

## Preguntas para la Próxima Clase

1. ¿Cómo manejar datos incompletos en análisis de DAP?
2. ¿Qué metodologías recomiendan para estimar beneficios ambientales?
3. ¿Cuándo es apropiado usar Python vs. Excel para análisis económicos?
4. ¿Cómo validar que las respuestas de encuestas son representativas?
5. ¿Qué herramientas adicionales recomiendan para análisis de proyectos?

---

**Fecha**: Abril 2026  
**Herramientas principales usadas**: Python, VS Code, Terminal  
**Tiempo dedicado**: ~2-3 horas de exploración inicial