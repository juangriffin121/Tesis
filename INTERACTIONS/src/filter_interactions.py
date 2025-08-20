import pandas as pd
import json
import numpy as np

# change the name to any of the proteins in the raw /App/Anotated_instances directory
name = "LAMP1"

df = pd.read_csv(f"../raw/App/Anotated_instances/{name}.tsv", "\t")

df1 = df[df.node1 == name]
df2 = df[df.node2 == name]

df1.set_index("node2", inplace=True)
df2.set_index("node1", inplace=True)

interact_dict = {}
for prot in df1.transpose():
    items_dict = {}
    for item in df1:
        if item != "node1":
            if item != "node1_string_id":
                if item != "node2":
                    if item == "node2_string_id":
                        items_dict["id"] = df1[item][prot]
                    else:
                        items_dict[item] = df1[item][prot]
    interact_dict[prot] = items_dict
for prot in df2.transpose():
    items_dict = {}
    for item in df2:
        if item != "node1":
            if item != "node2_string_id":
                if item != "node2":
                    if item == "node1_string_id":
                        items_dict["id"] = df2[item][prot]
                    else:
                        items_dict[item] = df2[item][prot]
    interact_dict[prot] = items_dict

for prot in interact_dict:
    for item, value in dict.items(interact_dict[prot]):
        if type(value) == np.int64:
            interact_dict[prot][item] = int(value)
        if type(value) == np.float64:
            interact_dict[prot][item] = float(value)

with open(f"../processed/App/Anotated_instances/{name}.json", "w+") as f:
    json.dump(interact_dict, f)

print("done")
