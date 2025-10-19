import pandas as pd
import os
# ruta absoluta de la carpeta donde está el script (.../scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
 
# construir la ruta del archivo csv de data
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "Airbnb_Open_Data.csv")
 
# creacion de funcion
def cargar_datos(path):
    print(f"Cargando datos desde {path}...")
   
    try:
        df = pd.read_csv(path)
        print("Datos han sido cargados!!!")
        return df
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo en {path}")
        print("Asegurate de tener el archivo en la carpeta 'data'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado {e}")
        return None
# ¿este archivo se está ejecutando directamente por el usuario o está siendo importado por otro script?
if __name__ == "__main__":
    # indica dónde está el script actual
    print(f"Ejecutando script desde: {os.path.abspath(__file__)}")
   
    # llama a la función de arriba para cargar el csv
    dataframe_juegos = cargar_datos(DATA_PATH)
   
    if dataframe_juegos is not None:
        print("\n---Primeras 5 filas---")
        print(dataframe_juegos.head())
       
        print("\n---Información del DataFrame---")
        dataframe_juegos.info()
 
