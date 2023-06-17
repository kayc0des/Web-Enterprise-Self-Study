import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage


class BaseModel:
    """
    BaseModel class to define all commonn attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates a new object
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        storage.new(self)


    def __str__(self):
        """
        Returns a human-readable string that represents th state
        or characteristics of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        The save method updates the value of the updated_at
        attribute anytime it's called!
        """
        self.updated_at = datetime.now()
        storage.save()

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
new_model = BaseModel(name="My First Model", age=15, score=105, location="Rwanda")
new_model.save()

another_model = BaseModel(name="Kingsley", age=22, score=105, location="Cameroon")
another_model.save()