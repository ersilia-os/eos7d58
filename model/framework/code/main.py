# imports
import os
import csv
import sys

from admet_ai import ADMETModel

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    model = ADMETModel()
    preds = model.predict(smiles=smiles_list)
    return preds

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]
    print(smiles_list)

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# rename columns
with open(os.path.join(root, "..", "columns", "run_columns.csv"), "r") as f:
    reader = csv.reader(f)
    next(reader)
    columns = []
    for r in reader:
        columns += [r[0]]
rename = dict((c0, c1) for c0, c1 in zip(list(outputs.columns), columns))
outputs = outputs.rename(columns=rename)
outputs.to_csv(output_file, index=False)
