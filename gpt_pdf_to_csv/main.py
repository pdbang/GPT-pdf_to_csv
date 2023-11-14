from gpt_pdf_to_csv.scripts import tables_utils, gpt_utils
import os
from io import StringIO
from pandas import DataFrame

prompt_cols_base = "Ton objectif est de retrouver les noms de lignes et de colonnes adaptés dans ce csv qui est corrompu. Tu écriras les paramètres de la fonction sous forme de liste comme dans python : ['*nom*', '*nom*']."
prompt_values_base = "Tu dois interpréter le csv qui te sera donné par l'utilisateur pour choisir les valeurs pertinentes pour les paramètres de la fonction to_csv."

def set_openai_api_key(openai_api_key: str):
    os.environ["OPENAI_API_KEY"] = openai_api_key

def basic_pdf_to_csv(filename: str) -> StringIO:
    df = tables_utils.pdf_to_df(filename)
    csv_data = StringIO()
    df.to_csv(csv_data)
    return csv_data

def gpt_rows_and_cols(csv_data, system_prompt: str) -> (list, list):
    system_prompt = prompt_cols_base + "\n" + system_prompt
    return gpt_utils.get_cols_and_rows(csv_data, system_prompt)

def gpt_csv_to_df(csv_data, rows: list, cols: list, system_prompt: str) -> DataFrame:
    system_prompt = prompt_values_base + "\n" + system_prompt
    dico = gpt_utils.get_csv_with_cols(csv_data, system_prompt, rows, cols)
    return tables_utils.to_csv(**dico)