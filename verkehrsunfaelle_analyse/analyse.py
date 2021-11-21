from pathlib import Path

import pandas as pd

import verkehrsunfaelle_analyse.config as config

if __name__ == "__main__":
    df = pd.read_csv(config.DATA_COMPLETE_PATH)

    # df_filt = df[
    #     [
    #         "vu_ort",
    #         "vu_hoehe",
    #         "datum",
    #         "uhrzeit",
    #         "datetime",
    #         "fg",
    #         "rf",
    #         "mofa",
    #         "kkr",
    #         "krad",
    #         "pkw",
    #         "lkw",
    #         "kom",
    #         "sonstige",
    #         "source_file",
    #     ]
    # ]

    df_promenade_kanal = df[
        (
            df["vu_ort"].str.lower().str.contains("promenade")
            | df["vu_ort"].str.lower().str.contains("kanal")
            | df["vu_ort"].str.lower().str.contains("neubrück")
        )
        & (
            df["vu_hoehe"].str.lower().str.contains("promenade")
            | df["vu_hoehe"].str.lower().str.contains("kanal")
            | df["vu_hoehe"].str.lower().str.contains("neubrück")
        )
    ]

    df_promenade_kanal.to_csv(config.ANALYSIS_OUTPUT_PATH)
    df_promenade_kanal.to_excel(Path(config.ANALYSIS_OUTPUT_PATH).with_suffix(".xlsx"))

    df = pd.read_csv(config.DATA_COMPLETE_UNFALLATLAS_PATH)

    # filter for promenade/neubrueckentor
    df_promenade_kanal = df[
        (df["XGCSWGS84"] >= config.REF_SOUTH_WEST[1])
        & (df["XGCSWGS84"] <= config.REF_NORTH_EAST[1])
        & (df["YGCSWGS84"] >= config.REF_SOUTH_WEST[0])
        & (df["YGCSWGS84"] <= config.REF_NORTH_EAST[0])
    ]

    df_promenade_kanal.to_csv(config.UNFALLATLAS_ANALYSIS_OUTPUT_PATH)
    df_promenade_kanal.to_excel(
        Path(config.UNFALLATLAS_ANALYSIS_OUTPUT_PATH).with_suffix(".xlsx")
    )
