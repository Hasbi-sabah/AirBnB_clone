#!/usr/bin/env python3
"""
Console 0.0.1
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ exits the program"""
        print("")
        return True

    def help_EOF(self):
        """ Shows the commands available"""
        print("exit the program")

    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True

    def format_help(self, command):
        display = super.format_help(command)
        return display + '\n'

    def emptyline(self):
        pass

    def missing_class(self):
        print("** class doesn't exist **")

    def missing_name(self):
        print("** class name missing **")

    def missing_id(self):
        print("** instance id missing **")

    def no_instance(self):
        print("** no instance found **")

    def get_className(self, cls_name):
            return getattr(models.base_model, cls_name, None)

    def do_create(self, cls_name):
        if not cls_name:
            self.missing_name()
        else:
            cls = self.get_className(cls_name)
            if cls:
                my_model = cls()
                my_model.save()
                print(my_model.id)
            else:
                self.missing_class()

    def do_show(self, arg):
        if arg:
            args = arg.split()
            cls_name = args[0]
            cls = self.get_className(cls_name)
            if not cls:
                self.missing_class()
                return
        else:
            self.missing_name()
            return
        if len(args) == 2 and len(args) <= 2:
            all_objs = models.storage.all()
            cls_id = args[1]
            key = "{}.{}".format(cls_name, cls_id)
            try:
                print(all_objs[key])
            except KeyError:
                self.no_instance()
        else:
            self.missing_id()

if __name__=='__main__':
    HBNBCommand().cmdloop()
