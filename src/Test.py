# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:45:16 2018

@author: Ezequiel
"""
from src.DataBug import DataBug
from src.FileCreator import FileCreator

bug = DataBug()
bug.id_number = 1222234
print(bug.id_number)
bug.description = "description"
bug.number = 2654

bug.image_path = "asddsa"
bug.incident = 132564
bug.list_hours = 9
bug.modify_files = "$ felino/ventas/kontroller \n$ felino/ventas/ent_comprobante"
bug.technical_problem = "problem"
bug.tests = "bla bla"

print(bug)

bugFile = FileCreator("C:\\bugs\\bug_", str(bug.number)+".txt", bug.modify_files)
