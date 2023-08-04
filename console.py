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
        line_arr = shlex.split(line)
        if self.is_valid('', line_arr, {}, 1):
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) >= 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
        if self.is_valid(line, line_arr, instances, 2):
            print(instances[line])

    def do_destroy(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) >= 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
        if self.is_valid(line, line_arr, instances, 2):
            del instances[line]
            models.storage.save()

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

    def do_update(self, line):
        instances = models.storage.all()
        line_arr = shlex.split(line)
        if len(line_arr) >= 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
        if self.is_valid(line, line_arr, instances, 3):
            setattr(instances[line], line_arr[2], line_arr[3])
            models.storage.save()



    def is_valid(self, line, line_arr, instances, flag):
        if flag >= 1 and len(line_arr) == 0:
            print('** class name missing **')
        elif flag >= 1 and line_arr[0] not in self.cls:
            print("** class doesn't exist **")
        elif flag >= 2 and len(line_arr) == 1:
            print('** instance id missing **')
        elif flag >= 2 and line not in instances:
            print('** no instance found **')
        elif flag >= 3 and len(line_arr) == 2:
            print('** attribute name missing **')
        elif flag >= 3 and len(line_arr) == 3:
            print('** value missing **')
        else:
            return True
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
