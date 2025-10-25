import pandas as pd
import numpy as np

def limpieza_nombres_columnas_airbnb(df):
    """
    Renombra columnas clave para facilitar el trabajo
    y convierte todos los nombres a minúsculas.
    """
    print("Iniciando limpieza de nombres de columnas...")

    df_renombrado = df.rename(columns={
        "NAME": "property_name",
        "host id": "host_id",
        "host name": "host_name",
        "neighbourhood group": "neighbourhood_group",
        "neighbourhood": "neighbourhood",
        "Construction year": "construction_year",
        "room type": "room_type",
        "number of reviews": "number_of_reviews",
        "reviews per month": "reviews_per_month",
        "review rate number": "review_rate_number",
        "availability 365": "availability_365",
        "service fee": "service_fee"
    })

    df_renombrado.columns = df_renombrado.columns.str.lower()

    print("Nombres de columnas normalizados correctamente.")
    return df_renombrado


def convertir_anio_construccion(df):
    """
    Convierte 'construction_year' a tipo Int64 si existe.
    """
    if "construction_year" in df.columns:
        print("Convirtiendo 'construction_year' a Int64...")
        df["construction_year"] = pd.to_numeric(df["construction_year"], errors='coerce').astype("Int64")
    else:
        print("Columna 'construction_year' no encontrada. Saltando conversión.")
    return df


def limpieza_price_y_service_fee(df):
    """
    Elimina símbolos como '$' y convierte 'price' y 'service_fee' a float.
    """
    print("Limpiando columnas 'price' y 'service_fee'...")

    for col in ["price", "service_fee"]:
        if col in df.columns:
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
    
    return df


def eliminar_filas_faltantes_airbnb(df):
    """
    Elimina filas con datos esenciales faltantes:
    'property_name', 'neighbourhood_group', 'price'
    """
    print("Eliminando filas con información faltante esencial...")

    filas_antes = len(df)
    df_limpio = df.dropna(subset=["property_name", "neighbourhood_group", "price"], how="any").reset_index(drop=True)
    filas_despues = len(df_limpio)

    print(f"Filas eliminadas: {filas_antes - filas_despues}")
    return df_limpio


def rellenar_valores_host_verified(df):
    """
    Rellena 'host_identity_verified' faltantes con 'unverified' (no verificado).
    """
    if "host_identity_verified" in df.columns:
        print("Rellenando valores faltantes en 'host_identity_verified' con 'unverified'...")
        df["host_identity_verified"] = df["host_identity_verified"].fillna("unverified")
    return df
