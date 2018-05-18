# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:16:44 2018

@author: Ezequiel
"""


class DataBug:

    def __init__(self):
        self._id_number = 0
        self._number = 0
        self._description = ""
        self._technical_problem = ""
        self._image_path = ""
        self._incident = 0
        self._modify_files = ""
        self._list_hours = 0
        self._tests = ""

    def update(self, id_number, number, description, technical_problem, image_path, incident, modify_files, list_hours,
               tests):
        self._id_number = id_number
        self._number = number
        self._description = description
        self._technical_problem = technical_problem
        self._image_path = image_path
        self._incident = incident
        self._modify_files = modify_files
        self._list_hours = list_hours
        self._tests = tests

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def technical_problem(self):
        return self._technical_problem

    @technical_problem.setter
    def technical_problem(self, value):
        self._technical_problem = value

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value

    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):
        self._incident = value

    @property
    def modify_files(self):
        return self._modify_files

    @modify_files.setter
    def modify_files(self, value):
        self._modify_files = value

    @property
    def list_hours(self):
        return self._list_hours

    @list_hours.setter
    def list_hours(self, value):
        self._list_hours = value

    @property
    def tests(self):
        return self._tests

    @tests.setter
    def tests(self, value):
        self._tests = value

    def __str__(self):
        return (str(self._id_number) + "," + str(self._number) + "," +
                self._description + "," + self._technical_problem + "," +
                self._image_path + "," + str(self._incident) + "," +
                self._modify_files + "," + str(self._list_hours) + "," +
                self._tests)
