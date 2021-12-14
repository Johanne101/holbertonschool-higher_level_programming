#!/usr/bin/python3
""" Module base clase """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ definition of instance atributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as file_js:
            dic_list = []
            if list_objs is None:
                for objects in list_objs:
                    dic_list.append(objects.to_dictionary())
                    file_js.write(cls.to_json_string(dic_list))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new_square = cls(1)
            new_square.update(**dictionary)
        if cls.__name__ == "Rectangle":
            new_rectangle = cls(1, 1)
            new_rectangle.update(**dictionary)
        return(new_rectangle)

    @classmethod
    def load_from_file(cls):
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as a_file:
                return [cls.create(**dict_o) for dict_o
                        in cls.from_json_string(a_file.read())]
        except IOError:
            return []

    """@classmethod
    def reset_nb_objects():
        Base._Base__nb_objects = 0
        """

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''saves list to CSV serialized file'''
        if list_objs is None:
            with open(cls.__name__ + ".csv", 'w', encoding="utf-8") as file:
                file.write("[]")
        else:
            if cls.__name__ == "Rectangle":
                attr_h = ['id', 'width', 'height', 'x', 'y']
            else:
                attr_h = ['id', 'size', 'x', 'y']
            dict_list = []
            for item in list_objs:
                dict_list.append(item.to_dictionary())
                wrt = csv.DictWriter(csv_file, fieldnames=list(attr_h))
                wrt.writeheader()
                for i in list_dict:
                    writer.writerow(i)

    @classmethod
    def load_from_file_csv(cls):
        '''Returns list of instances from csv file'''
        try:
            with open(cls.__name__ + ".csv", 'r', encoding="utf-8") as j_file:
                reader = csv.DictReader(j_file)
                objs_l = []
                for x in reader:
                    for val in x:
                        x[val] = int(x[val])
                    list_objs.append((cls.create(**dic)))
                return list_objs
        except IOError:
            return []
