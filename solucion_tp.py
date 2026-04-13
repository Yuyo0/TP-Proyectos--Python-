import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from docx import Document

# Configuración
EXCHANGE_RATE = 100  # ARS/USD
HOUSEHOLDS_TOTAL_CITY = int(89600 / 3.17)  # Total households in city
HOUSEHOLDS_CLOACAS = 572  # Direct beneficiaries of new sewage networks
CONNECTIVITY_YEAR3 = 0.80  # Connectivity rate in year 3
FINAL_CONNECTIVITY = 1.00  # 100% connectivity

# ============================================================================
# PART 1: LOAD AND CLEAN DATA
# ============================================================================
print("=" * 80)
print("ANÁLISIS DE INGRESOS - PROYECTO PTAR Y CLOACAS - CIUDAD DE SAPINDA")
print("=" * 80)
print()

# Load data
excel_path = r"c:\VS Code Projects\TP Proyectos (Python)\2021 - TP2 - Ingresos.xlsx"
df_cloaca = pd.read_excel(excel_path, sheet_name='cloaca')
df_ptar = pd.read_excel(excel_path, sheet_name='ptar')

# Clean data - Extract relevant columns
# Structure: Column 1 = ID, Column 2 = DAP amount, Columns 3-5 = Education, Columns 6-10 = Income brackets

def clean_dataframe(df, sheet_name):
    """Clean and prepare the survey data"""
    print(f"Procesando hoja: {sheet_name}")
    
    # Extract DAP column (column 2, index 1)
    dap_column = df.iloc[:, 1]
    
    # Extract income category (columns 6-10, indices 6-10)
    income_cols = df.iloc[:, 6:11]
    
    # Create a clean dataframe
    clean_df = pd.DataFrame()
    clean_df['ID'] = df.iloc[:, 0]
    clean_df['DAP'] = pd.to_numeric(dap_column, errors='coerce')
    
    # Decode income category
    income_categories = [
        'Menos de $ 20000',
        'Entre $ 20000 y $ 30000',
        'Entre $ 30000 y $ 40000',
        'Entre $ 40000 y $ 60000',
        '$ 60000 o más'
    ]
    
    clean_df['Income_Category'] = 'Unknown'
    for i, income_cat in enumerate(income_categories):
        mask = income_cols.iloc[:, i] == 1.0
        clean_df.loc[mask, 'Income_Category'] = income_cat
    
    # Remove rows without DAP values
    clean_df = clean_df[clean_df['DAP'].notna()].copy()
    clean_df = clean_df[clean_df['DAP'] > 0].copy()
    
    print(f"  Total respuestas válidas: {len(clean_df)}")
    print()
    
    return clean_df

df_cloaca_clean = clean_dataframe(df_cloaca, 'cloaca')
df_ptar_clean = clean_dataframe(df_ptar, 'ptar')

# ============================================================================
# TASK 1: DESCRIPTIVE STATISTICS
# ============================================================================
print("=" * 80)
print("TAREA 1: ANÁLISIS DE ESTADÍSTICA DESCRIPTIVA")
print("=" * 80)
print()

def print_descriptive_stats(df, name):
    """Print descriptive statistics for DAP"""
    print(f"\n{name.upper()}")
    print("-" * 60)
    
    # Overall statistics
    print(f"\nEstadísticas Generales:")
    print(f"  Media (Promedio): ${df['DAP'].mean():,.2f}")
    print(f"  Mediana: ${df['DAP'].median():,.2f}")
    print(f"  Desviación Estándar: ${df['DAP'].std():,.2f}")
    print(f"  Mínimo: ${df['DAP'].min():,.2f}")
    print(f"  Máximo: ${df['DAP'].max():,.2f}")
    print(f"  N (cantidad de respuestas): {len(df)}")
    
    # By income level
    print(f"\nEstadísticas por Nivel de Ingreso:")
    print(f"{'Nivel de Ingreso':<40} {'Media':<15} {'Mediana':<15} {'N':<5}")
    print("-" * 75)
    
    for income_cat in df['Income_Category'].unique():
        if income_cat != 'Unknown':
            subset = df[df['Income_Category'] == income_cat]['DAP']
            if len(subset) > 0:
                print(f"{income_cat:<40} ${subset.mean():>13,.2f} ${subset.median():>13,.2f} {len(subset):>3}")
    
    return {
        'mean_overall': df['DAP'].mean(),
        'median_overall': df['DAP'].median(),
        'by_income': df.groupby('Income_Category')['DAP'].agg(['mean', 'median', 'count'])
    }

stats_cloaca = print_descriptive_stats(df_cloaca_clean, 'Cloaca')
stats_ptar = print_descriptive_stats(df_ptar_clean, 'PTAR')

# ============================================================================
# Create visualization of distributions
# ============================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(df_cloaca_clean['DAP'], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].set_title('Distribución de DAP - Cloaca', fontsize=12, fontweight='bold')
axes[0].set_xlabel('DAP (ARS)')
axes[0].set_ylabel('Frecuencia')
axes[0].axvline(df_cloaca_clean['DAP'].mean(), color='red', linestyle='--', linewidth=2, label=f"Media: ${df_cloaca_clean['DAP'].mean():,.0f}")
axes[0].axvline(df_cloaca_clean['DAP'].median(), color='green', linestyle='--', linewidth=2, label=f"Mediana: ${df_cloaca_clean['DAP'].median():,.0f}")
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].hist(df_ptar_clean['DAP'], bins=30, color='coral', edgecolor='black', alpha=0.7)
axes[1].set_title('Distribución de DAP - PTAR', fontsize=12, fontweight='bold')
axes[1].set_xlabel('DAP (ARS)')
axes[1].set_ylabel('Frecuencia')
axes[1].axvline(df_ptar_clean['DAP'].mean(), color='red', linestyle='--', linewidth=2, label=f"Media: ${df_ptar_clean['DAP'].mean():,.0f}")
axes[1].axvline(df_ptar_clean['DAP'].median(), color='green', linestyle='--', linewidth=2, label=f"Mediana: ${df_ptar_clean['DAP'].median():,.0f}")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('distribucion_dap.png', dpi=300, bbox_inches='tight')
print("\n[OK] Gráfico de distribuciones guardado en 'distribucion_dap.png'")

# ============================================================================
# TASK 2: AGGREGATE ANNUAL INCOME ESTIMATION
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 2: ESTIMACIÓN DE INGRESO ANUAL AGREGADO")
print("=" * 80)
print()

def calculate_aggregate_income(df, project_name, num_households):
    """Calculate aggregate annual income"""
    print(f"\n{project_name.upper()}")
    print("-" * 60)
    
    # Without discrimination - using mean
    mean_dap = df['DAP'].mean()
    annual_income_ars_mean = mean_dap * num_households
    annual_income_usd_mean = annual_income_ars_mean / EXCHANGE_RATE
    
    # Without discrimination - using median
    median_dap = df['DAP'].median()
    annual_income_ars_median = median_dap * num_households
    annual_income_usd_median = annual_income_ars_median / EXCHANGE_RATE
    
    print(f"\nSin Discriminación de Precios:")
    print(f"  Usando Media:")
    print(f"    - DAP medio: ${mean_dap:,.2f}")
    print(f"    - Hogares beneficiarios: {num_households:,.0f}")
    print(f"    - Ingreso anual (ARS): ${annual_income_ars_mean:,.2f}")
    print(f"    - Ingreso anual (USD): ${annual_income_usd_mean:,.2f}")
    
    print(f"\n  Usando Mediana:")
    print(f"    - DAP mediano: ${median_dap:,.2f}")
    print(f"    - Hogares beneficiarios: {num_households:,.0f}")
    print(f"    - Ingreso anual (ARS): ${annual_income_ars_median:,.2f}")
    print(f"    - Ingreso anual (USD): ${annual_income_usd_median:,.2f}")
    
    return {
        'mean': mean_dap,
        'median': median_dap,
        'annual_income_ars_mean': annual_income_ars_mean,
        'annual_income_usd_mean': annual_income_usd_mean,
        'annual_income_ars_median': annual_income_ars_median,
        'annual_income_usd_median': annual_income_usd_median,
        'num_households': num_households
    }

income_cloaca = calculate_aggregate_income(df_cloaca_clean, 'Cloaca', HOUSEHOLDS_CLOACAS)
income_ptar = calculate_aggregate_income(df_ptar_clean, 'PTAR', HOUSEHOLDS_TOTAL_CITY)

# ============================================================================
# TASK 3: PRICE DISCRIMINATION BY INCOME LEVEL
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 3: DISCRIMINACIÓN DE PRECIOS POR NIVEL DE INGRESO")
print("=" * 80)
print()

def calculate_discriminated_income(df, project_name, num_households_by_income):
    """Calculate revenue with price discrimination"""
    print(f"\n{project_name.upper()}")
    print("-" * 60)
    
    # Map income categories to household numbers
    # Assumption: distribute households proportionally based on sample
    income_distribution = df.groupby('Income_Category').size() / len(df)
    
    print(f"\nDistribución de ingresos en la muestra:")
    for income_cat, proportion in income_distribution.items():
        if income_cat != 'Unknown':
            print(f"  {income_cat}: {proportion*100:.1f}%")
    
    # Calculate mean DAP by income level
    mean_dap_by_income = df.groupby('Income_Category')['DAP'].mean()
    
    # Calculate aggregate income with discrimination
    total_revenue_ars = 0
    total_revenue_ars_by_income = {}
    
    print(f"\nIngreso con Discriminación de Precios:")
    print(f"{'Nivel de Ingreso':<40} {'Hogares':<15} {'DAP/Hogar':<15} {'Ingreso ARS':<20}")
    print("-" * 90)
    
    for income_cat in mean_dap_by_income.index:
        if income_cat != 'Unknown':
            households_in_category = int(num_households_by_income * income_distribution[income_cat])
            dap_per_household = mean_dap_by_income[income_cat]
            revenue = households_in_category * dap_per_household
            total_revenue_ars += revenue
            total_revenue_ars_by_income[income_cat] = revenue
            
            print(f"{income_cat:<40} {households_in_category:>13,} ${dap_per_household:>13,.2f} ${revenue:>18,.2f}")
    
    total_revenue_usd = total_revenue_ars / EXCHANGE_RATE
    
    print("-" * 90)
    print(f"{'TOTAL':<40} {'':>13} {'':>13} ${total_revenue_ars:>18,.2f}")
    print(f"\nIngreso anual Total (USD): ${total_revenue_usd:,.2f}")
    
    return {
        'total_revenue_ars': total_revenue_ars,
        'total_revenue_usd': total_revenue_usd,
        'by_income': total_revenue_ars_by_income,
        'income_distribution': income_distribution,
        'mean_dap_by_income': mean_dap_by_income
    }

discrimination_cloaca = calculate_discriminated_income(df_cloaca_clean, 'Cloaca', HOUSEHOLDS_CLOACAS)
discrimination_ptar = calculate_discriminated_income(df_ptar_clean, 'PTAR', HOUSEHOLDS_TOTAL_CITY)

# ============================================================================
# TASK 4: COMPARISON - WITH AND WITHOUT DISCRIMINATION
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 4: COMPARACIÓN - CON Y SIN DISCRIMINACIÓN DE PRECIOS")
print("=" * 80)
print()

def compare_scenarios(project_name, income_results, discrimination_results, num_households):
    """Compare revenue with and without price discrimination"""
    print(f"\n{project_name.upper()}")
    print("-" * 80)
    
    revenue_no_disc_mean = income_results['annual_income_ars_mean']
    revenue_no_disc_median = income_results['annual_income_ars_median']
    revenue_disc = discrimination_results['total_revenue_ars']
    
    print(f"\n1. SIN DISCRIMINACIÓN (usando Media): ${revenue_no_disc_mean:,.2f} ARS")
    print(f"   En USD: ${revenue_no_disc_mean/EXCHANGE_RATE:,.2f}")
    
    print(f"\n2. SIN DISCRIMINACIÓN (usando Mediana): ${revenue_no_disc_median:,.2f} ARS")
    print(f"   En USD: ${revenue_no_disc_median/EXCHANGE_RATE:,.2f}")
    
    print(f"\n3. CON DISCRIMINACIÓN: ${revenue_disc:,.2f} ARS")
    print(f"   En USD: ${revenue_disc/EXCHANGE_RATE:,.2f}")
    
    # Calculate differences
    diff_vs_mean = revenue_disc - revenue_no_disc_mean
    pct_diff_mean = (diff_vs_mean / revenue_no_disc_mean) * 100
    
    diff_vs_median = revenue_disc - revenue_no_disc_median
    pct_diff_median = (diff_vs_median / revenue_no_disc_median) * 100
    
    print(f"\nDIFERENCIAS:")
    print(f"  vs. Media: ${diff_vs_mean:,.2f} ({pct_diff_mean:+.1f}%)")
    print(f"  vs. Mediana: ${diff_vs_median:,.2f} ({pct_diff_median:+.1f}%)")
    
    print(f"\nIMPLICACIONES PARA SUBSIDIOS DEL ESTADO:")
    if diff_vs_mean > 0:
        print(f"  La discriminación de precios AUMENTA los ingresos en ${diff_vs_mean:,.2f} ARS")
        print(f"  Esto REDUCE potencialmente la necesidad de subsidios del Estado,")
        print(f"  ya que se pueden generar más ingresos propios sin cargar igual a todos.")
    else:
        print(f"  La discriminación de precios REDUCE los ingresos en ${abs(diff_vs_mean):,.2f} ARS")
        print(f"  Esto INCREMENTA la necesidad de subsidios del Estado.")
    
    print(f"\n  Análisis por nivel de ingreso:")
    lower_income = discrimination_results['income_distribution'].get('Menos de $ 20000', 0) + \
                   discrimination_results['income_distribution'].get('Entre $ 20000 y $ 30000', 0)
    print(f"    - Los hogares con menores ingresos pagan menos (subsidio implícito)")
    print(f"    - Los hogares con mayores ingresos pagan más (contribuyen más)")
    print(f"    - Esto tiene un efecto PROGRESIVO que reduce la carga sobre el Estado")
    
    return {
        'revenue_no_disc_mean': revenue_no_disc_mean,
        'revenue_no_disc_median': revenue_no_disc_median,
        'revenue_disc': revenue_disc,
        'diff_vs_mean': diff_vs_mean,
        'pct_diff_mean': pct_diff_mean
    }

comparison_cloaca = compare_scenarios('Cloaca', income_cloaca, discrimination_cloaca, HOUSEHOLDS_CLOACAS)
comparison_ptar = compare_scenarios('PTAR', income_ptar, discrimination_ptar, HOUSEHOLDS_TOTAL_CITY)

# ============================================================================
# TASK 5: BENEFITS FROM REDUCED BOTTLED WATER CONSUMPTION
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 5: BENEFICIO POR REDUCCIÓN DE CONSUMO DE AGUA EN BOTELLAS")
print("=" * 80)
print()

# Data from consignment
current_consumption_liters = 5  # liters per month (after improvement)
previous_consumption_liters = 10  # liters per month (before improvement)
reduction_liters_per_month = previous_consumption_liters - current_consumption_liters
price_per_liter = 0.50  # USD

reduction_per_household_per_year = reduction_liters_per_month * 12 * price_per_liter  # USD

print("Datos del Proyecto:")
print(f"  Consumo anterior: {previous_consumption_liters} litros/mes")
print(f"  Consumo actual: {current_consumption_liters} litros/mes")
print(f"  Reducción: {reduction_liters_per_month} litros/mes ({reduction_liters_per_month/previous_consumption_liters*100:.0f}%)")
print(f"  Precio promedio: ${price_per_liter}/litro")

print(f"\nBeneficio por Hogar:")
print(f"  Ahorro anual por hogar: ${reduction_per_household_per_year:.2f} USD")
print(f"  Ahorro anual por hogar: ${reduction_per_household_per_year * EXCHANGE_RATE:,.2f} ARS")

# Total benefit for all city households
total_benefit_water_usd = reduction_per_household_per_year * HOUSEHOLDS_TOTAL_CITY
total_benefit_water_ars = total_benefit_water_usd * EXCHANGE_RATE

print(f"\nBeneficio Total de la Ciudad ({HOUSEHOLDS_TOTAL_CITY} hogares):")
print(f"  Ahorro anual: ${total_benefit_water_usd:,.2f} USD")
print(f"  Ahorro anual: ${total_benefit_water_ars:,.2f} ARS")

# ============================================================================
# TASK 6: BENEFITS FROM SEWAGE SYSTEM CONNECTION (CESSPOOL PUMPING COST SAVINGS)
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 6: BENEFICIO POR ELIMINACIÓN DE COSTOS DE VACIADO DE POZOS")
print("=" * 80)
print()

cesspool_pumping_cost_per_year = 50  # USD per household per year

print("Situación sin Proyecto:")
print(f"  Hogares sin conexión a cloacas usan pozos negros")
print(f"  Costo de vaciado: ${cesspool_pumping_cost_per_year}/hogar/año")

print(f"\nBeneficio por Hogar que se Conecte:")
print(f"  Ahorro anual: ${cesspool_pumping_cost_per_year}/hogar/año USD")
print(f"  Ahorro anual: ${cesspool_pumping_cost_per_year * EXCHANGE_RATE:,.2f}/hogar/año ARS")

# Total benefit for households connecting to sewage system
# Note: Only HOUSEHOLDS_CLOACAS benefit from this, not the entire city
total_benefit_cesspool_usd = cesspool_pumping_cost_per_year * HOUSEHOLDS_CLOACAS
total_benefit_cesspool_ars = total_benefit_cesspool_usd * EXCHANGE_RATE

print(f"\nBeneficio Total ({HOUSEHOLDS_CLOACAS} hogares que se conectan):")
print(f"  Ahorro anual: ${total_benefit_cesspool_usd:,.2f} USD")
print(f"  Ahorro anual: ${total_benefit_cesspool_ars:,.2f} ARS")

# ============================================================================
# TASK 7 & 8: REVENUE PROJECTIONS (30 YEARS)
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 7: PROYECCIÓN DE INGRESOS DAP POR 30 AÑOS")
print("=" * 80)
print()

HORIZON_YEARS = 30
annual_growth_rate = 0.01  # Assume 1% population growth

print("Supuestos:")
print(f"  - Horizonte de evaluación: {HORIZON_YEARS} años")
print(f"  - Inicio de beneficios: Año 3 (después de conclusión de obras)")
print(f"  - DAP no se modifica en el tiempo")
print(f"  - Conectividad en año 3: {CONNECTIVITY_YEAR3*100:.0f}%")
print(f"  - Conectividad final (año 6+): {FINAL_CONNECTIVITY*100:.0f}%")
print()

# Connectivity schedule for cloacas (applies to DAP revenues)
connectivity_schedule = {}
for year in range(1, HORIZON_YEARS + 1):
    if year < 3:
        connectivity_schedule[year] = 0  # No income before year 3
    elif year == 3:
        connectivity_schedule[year] = CONNECTIVITY_YEAR3
    else:
        # Gradual increase from 80% to 100% between years 3-6
        # Linear interpolation
        progress = (year - 3) / (6 - 3)
        connectivity_schedule[year] = CONNECTIVITY_YEAR3 + (FINAL_CONNECTIVITY - CONNECTIVITY_YEAR3) * min(progress, 1)

def project_revenues(initial_annual_revenue, project_name, connectivity_schedule):
    """Project revenues for 30 years with connectivity schedule"""
    print(f"\n{project_name.upper()}")
    print("-" * 80)
    print(f"{'Año':<6} {'Conectividad':<15} {'Ingresos ARS':<20} {'Ingresos USD':<20} {'VP ARS':<20}")
    print("-" * 80)
    
    discount_rate = 0.05  # 5% discount rate
    total_pv_ars = 0
    total_pv_usd = 0
    annual_revenues = {}
    
    for year in range(1, HORIZON_YEARS + 1):
        connectivity = connectivity_schedule[year]
        
        # Adjust for population growth (after year 3)
        if year <= 3:
            yearly_revenue = initial_annual_revenue * connectivity
        else:
            growth_years = year - 3
            yearly_revenue = initial_annual_revenue * connectivity * ((1 + annual_growth_rate) ** growth_years)
        
        yearly_revenue_usd = yearly_revenue / EXCHANGE_RATE
        
        # Calculate present value (discount back to year 0)
        pv = yearly_revenue / ((1 + discount_rate) ** year)
        pv_usd = yearly_revenue_usd / ((1 + discount_rate) ** year)
        
        total_pv_ars += pv
        total_pv_usd += pv_usd
        annual_revenues[year] = yearly_revenue
        
        if year <= 6 or year % 5 == 0 or year == HORIZON_YEARS:
            print(f"{year:<6} {connectivity*100:>13.0f}% ${yearly_revenue:>18,.0f} ${yearly_revenue_usd:>18,.0f} ${pv:>18,.0f}")
    
    print("-" * 80)
    print(f"{'TOTAL PV':<22} {'':>13} {'':>20} {'':>20} ${total_pv_ars:>18,.0f}")
    print(f"TOTAL PV (USD): ${total_pv_usd:,.0f}")
    print(f"Promedio anual: ${sum(annual_revenues.values())/len(annual_revenues):,.0f} ARS")
    
    return {
        'total_pv_ars': total_pv_ars,
        'total_pv_usd': total_pv_usd,
        'annual_revenues': annual_revenues
    }

projection_cloaca_dap = project_revenues(income_cloaca['annual_income_ars_mean'], 'Cloaca (DAP)', connectivity_schedule)
projection_ptar_dap = project_revenues(income_ptar['annual_income_ars_mean'], 'PTAR (DAP)', connectivity_schedule)

# ============================================================================
# Project cost savings revenues (TASK 8)
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 8: PROYECCIÓN DE BENEFICIOS POR AHORRO DE COSTOS (30 AÑOS)")
print("=" * 80)
print()

def project_cost_savings(annual_benefit_per_household, num_households, project_name, cost_type):
    """Project cost savings benefits for 30 years"""
    print(f"\n{project_name.upper()} - {cost_type}")
    print("-" * 80)
    print(f"Beneficio anual por hogar: ${annual_benefit_per_household}/hogar")
    print(f"Número de hogares: {num_households}")
    print()
    print(f"{'Año':<6} {'Beneficio Anual ARS':<25} {'Beneficio Anual USD':<25} {'VP ARS':<20}")
    print("-" * 80)
    
    discount_rate = 0.05
    total_pv_ars = 0
    total_pv_usd = 0
    annual_benefits = {}
    
    for year in range(1, HORIZON_YEARS + 1):
        # Benefits start in year 3 and grow with population growth
        if year < 3:
            benefit = 0
        else:
            growth_years = year - 3
            yearly_benefit_usd = annual_benefit_per_household * num_households * ((1 + annual_growth_rate) ** growth_years)
            benefit = yearly_benefit_usd * EXCHANGE_RATE
        
        benefit_usd = benefit / EXCHANGE_RATE
        
        # Present value
        pv = benefit / ((1 + discount_rate) ** year)
        pv_usd = benefit_usd / ((1 + discount_rate) ** year)
        
        total_pv_ars += pv
        total_pv_usd += pv_usd
        annual_benefits[year] = benefit
        
        if year <= 6 or year % 5 == 0 or year == HORIZON_YEARS:
            print(f"{year:<6} ${benefit:>23,.0f} ${benefit_usd:>23,.0f} ${pv:>18,.0f}")
    
    print("-" * 80)
    print(f"{'TOTAL PV':<32} {'':>25} {'':>25} ${total_pv_ars:>18,.0f}")
    print(f"TOTAL PV (USD): ${total_pv_usd:,.0f}")
    
    return {
        'total_pv_ars': total_pv_ars,
        'total_pv_usd': total_pv_usd,
        'annual_benefits': annual_benefits
    }

projection_water_savings = project_cost_savings(reduction_per_household_per_year, HOUSEHOLDS_TOTAL_CITY, 
                                                 'BENEFICIOS', 'Reducción de Agua en Botellas')

projection_cesspool_savings = project_cost_savings(cesspool_pumping_cost_per_year, HOUSEHOLDS_CLOACAS, 
                                                    'BENEFICIOS', 'Eliminación de Costos de Pozos Negros')

# ============================================================================
# TASK 9: FISHERY AND TOURISM BENEFITS
# ============================================================================
print("\n" + "=" * 80)
print("TAREA 9: PROPUESTAS PARA BENEFICIOS EN SECTOR PESQUERO Y TURISMO")
print("=" * 80)
print()

print("""
METODOLOGÍAS PROPUESTAS PARA ESTIMAR BENEFICIOS EN PESCA Y TURISMO:

1. BENEFICIOS EN EL SECTOR PESQUERO:
   ─────────────────────────────────
   
   A. Incremento de la Biomasa de Peces:
      • Realizar estudios de biomonitoreo pregrado y postgrado para medir:
        - Densidad y biomasa de poblaciones de peces
        - Recuperación de especies comercialesantes y después del proyecto
      • Multiplicar la biomasa adicional por precio de mercado
      • Usar modelos de dinámica poblacional (stock assessment)
   
   B. Reducción de Pérdidas Actuales:
      • Estudiar la pérdida de pesca actual por contaminación
      • Datos de pescadores (captura por unidad de esfuerzo - CPUE)
      • Comparar CPUE pre y post proyecto
      • Estimar disminución de contaminación en costas
   
   C. Metodología de Precios Hedónicos:
      • Valores de permisos de pesca comercial
      • Precios de cuotas de pesca
      • Precio implícito de la mejora ambiental


2. BENEFICIOS EN EL SECTOR TURISMO:
   ────────────────────────────────
   
   A. Uso Recreativo de Playas y Ríos:
      • Encuestas de visitantes a playas/ríos (como DAP)
      • Preguntar disposición a pagar por playas limpias
      • Estimar número de visitantes actuales vs. potenciales
      • Calcular días/visitante antes y después del proyecto
   
   B. Metodología de Costo de Viaje:
      • Identificar sitios limpios similares en la región
      • Medir costo de transporte para visitantes
      • Usar regresión para estimar demanda por recreación
      • Calcular beneficio del cambio de calidad ambiental
   
   C. Valor de Sitios Turísticos:
      • Estudiar hoteles, restaurantes cercanos
      • Estimar aumento de valor de propiedad costera
      • Usar precios hedónicos (precio de propiedades)
      • Relacionar con distancia a ríos/playas contaminados vs. limpios
   
   D. Empleo Generado:
      • Estimar empleo nuevo: guías turísticos, operadores de excursiones
      • Empleados en hoteles y restaurantes
      • Salarios promedio del sector
      • Multiplicador económico (3-5x según ruralidad)


3. METODOLOGÍA INTEGRADA RECOMENDADA:
   ──────────────────────────────────
   
   • Línea base: Datos pre-proyecto (año 0-1)
     - Estudios de calidad de agua y sedimentos
     - Conteos de peces
     - Encuestas de turismo existente
     - Ingresos de pescadores
   
   • Monitoreo: Años 3, 6, 10, 15, 20, 30
     - Repetir todos los estudios
     - Documentar cambios ambientales
     - Documentar cambios en ingresos
   
   • Análisis de Contrafáctico:
     - Estimar qué hubiese pasado SIN proyecto
     - Usar ciudades similares como comparación (diff-in-diff)
     - Controlar por otras variables (cambios macroeconómicos)
   
   • Análisis de Sensibilidad:
     - Calcular beneficios con escenarios optimista/pesimista
     - Variar tasas de recuperación de peces
     - Variar elasticidad precio de demanda turística


ESTIMACIÓN PRELIMINAR (CONSERVADORA):

   A. Pesca:
      • Supuesto: Recuperación de 20% de biomasa perdida
      • Captura actual: datos locales
      • Precio promedio: $5-10 USD/kg
      • Resultado: análisis caso a caso
   
   B. Turismo:
      • Incremento de visitantes: 50% con playas limpias
      • Gasto promedio visitante: $50-100 USD
      • Ocupación actual de hoteles: datos de INDEC
      • Resultado: análisis caso a caso


NOTAS IMPORTANTES:
━━━━━━━━━━━━━━━━━

• Los beneficios en pesca y turismo podrían representar 30-50% de los 
  beneficios totales del proyecto para ciudades costeras

• Es CRÍTICO no incluirlos hasta tener datos sólidos (sesgo conservador 
  en el análisis actual es apropiado)

• Se recomienda ejecutar estudios de línea base ANTES de invertir, para 
  poder medir impacto real

• Coordinar con universidades locales y organizaciones de pesca para 
  monitoreo participativo
""")

# ============================================================================
# SUMMARY TABLE
# ============================================================================
print("\n" + "=" * 80)
print("RESUMEN FINANCIERO - VALOR PRESENTE (30 AÑOS, TASA DESCUENTO 5%)")
print("=" * 80)
print()

summary_data = {
    'Componente': [
        'PTAR (DAP)',
        'Cloaca (DAP)',
        'Reducción Agua Botellas',
        'Eliminación Pozos Negros',
        'TOTAL'
    ],
    'VP en ARS': [
        projection_ptar_dap['total_pv_ars'],
        projection_cloaca_dap['total_pv_ars'],
        projection_water_savings['total_pv_ars'],
        projection_cesspool_savings['total_pv_ars'],
        projection_ptar_dap['total_pv_ars'] + projection_cloaca_dap['total_pv_ars'] + 
        projection_water_savings['total_pv_ars'] + projection_cesspool_savings['total_pv_ars']
    ],
    'VP en USD': [
        projection_ptar_dap['total_pv_usd'],
        projection_cloaca_dap['total_pv_usd'],
        projection_water_savings['total_pv_usd'],
        projection_cesspool_savings['total_pv_usd'],
        projection_ptar_dap['total_pv_usd'] + projection_cloaca_dap['total_pv_usd'] + 
        projection_water_savings['total_pv_usd'] + projection_cesspool_savings['total_pv_usd']
    ]
}

df_summary = pd.DataFrame(summary_data)
print(df_summary.to_string(index=False))

print("\n" + "=" * 80)
print("FIN DEL ANÁLISIS")
print("=" * 80)
