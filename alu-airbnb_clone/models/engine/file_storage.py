"""
FileStorage class serializes instances into JSON File and
deserializes JSON File to instances
"""
import json

class FileStorage():
    """
    Class FileStorage
    Represent an abstracted storage test_engine.

    It serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    #Private class attributes
    __file_path = 'file.json'
    __objects = dict() #__objects = {}

    #Public instance methods
    def all(self):
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file __file_path"""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass