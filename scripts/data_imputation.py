import pandas as pd
import numpy as np

def imputar_anio_construccion(df):
    """
    Rellena los años de construcción faltantes usando la moda del mismo 'neighbourhood'
    (barrio). Si aún quedan nulos, los elimina.
    """
    print("Iniciando imputación de 'Construction year'...")

    df_imputado = df.copy()

    df_imputado["Construction year"] = df_imputado.groupby("neighbourhood")["Construction year"].transform(
        lambda x: x.fillna(x.mode().iloc[0]) if not x.mode().empty else x
    )

    # Eliminar filas que aún sigan sin año
    filas_antes = len(df_imputado)
    df_limpio = df_imputado.dropna(subset=["Construction year"], how="all").reset_index(drop=True)
    filas_despues = len(df_limpio)

    print(f"Filas eliminadas en este paso: {filas_antes - filas_despues}")

    return df_limpio


def rellenar_mediana_columna(serie):
    """
    Rellena los valores nulos de una serie usando su mediana (si existe).
    """
    mediana = serie.dropna().median()
    return serie.fillna(mediana) if pd.notna(mediana) else serie


def imputacion_reviews_y_precios(df):
    """
    Imputa 'reviews per month' y 'price' basándose en la mediana
    de las propiedades en el mismo 'neighbourhood_group'.
    Luego elimina las filas que aún queden con nulos.
    """
    print("Iniciando imputación de 'reviews per month' y 'price'...")

    df_imputado = df.copy()

    # Imputar valores faltantes con mediana por grupo
    df_imputado["reviews per month"] = df_imputado.groupby("neighbourhood_group")["reviews per month"].transform(rellenar_mediana_columna)
    df_imputado["price"] = df_imputado.groupby("neighbourhood_group")["price"].transform(rellenar_mediana_columna)

    # Eliminar filas restantes con valores nulos
    filas_antes = len(df_imputado)
    df_limpio = df_imputado.dropna(subset=["price", "reviews per month"], how="any").reset_index(drop=True)
    filas_despues = len(df_limpio)

    print(f"Filas eliminadas en este paso: {filas_antes - filas_despues}")

    return df_limpio
