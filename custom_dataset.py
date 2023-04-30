import os
import json
import pandas as pd

df = pd.read_csv("brain_stroke.csv")
print("Please ensure that your dataset has columns and data like below:")
print(df.head())
print()
print()
print()


# Prompt the user for the dataset filename and load the data into a Pandas DataFrame
filename = input("Enter the file name (also ensure that file is present in Stroke-Prediction Folder): ")
if not os.path.isfile(filename):
    print("Error: The file does not exist.")
    exit()

# Write the filename to a JSON file for future use
config = {"filename": filename}
with open("config.json", "w") as f:
    json.dump(config, f)

print("Please wait it can take upto 30-60 mins")
#Run the Brain_Stroke_Prediction.ipynb
os.system("jupyter nbconvert --to notebook --execute Brain_Stroke_Prediction.ipynb")

print("Images and models are saved in the folders")
print("Please see the detailed results in the Brain_Stroke_Prediction.ipynb")

