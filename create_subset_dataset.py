# the purpose of this script is to create a subset of a large dataset
# images are selected randomly to reduce bias

import os
import random
from shutil import copyfile

selected = []
os.chdir("image_directory")
main_dataset = ""
subset_dataset = ""
ls = os.listdir(main_dataset)
subset_dataset_size = 10

while len(selected) < subset_dataset_size:
    index = random.randint(0, len(ls) - 1)
    if index not in selected:
        copyfile(f"{main_dataset}/{ls[index]}",
                 f"{subset_dataset}/{ls[index]}")
        selected.append(index)
