import os
import subprocess
import zipfile
import pandas as pd

COMP_NAME = "playground-series-s5e7"

# Directorio del proyecto (donde está este archivo)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Carpeta donde guardaremos los datos
DATA_DIR = os.path.join(PROJECT_DIR, "files")
os.makedirs(DATA_DIR, exist_ok=True)

ZIP_PATH = os.path.join(DATA_DIR, f"{COMP_NAME}.zip")
TRAIN_PATH = os.path.join(DATA_DIR, "train.csv")

def download_data():
    """Descarga los datos de Kaggle si no existen."""
    if os.path.exists(TRAIN_PATH):
        print("✅ train.csv ya existe en 'files/', no se descarga nada.")
        return

    print("⬇️ Descargando datos desde Kaggle...")
    # Necesitas tener el CLI de Kaggle instalado y configurado:
    #   pip install kaggle
    #   y tu kaggle.json en la ruta adecuada
    subprocess.run(
        [
            "kaggle", "competitions", "download",
            "-c", COMP_NAME,
            "-p", DATA_DIR
        ],
        check=True
    )

    # Buscar el zip descargado (por si el nombre exacto cambia)
    zips = [f for f in os.listdir(DATA_DIR) if f.endswith(".zip")]
    if not zips:
        raise FileNotFoundError("No se encontró ningún .zip en la carpeta 'files' después de la descarga.")

    zip_file = os.path.join(DATA_DIR, zips[0])
    print(f"📦 Descomprimiendo: {zip_file}")

    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(DATA_DIR)

    print("✅ Archivos extraídos en:", DATA_DIR)


def main():
    download_data()

    print("📁 Archivos en 'files/':")
    print(os.listdir(DATA_DIR))

    if os.path.exists(TRAIN_PATH):
        df = pd.read_csv(TRAIN_PATH)
        print("\n🧾 Primeras filas de train.csv:")
        print(df.head())
        print("\nℹ️ Info de train.csv:")
        print(df.info())
    else:
        print("⚠️ No se encontró train.csv en 'files/'.")


if __name__ == "__main__":
    main()
