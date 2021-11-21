import verkehrsunfaelle_analyse.config as config

import pandas as pd
from pathlib import Path


def statistik_polizei():
    # load the various files as dataframes

    all_df = []

    for csv_path in Path(config.ORIGINAL_DATA_FOLDER).glob("*.csv"):
        print(f"Loading {csv_path}")
        year_df = pd.read_csv(csv_path)

        # year_df["uhrzeit"] = year_df["uhrzeit"].fillna("00:00")
        # year_df["datetime"] = year_df.agg(
        #     lambda x: f"{x['datum']} {str(x['uhrzeit']).zfill(5 if ':' in str(x['uhrzeit']) else 4)}",
        #     axis=1,
        # )
        # year_df["datetime"] = pd.to_datetime(
        #     year_df["datetime"], infer_datetime_format=True, errors="coerce"
        # )

        year_df["source_file"] = str(csv_path.name)

        all_df.append(year_df)

    concat_df = pd.concat(all_df)

    # remove unnamed columns
    concat_df = concat_df.filter(
        [col for col in concat_df.columns if "Unnamed" not in col]
    )

    concat_df.to_csv(config.DATA_COMPLETE_PATH)


def statistik_unfallatlas():
    all_df = []

    for csv_path in (Path(config.ORIGINAL_DATA_FOLDER) / "unfallatlas").glob("*.csv"):
        # csv_path = "C:/Users/chris/workspace/open-data/Unfallstatistiken/csv/unfallatlas/Unfallorte2020_LinRef.csv"
        print(f"Loading {csv_path}")

        year_df = pd.read_csv(csv_path, delimiter=";")

        # select Muenster
        year_df = year_df[
            (year_df["ULAND"] == 5)
            & (year_df["UREGBEZ"] == 5)
            & (year_df["UKREIS"] == 15)
        ]

        if len(year_df) == 0:
            continue

        year_df["source_file"] = str(csv_path.name)
        all_df.append(year_df)

    concat_df = pd.concat(all_df)

    concat_df["XGCSWGS84"] = concat_df["XGCSWGS84"].str.replace(",", ".").astype(float)
    concat_df["YGCSWGS84"] = concat_df["YGCSWGS84"].str.replace(",", ".").astype(float)

    concat_df.to_csv(config.DATA_COMPLETE_UNFALLATLAS_PATH)


if __name__ == "__main__":
    statistik_polizei()
    statistik_unfallatlas()
