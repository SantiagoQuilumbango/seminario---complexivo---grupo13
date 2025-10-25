# Libreria general
import os
# funciones de los scripts
from scripts.data_loader import cargar_datos 
from scripts.data_cleaning import (
    limpieza_nombres_columnas_airbnb, 
    convertir_anio_construccion, 
    limpieza_price_y_service_fee, 
    eliminar_filas_faltantes_airbnb, 
    rellenar_valores_host_verified
)
from scripts.data_imputation import (
    imputar_anio_construccion, 
    rellenar_mediana_columna,
    imputacion_reviews_y_precios
)
from scripts.data_new_features import (
    crear_costo_total
)
from scripts.data_saving import guardar_datos_limpios
# ruta absoluta de la carpeta donde está el script (.../scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
 
# construir la ruta del archivo csv de data
DATA_PATH = os.path.join(SCRIPT_DIR, ".", "data", "Airbnb_Open_Data.csv")
 
# nueva ruta de salida
PROCESSED_DATA_PATH = os.path.join(SCRIPT_DIR, "data", "processed", "Airbnb_clean.csv")

# ¿este archivo se está ejecutando directamente por el usuario o está siendo importado por otro script?
if __name__ == "__main__":
    # indica dónde está el script actual
    print(f"Ejecutando script desde: {os.path.abspath(__file__)}")
   
    # llama a la función de arriba para cargar el csv
    dataframe_juegos = cargar_datos(DATA_PATH)
   
    if dataframe_juegos is not None:
        # MÓDULO LIMPIEZA DE DATOS
        print("--- INICIANDO LIMPIEZA DE DATOS ---")
        df_limpio = limpieza_nombres_columnas_airbnb(dataframe_juegos)
        df_limpio = convertir_anio_construccion(df_limpio)
        df_limpio = limpieza_price_y_service_fee(df_limpio)
        df_limpio = eliminar_filas_faltantes_airbnb(df_limpio)
        df_limpio = rellenar_valores_host_verified(df_limpio)
        print("\n--- LIMPIEZA DE DATOS TERMINADA ---")

        # MÓDULO IMPUTACIÓN DE DATOS
        print("\n---INICIANDO IMPUTACIÓN DE DATOS---")
        df_procesado = imputar_anio_construccion(df_limpio)
        df_procesado["reviews_per_month"] = rellenar_mediana_columna(df_procesado["reviews_per_month"])
        df_procesado = imputacion_reviews_y_precios(df_procesado)#3
        print("\n---IMPUTACIÓN DE DATOS TERMINADO---")

        # MÓDULO NUEVAS COLUMNAS 
        print("\n---INICIANDO AGREGACIÓN NUEVAS COLUMNAS---")
        df_final = crear_costo_total(df_procesado)
        
        print("\n---AGREGACIÓN NUEVAS COLUMNAS TERMINADO---")
        
        # GUARDAR DATOS
        guardar_datos_limpios(df_final, PROCESSED_DATA_PATH)
        
        # AQUÍ TERMINÓ EL PIPELINE DE LIMPIEZA
        print("\n---PIPELINE TERMINADO---")
        
        print("\n---Información del DataFrame---")
        df_final.info(show_counts=True)
        
    else: 
        print("Ha ocurrido un error en la carga de datos")
    #wwwwww