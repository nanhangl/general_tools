# the purpose of this script is to create a subset of a large dataset
# images are selected randomly to reduce bias

import os
import random
from shutil import copyfile

selected = []
os.chdir("img_dir")
main_dataset = "."
subset_dataset = "subset"
ls = os.listdir(main_dataset)
subset_dataset_size = 100

while len(selected) < subset_dataset_size:
    index = random.randint(0, len(ls) - 1)
    withoutExt = ls[index].split(".")[:-1]
    withoutExt = '.'.join(withoutExt)
    ext = ls[index].split(".")[-1]
    if index not in selected and ext == "png":
        copyfile(f"{main_dataset}/{ls[index]}",
                 f"{subset_dataset}/{ls[index]}")
        copyfile(f"{main_dataset}/annotations/{withoutExt}.xml",
                 f"{subset_dataset}/{withoutExt}.xml")
        selected.append(index)
