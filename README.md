# GPT-pdf_to_csv

Ce repository a pour objectif de compléter l'utilisation de tabula pour extraire des tables de pdf en utilisant gpt-3.5.

Exemple d'utilisation :
```
%pip install --upgrade git+https://github.com/pdbang/GPT-pdf_to_csv.git 
import gpt_pdf_to_csv as gptable

openai_api_key = "xxx"
system_prompt_cols = "Les colonnes sont Valeurs, Unités et Pourcentage. Pour les lignes, fais bien attention à ne garder que les noms de lignes qui respectent certaines conditions"
system_prompt_values = "Bon courage"
gptable.set_openai_api_key(openai_api_key)
csv_data = gptable.basic_pdf_to_csv("pdf/fiche_technique.pdf")
rows, cols = gptable.gpt_rows_and_cols(csv_data, system_prompt_cols)
df = gptable.gpt_csv_to_df(csv_data, rows, cols, system_prompt_values)
```