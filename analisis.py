# ============================================
# 1. IMPORTAR LIBRERÍAS
# ============================================
import pandas as pd                    # Para manejar datos en tablas
import matplotlib.pyplot as plt        # Para crear gráficas

# ============================================
# 2. CARGAR DATOS
# ============================================
df = pd.read_csv('Datos/EDUCACION.csv', sep=';')  # Carga el archivo CSV usando separador ';'

# ============================================
# 3. EXPLORACIÓN INICIAL
# ============================================
print("=== Tamaño del dataset ===")
print(df.shape)                        # Muestra (filas, columnas)

print("\n=== Primeras 5 filas ===")
print(df.head())                       # Muestra las primeras 5 filas

print("\n=== Nombres de columnas ===")
print(df.columns.tolist())             # Lista de nombres de columnas

print("\n=== Información general ===")
print(df.info())                       # Tipos de datos y valores no vacíos por columna

print("\n=== Estadísticas básicas ===")
print(df.describe())                   # Promedio, mínimo, máximo de columnas numéricas

print("\n=== Valores vacíos por columna ===")
print(df.isnull().sum())               # Cuenta celdas vacías por columna

# ============================================
# 4. LIMPIEZA DE DATOS
# ============================================
# Elimina columnas con demasiados vacíos (más del 50% de los datos)
df = df.drop('TAMAÑO_PROMEDIO_DE_GRUPO', axis=1)
df = df.drop('SEDES_CONECTADAS_A_INTERNET', axis=1)

df_limpio = df.dropna()                # Elimina filas con al menos un valor vacío

print("\n=== Filas antes y después de limpiar ===")
print(df.shape)                        # Tamaño antes
print(df_limpio.shape)                 # Tamaño después

# ============================================
# 5. ANÁLISIS - DESERCIÓN POR DEPARTAMENTO
# ============================================
# Convierte la columna 'DESERCIÓN' de texto a número decimal
df_limpio['DESERCIÓN'] = df_limpio['DESERCIÓN'].str.replace('%', '').str.replace(',', '.').astype(float)

# Calcula el promedio de deserción por departamento
promedio_desercion = df_limpio.groupby('DEPARTAMENTO')['DESERCIÓN'].mean()
promedio_desercion = promedio_desercion.sort_values(ascending=False)  # Ordena de mayor a menor

# ============================================
# 6. GRÁFICA - DESERCIÓN POR DEPARTAMENTO
# ============================================
plt.figure(figsize=(12, 6))            
promedio_desercion.plot(kind='barh')   # Gráfica de barras horizontales
plt.title('Deserción promedio por departamento')  
plt.xlabel('Porcentaje de deserción')  
plt.ylabel('Departamento')             
plt.tight_layout()                     
plt.show()                             

# ============================================
# 7. ANÁLISIS - COBERTURA NETA POR AÑO
# ============================================
# Convierte la columna 'COBERTURA_NETA' de texto a número decimal
df_limpio['COBERTURA_NETA'] = df_limpio['COBERTURA_NETA'].str.replace('%', '').str.replace(',', '.').astype(float)

# Calcula el promedio de cobertura neta por año
promedio_cambio_anual = df_limpio.groupby('AÑO')['COBERTURA_NETA'].mean()
print(promedio_cambio_anual)

# Gráfica de línea para cobertura neta promedio por año
plt.figure(figsize=(12, 6))            
promedio_cambio_anual.plot(kind='line')   
plt.title('Cobertura neta promedio por año')  
plt.xlabel('AÑO')  
plt.ylabel('COBERTURA_NETA')             
plt.tight_layout()                     
plt.show()                             

# ============================================
# 8. ANÁLISIS - DESERCIÓN PROMEDIO POR AÑO
# ============================================
# Calcula el promedio de deserción por año
promedio_por_departamento_año = df_limpio.groupby('AÑO')['DESERCIÓN'].mean()
promedio_por_departamento_año = promedio_por_departamento_año.sort_index(ascending=True)  # Orden cronológico

# Gráfica de línea para deserción promedio por año
plt.figure(figsize=(12, 6))            
promedio_por_departamento_año.plot(kind='line')   
plt.title('Deserción promedio por año')  
plt.xlabel('AÑO')  
plt.ylabel('DESERCIÓN')             
plt.tight_layout()                     
plt.show()                             

# ============================================
# 9. ANÁLISIS - APROBACIÓN POR DEPARTAMENTO
# ============================================
# Convierte la columna 'APROBACIÓN' de texto a número decimal
df_limpio['APROBACIÓN'] = df_limpio['APROBACIÓN'].str.replace('%', '').str.replace(',', '.').astype(float)

# Calcula el promedio de aprobación por departamento
aprobacion_por_departamento = df_limpio.groupby('DEPARTAMENTO')['APROBACIÓN'].mean()
aprobacion_por_departamento = aprobacion_por_departamento.sort_values(ascending=False)

# Gráfica de barras horizontales para aprobación por departamento
plt.figure(figsize=(12, 6))            
aprobacion_por_departamento.plot(kind='barh')   
plt.title('Aprobación promedio por departamento')  
plt.xlabel('APROBACIÓN')  
plt.ylabel('DEPARTAMENTO')             
plt.tight_layout()                     
plt.show()    
