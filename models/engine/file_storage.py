"""A class that serializes instances to a JSON file and
    deserializes JSON file to instances"""
import json


class FileStorage:
    """Class for storing and accessing data"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as s_file:
            s_dict = {key: value.to_dict() for key, value
                      in FileStorage.__objects.items()}
            json.dump(s_dict, s_file)

    def reload(self):
        """deserializes the JSON file to __objects(if file exist """
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as r_file:
            obj_dict = json.load(r_file)
            obj_dict = {key: self.classes()[val["__class__"]](**val)
                        for key, val in obj_dict.items()}
            FileStorage.__objects = obj_dict
