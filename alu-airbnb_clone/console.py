import cmd
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# import uuid
# from datetime import datetime
# import os
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models.__init__ import storage

# class BaseModel():
#     def __init__(self):
#         print("hello world")

class HBNBCommand(cmd.Cmd):
    """
    CLI CLass
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exits the command lop
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program
        """
        return True

    def emptyline(self):
        """ When no input is passed"""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel
        """
        if arg:
            class_name = arg.strip() #get the class name from the argument
            try:
                class_name = BaseModel()
                class_name.save()
                print(type(class_name))
                print(class_name.id)
            except KeyError:
                print(f"Error: {class_name} is nt a valid class name")
        else:
            print("Class name missing")
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()