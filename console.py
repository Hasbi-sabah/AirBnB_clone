#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import uuid
import shlex
import re

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    cls = ['BaseModel', 'User', 'Place', 'City', 'State', 'Amenity', 'Review']

    def do_quit(self, line):
        '''handles quit'''
        return True

    def help_quit(self):
        print('Handles the quit command and exits')
    
    def do_EOF(self, line):
        '''handles EOF'''
        print()
        return True

    def help_EOF(self):
        print('Handles the EOF and exits')

    def emptyline(self):
        '''handles empty lines'''
        pass

    def do_create(self, line):
        line_arr = shlex.split(line)
        if self.is_valid('', line_arr, {}, 1):
            new = eval(line_arr[0])()
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

    def count(self, line):
        instances = models.storage.all()
        count = 0
        for inst in instances:
            if line == instances[inst].to_dict()['__class__']:
                count += 1
        print(count)

    def do_update(self, line, flag=0):
        instances = models.storage.all()
        if not flag:
            line_arr = shlex.split(line)
        else:
            line_arr = line
        if len(line_arr) >= 2:
            line = '{}.{}'.format(line_arr[0], line_arr[1])
        if self.is_valid(line, line_arr, instances, 3):
            setattr(instances[line], line_arr[2], line_arr[3])
            models.storage.save()

    def default(self, line):
        instances = models.storage.all()
        line_arr = re.match('^(\w+)\.(\w+)\((.*)\)', line)
        if line_arr:
            line_arr = list(line_arr.groups()) 
            line_arr[2] = line_arr[2].replace(',', '')
            line_args = shlex.split(line_arr[2])
        cmd = {'all': self.do_all, 'count': self.count, 'show': self.do_show, 'destroy': self.do_destroy}
        if line_arr and len(line_arr) >= 2 and line_arr[0] in self.cls and line_arr[1] in cmd:
            if len(line_arr) >= 3 and (line_arr[1] == 'show' or line_arr[1] == 'destroy'):
                arg = line_arr[0] + ' ' + line_arr[2]
            else:
                arg = line_arr[0]
            cmd[line_arr[1]](arg)
        elif line_arr and len(line_arr) >= 2 and line_arr[1] == 'update':
            if len(line_args) == 1:
                args = [line_arr[0], line_args[0]]
                self.do_update(args, 1)
            for i in range (1, len(line_args), 2):
                args = [line_arr[0], line_args[0], line_args[i]]
                if i + 1 < len(line_args):
                    args.append(line_args[i + 1])
                self.do_update(args, 1)
        else:
            super().default(line)

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
