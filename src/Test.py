# -*- coding: utf-8 -*-
"""
Created on Wed May 16 01:45:16 2018

@author: Ezequiel
"""
from src.DataBug import DataBug

bug = DataBug()
bug.id_number = 1222234
print(bug.id_number)
bug.description = "description"
bug.number = 2654

bug.image_path = "asddsa"
bug.incident = 132564
bug.list_hours = 9
bug.modify_prgs = "asdsd"
bug.technical_problem = "problem"
bug.tests = "bla bla"

print(bug)
