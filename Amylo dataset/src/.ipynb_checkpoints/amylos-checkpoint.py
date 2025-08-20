import pandas as pd
import json

descriptions = pd.read_csv(r'C:\Users\Usuario\my_scripts\tesina\Amylo dataset\raw\kung_funding - description.csv')
df = pd.read_csv(r'C:\Users\Usuario\my_scripts\tesina\Amylo dataset\raw\kung_funding - data.csv')
fields = {}
for field,description in zip(descriptions['field'],descriptions['definition']):
  fields[field] = description
df.set_index('uniprot_id', inplace = True)
df_prot = df.transpose()
prots = {}
for ID in df_prot:
  prots[ID] = {'name' : df_prot[ID]['uniprot_protein_name'],
               'category_amyloids' : df_prot[ID]['category_amyloids'],
               'amypro_category' : df_prot[ID]['amypro_category'],
               'amyloid_peptides' : df_prot[ID]['amyloid_peptides']}
with open(r'C:\Users\Usuario\my_scripts\tesina\Amylo dataset\processed\kung_funding_filtered.json','w') as f:
  json.dump(prots,f)
 