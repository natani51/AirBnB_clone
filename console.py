#!/usr/bin/python3
"""This is the console for AirBnB"""

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


def pattern(arg):
    """
    Retrieve the cmd method and the respective arguments according
    to a pattern so that they can be invoked under this scheme:
    <class>. <cmd> ([args, ...])
    """
    pattern = '\.([^.]+)\(|([^(),]+)[,\s()]*[,\s()]*'
    argum = re.findall(pattern, arg)
    cmd = argum[0][0]
    argum = argum[1:]
    line = ' '.join(map(lambda x: x[1].strip('"'), argum))
    return cmd, line


def loop_dic(line, obj_upt):
    """
    Loop for update with format:
    <class name>.update(<id>, <dictionary representation>)
    """
    j = 4
    while j <= len(line):
        try:
            atrribute = line[j]
        except IndexError:
            print("** attribute name missing **")
        else:
            try:
                value = line[j+1]
            except IndexError:
                print("** value missing **")
            else:
                setattr(obj_upt, atrribute, value)
                obj_upt.save()
                if j+1 == len(line) - 1:
                    break
        j += 1


class HBNBCommand(cmd.Cmd):
    """AirBnB console main class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Handle End Of File"""
        return True

    def do_quit(self, arg):
        """Exit program"""
        return True

    def emptyline(self):
        """If line is empty don't do anything"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.classes[arg]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
         (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234.
         """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        objects = storage.all()
                        models.storage.delete(objects[key])
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if len(arg) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items()
                   if arg in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email
        """
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            for iter in range(len(line)):
                line[iter] = line[iter].strip("\"'\"{\"}:\"'")
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj_upt = models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            atrribute = line[2]
                        except IndexError:
                            print("** attribute name missing **")
                        else:
                            try:
                                value = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                setattr(obj_upt, atrribute, value)
                                obj_upt.save()
                                if len(line) >= 5:
                                    loop_dic(line, obj_upt)
            else:
                print("** class doesn't exist **")

    def do_BaseModel(self, arg):
        """
        Lets you invoke each of the console methods
        for the BaseModel class with the following syntax:
        BaseModel.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'BaseModel', line]))

    def do_Amenity(self, arg):
        """
        Lets you invoke each of the console methods
        for the Amenity class with the following syntax:
        Amenity.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Amenity', line]))

    def do_City(self, arg):
        """
        Lets you invoke each of the console methods
        for the City class with the following syntax:
        City.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'City', line]))

    def do_Place(self, arg):
        """
        Lets you invoke each of the console methods
        for the Place class with the following syntax:
        Place.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Place', line]))

    def do_Review(self, arg):
        """
        Lets you invoke each of the console methods
        for the Review class with the following syntax:
        Review.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'Review', line]))

    def do_State(self, arg):
        """
        Lets you invoke each of the console methods
        for the State class with the following syntax:
        State.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'State', line]))

    def do_User(self, arg):
        """
        Lets you invoke each of the console methods
        for the User class with the following syntax:
        User.<cmd>([args, ...])
        cmd can be: all, create, update, show destroy
        """
        cmd, line = pattern(arg)
        self.onecmd(' '.join([cmd, 'User', line]))

    def do_count(self, arg):
        """
        Retrieve the number of instances of a class: <class name>.count()
        """
        if len(arg) == 0:
            print(len([str(value) for value in models.storage.all().values()]))
        elif arg in models.classes:
            print(len([str(value) for key, value in
                       models.storage.all().items()
                      if arg in key]))
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
