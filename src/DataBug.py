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
        self._modify_prgs = ""
        self._list_hours = 0
        self._tests = ""

    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value

    @id_number.deleter
    def id_number_deleter(self):
        del self._id_number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @number.deleter
    def number_deleter(self):
        del self._number

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @description.deleter
    def description_deleter(self):
        del self._description

    @property
    def technical_problem(self):
        return self._technical_problem

    @technical_problem.setter
    def technical_problem(self, value):
        self._technical_problem = value

    @technical_problem.deleter
    def technical_problem_deleter(self):
        del self._technical_problem

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, value):
        self._image_path = value

    @image_path.deleter
    def image_path_deleter(self):
        del self._image_path

    @property
    def incident(self):
        return self._incident

    @incident.setter
    def incident(self, value):
        self._incident = value

    @incident.deleter
    def incident_deleter(self):
        del self._incident

    @property
    def modify_prgs(self):
        return self._modify_prgs

    @modify_prgs.setter
    def modify_prgs(self, value):
        self._modify_prgs = value

    @modify_prgs.deleter
    def modify_prgs_deleter(self):
        del self._modify_prgs

    @property
    def list_hours(self):
        return self._list_hours

    @list_hours.setter
    def list_hours(self, value):
        self._list_hours = value

    @list_hours.deleter
    def list_hours_deleter(self):
        del self._list_hours

    @property
    def tests(self):
        return self._tests

    @tests.setter
    def tests(self, value):
        self._tests = value

    @tests.deleter
    def tests_deleter(self):
        del self._tests

    def __str__(self):
        return str(self._id_number) + "," + str(self._number) + "," + \
               self._description + "," + self._technical_problem + "," + \
               self._image_path + "," + str(self._incident) + "," + \
               self._modify_prgs + "," + str(self._list_hours) + "," + \
               self._tests
