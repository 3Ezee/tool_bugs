# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:45:16 2018

@author: Ezequiel
"""
from src.DataBug import DataBug
from src.FileCreator import FileCreator
from src.DatabaseManager import DatabaseManager
import pandas as pd

bug = DataBug()
bug.id_number = 1222234
print(bug.id_number)
bug.description = "description"
bug.number = 2654
pd.rea
bug.image_path = "asddsa"
bug.incident = 132564
bug.list_hours = 9
bug.modify_files = "$ felino/ventas/kontroller \n$ felino/ventas/ent_comprobante"
bug.technical_problem = "problem"
bug.solution = "solution"
bug.tests = "bla bla"

print(bug)

bugFile = FileCreator("C:\\bugs\\bug_", str(bug.number)+".txt", bug.modify_files)

dm = DatabaseManager()
dm.write(bug.id_number,
         bug.number,
         bug.description,
         bug.technical_problem,
         bug.solution,
         bug.image_path,
         bug.incident,
         bug.modify_files,
         bug.list_hours)
