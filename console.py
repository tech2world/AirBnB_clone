#!/usr/bin/python3
"""
This module defines the HBNBCommand class.
"""
import cmd

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project"""
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Amenity', 'City', 'Place', 'Review', 'State']

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if not args:
            print("** class name missing **")
            return
        elif args not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args)()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        elif args.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args.split()) < 2:
            print("** instance id missing **")
            return
        key = args.split()[0] + "." + args.split()[1]
        obj = storage.all()
        if key in obj:
            print(obj[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        elif args.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args.split()) < 2:
            print("** instance id missing **")
            return
        key = args.split()[0] + "." + args.split()[1]
        obj = storage.all()
        if key in obj:
            obj.pop(key)
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name"""
        obj = storage.all()
        if not args:
            print([str(obj[k]) for k in obj])
        elif args in self.classes:
            print([str(obj[k]) for k in obj if k.startswith(args + ".")])
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return
        elif args.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args.split()) < 2:
            print("** instance id missing **")
            return

        # Parse arguments
        class_name, instance_id = args.split()[0], args.split()[1]
        attribute_dict = {}
        for pair in args.split()[2:]:
            pair_list = pair.split("=")
            key, value = pair_list[0], pair_list[1]
            if value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            else:
                try:
                    value = float(value)
                    if value.is_integer():
                        value = int(value)
                except ValueError:
                    pass
            attribute_dict[key] = value

        # Retrieve object to update
        key = class_name + "." + instance_id
        obj = storage.all()
        if key not in obj:
            print("** no instance found **")
            return
        obj = obj[key]

        # Update object attributes
        for key, value in attribute_dict.items():
            if key == "created_at" or key == "updated_at":
                continue
            setattr(obj, key, value)

        # Save updated object
        obj.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()