#!/usr/bin/env python3
"""
Console 0.0.1
"""
import cmd


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

if __name__=='__main__':
    HBNBCommand().cmdloop()
