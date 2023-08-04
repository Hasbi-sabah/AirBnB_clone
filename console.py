#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import models
import uuid
import shlex

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    cls = ['BaseModel']

    def do_quit(self, line):
        '''handles quit'''
        return True

    def help_quit(self):
        print('Handles the quit command and exits')
    
    def do_EOF(self, line):
        '''handles EOF'''
        return True

    def help_EOF(self):
        print('Handles the EOF and exits')

    def emptyline(self):
        '''handles empty lines'''
        pass

    def do_create(self, line):
        if not line:
            print('** class name missing **')
        elif line not in self.cls:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) == 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
            if line in instances:
                print(instances[line])
            else:
                print('** no instance found **')
        else:
            self.error_printer(line_arr)

    def do_destroy(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) == 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
            if line in instances:
                del instances[line]
                models.storage.save()
            else:
                print('** no instance found **')
        else:
            self.error_printer(line_arr)

    def do_all(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) == 1 and line_arr[0] not in self.cls:
            print("** class doesn't exist **")
            return
        lst = []
        for inst in instances:
            if len(line_arr) == 0 or (len(line_arr) >= 1 and line_arr[0] == instances[inst].to_dict()['__class__']):
                lst.append(str(instances[inst]))
        print(lst)

    def error_printer(self, args):
        if not args:
            print('** class name missing **')
        elif args[0] not in self.cls:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
if __name__ == '__main__':
    HBNBCommand().cmdloop()
