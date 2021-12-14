#!/usr/bin/python3
'''module that contains Base Class'''
import json
import csv


class Base:
    '''Private Base Class Attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize class constructor'''
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns json representation of list of dictionaries'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''returns list of the JSON string'''
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''saves JSON representation of an object to a text file'''
        if list_objs is None:
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write("[]")
        else:
            list_of_dict = []
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file:
                file.write(Base.to_json_string(list_of_dict))

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if cls.__name__ == "Square":
            newobj = cls(1)
            newobj.update(**dictionary)
            return newobj
        if cls.__name__ == "Rectangle":
            newobj = cls(1, 1)
            newobj.update(**dictionary)
            return newobj

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances from a json file'''
        filename = cls.__name__ + ".json"
        list_objs = []
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                list_instance = Base.from_json_string(f.read())
                for dict in list_instance:
                    list_objs.append((cls.create(**dict)))
                return list_objs
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''saves CSV representation of an object to a text file'''
        if list_objs is None:
            with open(cls.__name__ + ".csv", 'w', encoding="utf-8") as file:
                file.write("[]")
        else:
            if cls.__name__ == "Rectangle":
                header = ['id', 'width', 'height', 'x', 'y']
            else:
                header = ['id', 'size', 'x', 'y']
            list_of_dict = []
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
            with open(cls.__name__ + ".csv", 'w', encoding="utf-8") as file:
                wr = csv.DictWriter(file, fieldnames=header)
                wr.writeheader()
                for dic in list_of_dict:
                    wr.writerow(dic)

    @classmethod
    def load_from_file_csv(cls):
        '''returns a list of instances from a csv file'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                reader = csv.DictReader(f)
                list_objs = []
                for row in reader:
                    for val in row:
                        row[val] = int(row[val])
                    list_objs.append((cls.create(**row)))
                return list_objs
        except IOError:
            return []
