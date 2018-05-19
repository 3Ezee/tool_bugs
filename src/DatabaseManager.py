# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:17:44 2018

@author: Ezequiel
"""

import pandas as pd


class DatabaseManager:

    def __init__(self, direction):
        self.df = None
        self.direction = direction
        self.columns_names = ['id','bug','descripción','problema técnico','solución','ruta imagen','incidentes','archivos modificados','horas']

        # self.connect(self.direction)

    def connect(self, direction):
        try:
            self.df = pd.read_csv(direction, names = self.columns_name)

        except IOError:
            print("Could not read file: ", direction)

    def write(self,
              id_number,
              number,
              description,
              technical_problem,
              solution,
              image_path,
              incident,
              modify_files,
              list_hours):

        information = [str(id_number),
                       str(number),
                       description,
                       technical_problem,
                       solution,
                       image_path,
                       incident,
                       modify_files,
                       str(list_hours)]
        self.df = pd.DataFrame(data=information, columns = self.columns_names)
        self.df.to_csv(self.direction, index=False, header=False)
