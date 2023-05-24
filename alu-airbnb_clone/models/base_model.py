import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class to define all commonn attributes/methods
    for other classes
    """

    def __init__(self):
        """
        Instantiates a new object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a human-readable string that represents th state
        or characteristics of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        The save method updates the value of the updated_at
        attribute anytime it's called
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a Dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy() #
        """
        __dict__ attribute is a dict that holds the namespace of a class
        or an instance. >>> print(BaseModel.__dict__)
        """
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict


"""
Manually try out the BaseModel
"""
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
#print(my_model)
my_model.save()
#print(my_model)

"""
Create a JSON Variable and assign it to my_model.to_dict()
"""
my_model_json = my_model.to_dict()
#print(my_model_json)

#print("JSON of my model:")
#for key in my_model_json.keys():
    #print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))