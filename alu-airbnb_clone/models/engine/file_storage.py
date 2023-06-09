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
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        """
        with open(self.__file_path, 'r') as file:
            json_data = file.read()

        self.__objects = json.loads(json_data)
        """try:
            with open(self.__file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    self.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError or NameError:
            pass"""


"""Alternative"""
class FilesTorage():
    """Serializes instances to JSON file and
    Deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """Returns the dictionary object"""
        return self.__objects
    
    def new(self, obj):
        """Adds to the object dictionary a new obj by <class name>.id"""
        
        classname = obj.__class__name
        id = obj.id
        key = f"{classname}.{id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __object to the JSON file"""

        #convert object to JSON-formatted String
        json_data = json.dump(self.__objects)

        #open a file in write mode
        with open(self.__file_path, 'w') as file:
            file.write(json_data)

    def reload(self):
        """Deserialize JSON file to __objects"""

        with open(self.__file_path, 'r') as file:
            json_data = file.read()

        self.__objects = json.loads(json_data)