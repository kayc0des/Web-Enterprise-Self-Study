import cmd 
import sys
from models.base_model import BaseModel
#from models.base_model import BaseModel

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

        


if __name__ == '__main__':
    HBNBCommand().cmdloop()