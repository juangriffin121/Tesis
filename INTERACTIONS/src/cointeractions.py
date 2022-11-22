import json

with open('../processed/App/App_interactions.json','r') as f:
  App_dict = json.load(f)

names = ['TFRC','ACP2','CTLA4','EGFR','ASGR','L1CAM','LAMP1']

Anotated_interactions_dict = {}
for name in names:
  with open(f'../processed/App/Anotated_instances/{name}.json','r') as f:
    Anotated_interactions_dict[name] = json.load(f)

cointeractions = []
for App_interacting_prot in App_dict:
  for name in names:
    for Anot_int in Anotated_interactions_dict[name]:
      print(App_interacting_prot,Anot_int)
      if App_dict[App_interacting_prot]['id'] == Anotated_interactions_dict[name][Anot_int]['id']:
       cointeractions.append(App_interacting_prot + f' interacciona con {name} ademas que con App') #App_dict[App_interacting_prot]['id']

for cointeraction in cointeractions:
  print(cointeraction)
  
#El complejo adaptor protein que elm dice que TRG endocytyc interacciona hay distintos
#App interacciona con subunidad mu de AP4 mientras que las subunidades mu de otros AP
#Interaccionan con las ptras prots