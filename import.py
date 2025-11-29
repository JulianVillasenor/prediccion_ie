import kagglehub
import os
import shutil
import pandas as pd

# 1. Descargar dataset
path = kagglehub.dataset_download(
    "rakeshkapilavai/extrovert-vs-introvert-behavior-data"
)

print("Dataset descargado en:", path)
print("Archivos en el dataset:")
print(os.listdir(path))

# 2. Crear carpeta 'files' dentro del proyecto (si no existe)
project_dir = os.getcwd()  # B:\unison\reconocimiento_patrones\prediccion_ie
dest_dir = os.path.join(project_dir, "files")
os.makedirs(dest_dir, exist_ok=True)

# 3. Elegir el archivo bueno
src_csv = os.path.join(path, "personality_dataset.csv")  # este es el chido
dst_csv = os.path.join(dest_dir, "personality_dataset.csv")

# 4. Copiar a tu carpeta de trabajo
shutil.copy(src_csv, dst_csv)
print("CSV copiado a:", dst_csv)

# 5. Probar lectura con pandas
df = pd.read_csv(dst_csv)
print(df.head())
print(df.info())
