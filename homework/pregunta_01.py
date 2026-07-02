"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    df = pd.read_fwf(
        "files/input/clusters_report.txt",
        colspecs=[(3, 9), (9, 25), (25, 41), (41, None)],
        names=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
        skiprows=4,
    )

    df["cluster"] = df["cluster"].ffill().astype(int)
    df["cantidad_de_palabras_clave"] = df["cantidad_de_palabras_clave"].ffill().astype(int)
    df["porcentaje_de_palabras_clave"] = (
        df["porcentaje_de_palabras_clave"]
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
        .ffill()
        .astype(float)
    )

    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
    )

    df = (
        df.groupby(
            ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave"],
            sort=False,
        )["principales_palabras_clave"]
        .apply(lambda x: " ".join(x.dropna()))
        .reset_index()
    )

    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.rstrip(".")
    )

    return df


print(pregunta_01())

