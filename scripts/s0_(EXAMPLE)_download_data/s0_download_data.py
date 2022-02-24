import json

# adds scripts/ and src/ folder: so you can import scripts/functions across project steps
import sys 
sys.path.append("../../src")
sys.path.append("../../scripts")

from data_filepaths import s0_balzac_books

# %%

# thanks to the sys.path.append("../../src") line, we can easily use functions from utils.py here:
from utils import useful_function 
useful_function() 

# %%

downloaded_list_of_books = [
    "madame bovary",
    "le père goriot"
]

# %%

with open(s0_balzac_books, "w") as f:
    json.dump(downloaded_list_of_books, f)
