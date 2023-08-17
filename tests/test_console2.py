import unittest

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class ConsoleTestCase(unittest.TestCase):
    """DOC DOC"""

    def check_json(self, classname, id):
        keyname = classname+"."+id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname]["id"], id)
        self.assertEqual(saved_data[keyname]["__class__"], classname)

    def test_error(self):
        """DOC DOC"""
        cmd_classname = ["create", "update", "show", "destroy"]
        cmd_id = ["update", "show", "destroy"]
        cmd_attr = ["update"]

        """ERROR """
        """ class name missing """
        for cmd in cmd_classname:
            # print(f"class name missing : {cmd}")
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ class doesn't exist """
        class_dont_exist = ["create x", "update x",
                            "show x", "destroy x", "all x"]
        for cmd in class_dont_exist:
            # print(f"class doesn't exist : {cmd}")
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class doesn't exist **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ instance id missing """
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().cls
        for cmd in cmds:
            for clas in all_class:
                # print(f"instance id missing : {cmd} {clas}")
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** instance id missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ no instance found """
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().cls
        wrong_id = "x"
        for cmd in cmds:
            for clas in all_class:
                # print(f"no instance found : {cmd} {clas} {wrong_id}")
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** no instance found **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ name missing """
        new_BaseModel = BaseModel()
        new_User = User()
        new_State = State()
        new_City = City()
        new_Amenity = Amenity()
        new_Place = Place()
        new_Review = Review()
        id_BaseModel = new_BaseModel.id
        id_User = new_User.id
        id_State = new_State.id
        id_City = new_City.id
        id_Amenity = new_Amenity.id
        id_Place = new_Place.id
        id_Review = new_Review.id
        id_dict = {"BaseModel": id_BaseModel, "User": id_User,
                   "State": id_State, "City": id_City, "Amenity": id_Amenity,
                   "Place": id_Place, "Review": id_Review}
        cmds = ["update"]
        all_class = HBNBCommand().cls
        for cmd in cmds:
            for clas in all_class:
                # print(f"no instance found : {cmd} {clas} {wrong_id}")
                # print(f"{cmd} {clas} {id_dict[clas]}")
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** attribute name missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ value missing """
        new_BaseModel = BaseModel()
        new_User = User()
        new_State = State()
        new_City = City()
        new_Amenity = Amenity()
        new_Place = Place()
        new_Review = Review()
        id_BaseModel = new_BaseModel.id
        id_User = new_User.id
        id_State = new_State.id
        id_City = new_City.id
        id_Amenity = new_Amenity.id
        id_Place = new_Place.id
        id_Review = new_Review.id
        id_dict = {"BaseModel": id_BaseModel, "User": id_User,
                   "State": id_State, "City": id_City, "Amenity": id_Amenity,
                   "Place": id_Place, "Review": id_Review}
        cmds = ["update"]
        all_class = HBNBCommand().cls
        for cmd in cmds:
            for clas in all_class:
                # print(f"no instance found : {cmd} {clas} {wrong_id}")
                # print(f"{cmd} {clas} {id_dict[clas]}")
                with patch('sys.stdout', new=StringIO()) as f:
                    expected = "** value missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
                    self.assertCountEqual(expected, f.getvalue().strip())


# python3 -m unittest -v tests/test_console.py
# echo "python3 -m unittest -v tests/test_console.py " | bash
#   all_class = ["BaseModel", "User", "State",
# "City", "Amenity", "Place", "Review"]

if __name__ == '__main__':
    unittest.main()
