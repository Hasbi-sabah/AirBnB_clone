#!/usr/bin/env python3
"""
Console 0.0.1
"""
import cmd
import models
import re


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
        """ Create a instance"""
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

    def do_show(self, args):
        """ Display the requested data"""
        key = self.verify_input(args)
        if key:
            all_objs = models.storage.all()
            try:
                print(all_objs[key])
            except KeyError:
                self.no_instance()

    def do_destroy(self, args):
        """ Delete an instance"""
        key = self.verify_input(args)
        if key:
            all_objs = models.storage.all()
            try:
                del all_objs[key]
                models.storage.save()
            except KeyError:
                self.no_instance()

    def do_all(self, args=None):
        """ Display all objects"""
        print_model = []
        all_objs = models.storage.all()
        if args:
            cls = self.check_class(args)
            if not cls:
                return
            for key in all_objs.keys():
                if args == key.split(".")[0]:
                    print_model.append(str(all_objs[key]))
        else:
            for key in all_objs.keys():
                print_model.append(str(all_objs[key]))
        print(print_model)

    def check_atr(self, args):
        ins = self.verify_input(args)
        if ins:
            atr = args.split()
            if len(atr) < 3:
                print("** attribute name missing **")
            elif len(atr) < 4:
                print("** value missing **")
            else:
                return True
        return None

    def check_val_typ(self, arg):
        if re.match(r"^\d+$", arg):
            return int(args)
        elif re.match(r"^\d+\.\d+$", arg):
            return float(arg)
        else:
            return arg

    def do_update(self, args):
        """ Update specific object"""
        if self.check_atr(args):
            all_objs = models.storage.all()
            atr = args.split()
            obj = "{}.{}".format(atr[0], atr[1])
            value = self.check_val_typ(atr[3])
            setattr(all_objs[obj], atr[2], value)
            models.storage.save()


    def check_class(self, arg):
        cls = self.get_className(arg)
        if not cls:
            self.missing_class()
            return None
        return True

    def verify_input(self, arg):
        if arg:
            args = arg.split()
            if not self.check_class(args[0]):
                return None
        else:
            self.missing_name()
            return None
        if len(args) >= 2:
            cls_id = args[1]
            key = "{}.{}".format(args[0], cls_id)
            return key
        else:
            self.missing_id()
            return None

if __name__=='__main__':
    HBNBCommand().cmdloop()
