# TP Proyectos - Python

## 📊 Análisis de Ingresos - Proyecto PTAR y Cloacas - Ciudad de Sapinda

Este repositorio contiene el análisis completo de un proyecto de optimización y ampliación de la Planta de Tratamiento de Aguas Residuales (PTAR) en la ciudad de Sapinda, Argentina.

### 🎯 Objetivo del Proyecto

Evaluar los ingresos y beneficios de un proyecto de saneamiento urbano que incluye:
- Optimización de la Planta de Tratamiento de Aguas Residuales (PTAR)
- Construcción de nuevas redes de alcantarillado (cloacas)
- Análisis de disposición a pagar (DAP) de los beneficiarios

### 📁 Archivos Principales

#### Datos de Entrada
- `2024 - TP2 - Ingresos.docx` - Consignas y especificaciones del proyecto
- `2021 - TP2 - Ingresos.xlsx` - Base de datos con encuestas de disposición a pagar

#### Análisis y Resultados
- `solucion_tp.py` - Script Python completo con todo el análisis
- `RESUMEN_SOLUCION.md` - Resumen detallado de resultados
- `INFORME_PROFESOR.md` - Informe para docente sobre herramientas y aprendizaje
- `distribucion_dap.png` - Gráficos de distribución de disposición a pagar

#### Salidas del Análisis
- `resultados_analisis.txt` - Resultados completos del programa
- `resultados_analisis_utf8.txt` - Versión con codificación UTF-8

### 🛠️ Tecnologías Utilizadas

- **Python 3.14** - Lenguaje de programación principal
- **pandas** - Manipulación y análisis de datos
- **openpyxl** - Lectura de archivos Excel
- **python-docx** - Lectura de archivos Word
- **matplotlib** - Generación de gráficos
- **VS Code** - Entorno de desarrollo

### 📈 Resultados Principales

#### Estadísticas Descriptivas
- **Cloaca**: Media $1,442 ARS/hogar/año (60 respuestas válidas)
- **PTAR**: Media $168 ARS/hogar/año (142 respuestas válidas)

#### Valor Presente Total (30 años, tasa descuento 5%)
- **PTAR (DAP)**: $693K USD
- **Cloaca (DAP)**: $121K USD
- **Reducción agua botellas**: $12.7M USD
- **Eliminación pozos negros**: $430K USD
- **TOTAL**: **$14.0M USD**

### 🔍 Metodologías Implementadas

1. **Análisis de Disposición a Pagar (DAP)** - Encuestas contingentes
2. **Proyecciones financieras** - Valor presente con crecimiento poblacional
3. **Beneficios por ahorro de costos** - Agua embotellada y vaciado de pozos
4. **Propuestas para beneficios ambientales** - Metodologías para pesca y turismo

### 📋 Estructura del Análisis

```
TAREA 1: Estadística descriptiva de encuestas DAP
TAREA 2: Estimación de ingresos anuales agregados
TAREA 3: Discriminación de precios por nivel de ingreso
TAREA 4: Comparación con/sin discriminación (impacto en subsidios)
TAREA 5: Beneficios por reducción de consumo de agua embotellada
TAREA 6: Beneficios por eliminación de costos de pozos negros
TAREA 7: Proyección de ingresos DAP (30 años)
TAREA 8: Proyección de beneficios por ahorro de costos (30 años)
TAREA 9: Metodologías para estimar beneficios en pesca y turismo
```

### 🚀 Cómo Ejecutar el Análisis

1. **Instalar dependencias**:
   ```bash
   pip install pandas openpyxl python-docx matplotlib
   ```

2. **Ejecutar el análisis completo**:
   ```bash
   python solucion_tp.py
   ```

3. **Ver resultados**: Los gráficos y archivos de salida se generan automáticamente.

### 👥 Equipo

- **Desarrollador**: [Tu nombre]
- **Institución**: [Tu universidad/facultad]
- **Materia**: [Nombre de la materia]
- **Profesor**: [Nombre del profesor]

### 📝 Notas Importantes

- **Limitación de datos**: La columna de ingresos familiares tiene datos incompletos, lo que impide análisis completo de discriminación de precios.
- **Sesgo conservador**: Los beneficios ambientales (pesca y turismo) no se incluyen en cálculos finales por falta de datos específicos.
- **Horizonte**: 30 años con tasa de descuento del 5%.

### 🔗 Enlaces Relacionados

- [Documentación Python](https://docs.python.org/3/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Metodología de Valoración Contingente](https://en.wikipedia.org/wiki/Contingent_valuation)

### 📄 Licencia

Este proyecto es para fines académicos. Los datos utilizados son propiedad de la institución educativa.

---

**Última actualización**: Abril 2026
**Versión**: 1.0