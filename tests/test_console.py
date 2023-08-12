import uuid
import os
import unittest
from io import StringIO
from unittest.mock import patch, Mock
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import console


class TestConsole(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_doc(self):
        self.assertIsNotNone(console.__doc__)

    def test_class_doc(self):
        self.assertIsNotNone(HBNBCommand.__doc__)

    def test_method_docs(self):
        """Test all methods in ``console`` for docs"""
        methods = [
            HBNBCommand.do_EOF,
            HBNBCommand.help_EOF,
            HBNBCommand.do_quit,
            HBNBCommand.help_quit,
            HBNBCommand.emptyline,
            HBNBCommand.is_valid,
            HBNBCommand.value_type,
            HBNBCommand.do_create,
            HBNBCommand.help_create,
            HBNBCommand.do_show,
            HBNBCommand.help_show,
            HBNBCommand.do_destroy,
            HBNBCommand.help_destroy,
            HBNBCommand.do_all,
            HBNBCommand.help_all,
            HBNBCommand.count,
            HBNBCommand.do_update,
            HBNBCommand.default,
        ]
        for meth in methods:
            self.assertIsNotNone(meth.__doc__)

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_help_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_destroy(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_all(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_create_with_valid_class_name_BaseModel(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_User(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Place(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_State(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_City(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Amenity(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Review(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_with_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_id(self):
        test_inst = User()
        test_inst.save()
        cmd = f"show User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    def test_show_without_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_with_invalid_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_instance_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("show User 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id(self):
        test_inst = User()
        test_inst.save()
        cmd = f"destroy User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_with_nonexistent_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_with_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_with_nonexistent_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all_with_no_class(self):
        test_inst1 = User()
        test_inst1.save()
        test_inst2 = User()
        test_inst2.save()
        test_inst3 = User()
        test_inst2.save()
        test_inst4 = Place()
        test_inst4.save()
        test_inst5 = Place()
        test_inst5.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst1.id})", output)
            self.assertIn(f"[User] ({test_inst2.id})", output)
            self.assertIn(f"[User] ({test_inst3.id})", output)
            self.assertIn(f"[Place] ({test_inst4.id})", output)
            self.assertIn(f"[Place] ({test_inst5.id})", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

    def test_all_with_valid_class(self):
        test_inst1 = User()
        test_inst1.save()
        test_inst2 = User()
        test_inst2.save()
        test_inst3 = City()
        test_inst2.save()
        test_inst4 = Place()
        test_inst4.save()
        test_inst5 = Place()
        test_inst5.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst1.id})", output)
            self.assertIn(f"[User] ({test_inst2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

    def test_all_with_empty_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_all_with_noexistent_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_with_valid_input_str(self):
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} name 'malibu smith'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "malibu smith")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_valid_input_int(self):
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} age 24"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "age"))
        self.assertEqual(test_inst.age, 24)
        self.assertEqual(type(test_inst.age), int)

    def test_update_with_valid_input_float(self):
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} height 1.80"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "height"))
        self.assertEqual(test_inst.height, 1.80)
        self.assertEqual(type(test_inst.height), float)

    def test_update_with_class(self):
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} __class__ 'not allowed'"
        self.assertNotEqual(test_inst.__class__, "not allowed")

    def test_update_with_user_attr(self):
        test_inst = User()
        test_inst.save()
        cmd = f"update User {test_inst.id} email 'airbnb@mail.com'"
        HBNBCommand().onecmd(cmd)
        cmd = f"update User {test_inst.id} password root"
        HBNBCommand().onecmd(cmd)
        cmd = f"update User {test_inst.id} first_name Betty"
        HBNBCommand().onecmd(cmd)
        cmd = f"update User {test_inst.id} last_name Holberton"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "email"))
        self.assertEqual(test_inst.email, "airbnb@mail.com")
        self.assertEqual(type(test_inst.email), str)
        self.assertTrue(hasattr(test_inst, "password"))
        self.assertEqual(test_inst.password, "root")
        self.assertEqual(type(test_inst.password), str)
        self.assertTrue(hasattr(test_inst, "first_name"))
        self.assertEqual(test_inst.first_name, "Betty")
        self.assertEqual(type(test_inst.first_name), str)
        self.assertTrue(hasattr(test_inst, "last_name"))
        self.assertEqual(test_inst.last_name, "Holberton")
        self.assertEqual(type(test_inst.last_name), str)

    def test_update_with_state_attr(self):
        test_inst = State()
        test_inst.save()
        cmd = f"update State {test_inst.id} name Betty"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_city_attr(self):
        test_inst = City()
        test_inst.save()
        cmd = f"update City {test_inst.id} state_id 'the id'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "state_id"))
        self.assertEqual(test_inst.state_id, "the id")
        self.assertEqual(type(test_inst.state_id), str)
        cmd = f"update City {test_inst.id} state_id 404"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "state_id"))
        self.assertEqual(test_inst.state_id, "404")
        self.assertEqual(type(test_inst.state_id), str)
        cmd = f"update City {test_inst.id} name 'roma'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "roma")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_amenity_attr(self):
        test_inst = Amenity()
        test_inst.save()
        cmd = f"update Amenity {test_inst.id} name 'sea side'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "sea side")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_place_attr(self):
        test_inst = Place()
        test_inst.save()
        cmd = f"update Place {test_inst.id} city_id 'a random id'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "city_id"))
        self.assertEqual(test_inst.city_id, "a random id")
        self.assertEqual(type(test_inst.city_id), str)
        cmd = f"update Place {test_inst.id} user_id 'a random user id'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        cmd = f"update Place {test_inst.id} name 'Betty'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)
        cmd = f"update Place {test_inst.id} description 'this is boring'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "description"))
        self.assertEqual(test_inst.description, "this is boring")
        self.assertEqual(type(test_inst.description), str)
        cmd = f"update Place {test_inst.id} number_rooms 5"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "number_rooms"))
        self.assertEqual(test_inst.number_rooms, 5)
        self.assertEqual(type(test_inst.number_rooms), int)
        cmd = f"update Place {test_inst.id} number_bathrooms 2"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "number_bathrooms"))
        self.assertEqual(test_inst.number_bathrooms, 2)
        self.assertEqual(type(test_inst.number_bathrooms), int)
        cmd = f"update Place {test_inst.id} max_guest 6"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "max_guest"))
        self.assertEqual(test_inst.max_guest, 6)
        self.assertEqual(type(test_inst.max_guest), int)
        cmd = f"update Place {test_inst.id} price_by_night 500"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "price_by_night"))
        self.assertEqual(test_inst.price_by_night, 500)
        self.assertEqual(type(test_inst.price_by_night), int)
        cmd = f"update Place {test_inst.id} latitude 200.5"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.latitude, 200.5)
        self.assertEqual(type(test_inst.latitude), float)
        cmd = f"update Place {test_inst.id} latitude 200"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.latitude, 200)
        self.assertEqual(type(test_inst.latitude), float)
        cmd = f"update Place {test_inst.id} longitude 200.5"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "longitude"))
        self.assertEqual(test_inst.longitude, 200.5)
        self.assertEqual(type(test_inst.longitude), float)
        cmd = f"update Place {test_inst.id} longitude 200"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "longitude"))
        self.assertEqual(test_inst.longitude, 200)
        self.assertEqual(type(test_inst.longitude), float)

    def test_update_with_Review_attr(self):
        test_inst = Review()
        test_inst.save()
        cmd = f"update Review {test_inst.id} place_id 'a random id'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "place_id"))
        self.assertEqual(test_inst.place_id, "a random id")
        self.assertEqual(type(test_inst.place_id), str)
        cmd = f"update Review {test_inst.id} user_id 'a random user id'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        cmd = f"update Review {test_inst.id} text 'this is so boring'"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "text"))
        self.assertEqual(test_inst.text, "this is so boring")
        self.assertEqual(type(test_inst.text), str)

    def test_update_with_missing_class_name(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_with_nonexistent_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_with_missing_id(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_with_nonexistent_instance(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 121212")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_with_missing_attribute_name(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_with_missing_attribute_value(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {test_inst.id} name")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_with_many_input(self):
        test_inst = User()
        test_inst.save()
        cmd1 = f"update User {test_inst.id} name 'malibu smith' "
        cmd2 = f"age 30 height 1.7"
        HBNBCommand().onecmd(cmd1 + cmd2)
        self.assertFalse(hasattr(test_inst, "age"))
        self.assertFalse(hasattr(test_inst, "height"))

    def test_all_with_valid_class2(self):
        test_inst1 = User()
        test_inst1.save()
        test_inst2 = User()
        test_inst2.save()
        test_inst3 = City()
        test_inst2.save()
        test_inst4 = Place()
        test_inst4.save()
        test_inst5 = Place()
        test_inst5.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst1.id})", output)
            self.assertIn(f"[User] ({test_inst2.id})", output)
            self.assertNotIn(f"[Place]", output)
            self.assertNotIn(f"[Basemodel]", output)
            self.assertNotIn(f"[City]", output)
            self.assertTrue(output.startswith('["'))
            self.assertTrue(output.endswith('"]'))

    def test_all_with_empty_class2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_all_with_noexistent_class2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count_with_nonexistent_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_count_with_valid_class(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

    def test_count_with_valid_class1(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_count_with_valid_class2(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "0")

    def test_count_with_valid_class3(self):
        test_inst = User()
        test_inst.save()
        test_inst = Place()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

    def test_show_with_valid_class_and_id2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.show({test_inst.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    def test_show_with_invalid_class_name2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_without_instance_id2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_with_invalid_instance_id2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_valid_class_and_id2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.destroy({test_inst.id})"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            HBNBCommand().onecmd(f"show User {test_inst.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy_with_nonexistent_class2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_with_missing_id2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_with_nonexistent_instance2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_with_valid_input_str2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.update({test_inst.id}, name, 'malibu smith')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "malibu smith")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_valid_input_int2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.update({test_inst.id}, age, 24)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "age"))
        self.assertEqual(test_inst.age, 24)
        self.assertEqual(type(test_inst.age), int)

    def test_update_with_valid_input_float2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.update({test_inst.id}, height, 1.80)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "height"))
        self.assertEqual(test_inst.height, 1.80)
        self.assertEqual(type(test_inst.height), float)

    def test_update_with_class2(self):
        test_inst = User()
        test_inst.save()
        cmd = f"User.update({test_inst.id}, __class__, 'not allowed')"
        self.assertNotEqual(test_inst.__class__, "not allowed")

    def test_update_with_user_attr2(self):
        test_inst = User()
        test_inst.save()
        cmd1 = f"User.update({test_inst.id}, email, 'airbnb@mail.com', "
        cmd2 = f"password, root, "
        cmd3 = f"first_name, Betty, "
        cmd4 = f"last_name, Holberton)"
        HBNBCommand().onecmd(cmd1 + cmd2 + cmd3 + cmd4)
        self.assertTrue(hasattr(test_inst, "email"))
        self.assertEqual(test_inst.email, "airbnb@mail.com")
        self.assertEqual(type(test_inst.email), str)
        self.assertTrue(hasattr(test_inst, "password"))
        self.assertEqual(test_inst.password, "root")
        self.assertEqual(type(test_inst.password), str)
        self.assertTrue(hasattr(test_inst, "first_name"))
        self.assertEqual(test_inst.first_name, "Betty")
        self.assertEqual(type(test_inst.first_name), str)
        self.assertTrue(hasattr(test_inst, "last_name"))
        self.assertEqual(test_inst.last_name, "Holberton")
        self.assertEqual(type(test_inst.last_name), str)

    def test_update_with_state_attr2(self):
        test_inst = State()
        test_inst.save()
        cmd = f"State.update({test_inst.id}, name, Betty)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_city_attr2(self):
        test_inst = City()
        test_inst.save()
        cmd = f"City.update({test_inst.id}, state_id, 'the id')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "state_id"))
        self.assertEqual(test_inst.state_id, "the id")
        self.assertEqual(type(test_inst.state_id), str)
        cmd = f"City.update({test_inst.id}, name, 'roma')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "roma")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_amenity_attr2(self):
        test_inst = Amenity()
        test_inst.save()
        cmd = f"Amenity.update({test_inst.id}, name, 'sea side')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "sea side")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_place_attr2(self):
        test_inst = Place()
        test_inst.save()
        cmd = f"Place.update({test_inst.id} city_id, 'a random id', user_id, 'a random user id')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "city_id"))
        self.assertEqual(test_inst.city_id, "a random id")
        self.assertEqual(type(test_inst.city_id), str)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        cmd = f"Place.update({test_inst.id}, name, 'Betty', description, 'this is boring')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)
        self.assertTrue(hasattr(test_inst, "description"))
        self.assertEqual(test_inst.description, "this is boring")
        self.assertEqual(type(test_inst.description), str)
        cmd = f"Place.update({test_inst.id}, number_rooms, 5, number_bathrooms, 2)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "number_rooms"))
        self.assertEqual(test_inst.number_rooms, 5)
        self.assertEqual(type(test_inst.number_rooms), int)
        self.assertTrue(hasattr(test_inst, "number_bathrooms"))
        self.assertEqual(test_inst.number_bathrooms, 2)
        self.assertEqual(type(test_inst.number_bathrooms), int)
        cmd = f"Place.update({test_inst.id}, max_guest, 6, price_by_night, 500, latitude, 200.5)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "max_guest"))
        self.assertEqual(test_inst.max_guest, 6)
        self.assertEqual(type(test_inst.max_guest), int)
        self.assertTrue(hasattr(test_inst, "price_by_night"))
        self.assertEqual(test_inst.price_by_night, 500)
        self.assertEqual(type(test_inst.price_by_night), int)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.latitude, 200.5)
        self.assertEqual(type(test_inst.latitude), float)
        cmd = f"Place.update({test_inst.id}, latitude, 200, longitude, 200)"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.longitude, 200)
        self.assertEqual(type(test_inst.longitude), float)
        self.assertTrue(hasattr(test_inst, "longitude"))
        self.assertEqual(test_inst.longitude, 200)
        self.assertEqual(type(test_inst.longitude), float)

    def test_update_with_Review_attr2(self):
        test_inst = Review()
        test_inst.save()
        cmd = f"Review.update({test_inst.id}, place_id, 'a random id')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "place_id"))
        self.assertEqual(test_inst.place_id, "a random id")
        self.assertEqual(type(test_inst.place_id), str)
        cmd = f"Review.update({test_inst.id}, user_id 'a random user id')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        cmd = f"Review.update({test_inst.id}, text, 'this is so boring')"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "text"))
        self.assertEqual(test_inst.text, "this is so boring")
        self.assertEqual(type(test_inst.text), str)

    def test_update_with_nonexistent_instance2(self):
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(121212)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_update_with_missing_attribute_name2(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({test_inst.id})")
            output = f.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_with_missing_attribute_value2(self):
        test_inst = User()
        test_inst.save()
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({test_inst.id}, name)")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_with_valid_input_str3(self):
        test_inst = User()
        test_inst.save()
        attr_dict = {"name": "malibu smith"}
        cmd = f"User.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "malibu smith")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_valid_input_int3(self):
        test_inst = User()
        test_inst.save()
        attr_dict = {"age": 24}
        cmd = f"User.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "age"))
        self.assertEqual(test_inst.age, 24)
        self.assertEqual(type(test_inst.age), int)

    def test_update_with_valid_input_float3(self):
        test_inst = User()
        test_inst.save()
        attr_dict = {"height": 1.80}
        cmd = f"User.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "height"))
        self.assertEqual(test_inst.height, 1.80)
        self.assertEqual(type(test_inst.height), float)

    def test_update_with_class3(self):
        test_inst = User()
        test_inst.save()
        attr_dict = {"__class__": "not allowed"}
        cmd = f"User.update({test_inst.id}, {attr_dict})"
        self.assertNotEqual(test_inst.__class__, "not allowed")

    def test_update_with_user_attr3(self):
        test_inst = User()
        test_inst.save()
        attr_dict = {
            "email": "airbnb@mail.com",
            "password": "root",
            "first_name": "Betty",
            "last_name": "Holberton",
        }
        cmd = f"User.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "email"))
        self.assertEqual(test_inst.email, "airbnb@mail.com")
        self.assertEqual(type(test_inst.email), str)
        self.assertTrue(hasattr(test_inst, "password"))
        self.assertEqual(test_inst.password, "root")
        self.assertEqual(type(test_inst.password), str)
        self.assertTrue(hasattr(test_inst, "first_name"))
        self.assertEqual(test_inst.first_name, "Betty")
        self.assertEqual(type(test_inst.first_name), str)
        self.assertTrue(hasattr(test_inst, "last_name"))
        self.assertEqual(test_inst.last_name, "Holberton")
        self.assertEqual(type(test_inst.last_name), str)

    def test_update_with_state_attr3(self):
        test_inst = State()
        test_inst.save()
        attr_dict = {"name": "Betty"}
        cmd = f"State.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_city_attr3(self):
        test_inst = City()
        test_inst.save()
        attr_dict = {"state_id": "the id", "name": "roma"}
        cmd = f"City.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "state_id"))
        self.assertEqual(test_inst.state_id, "the id")
        self.assertEqual(type(test_inst.state_id), str)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "roma")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_amenity_attr3(self):
        test_inst = Amenity()
        test_inst.save()
        attr_dict = {"name": "sea side"}
        cmd = f"Amenity.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "sea side")
        self.assertEqual(type(test_inst.name), str)

    def test_update_with_place_attr3(self):
        test_inst = Place()
        test_inst.save()
        attr_dict = {
            "city_id": "a random id",
            "user_id": "a random user id",
            "name": "Betty",
            "description": "this is boring",
            "number_rooms": 5,
            "number_bathrooms": 2,
        }
        cmd = f"Place.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "city_id"))
        self.assertEqual(test_inst.city_id, "a random id")
        self.assertEqual(type(test_inst.city_id), str)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "name"))
        self.assertEqual(test_inst.name, "Betty")
        self.assertEqual(type(test_inst.name), str)
        self.assertTrue(hasattr(test_inst, "description"))
        self.assertEqual(test_inst.description, "this is boring")
        self.assertEqual(type(test_inst.description), str)
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "number_rooms"))
        self.assertEqual(test_inst.number_rooms, 5)
        self.assertEqual(type(test_inst.number_rooms), int)
        self.assertTrue(hasattr(test_inst, "number_bathrooms"))
        self.assertEqual(test_inst.number_bathrooms, 2)
        self.assertEqual(type(test_inst.number_bathrooms), int)
        attr_dict = {"latitude": 200.5, "price_by_night": 500, "max_guest": 6}
        cmd = f"Place.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "max_guest"))
        self.assertEqual(test_inst.max_guest, 6)
        self.assertEqual(type(test_inst.max_guest), int)
        self.assertTrue(hasattr(test_inst, "price_by_night"))
        self.assertEqual(test_inst.price_by_night, 500)
        self.assertEqual(type(test_inst.price_by_night), int)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.latitude, 200.5)
        self.assertEqual(type(test_inst.latitude), float)
        attr_dict = {"latitude": 200, "longitude": 200}
        cmd = f"Place.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "latitude"))
        self.assertEqual(test_inst.longitude, 200)
        self.assertEqual(type(test_inst.longitude), float)
        self.assertTrue(hasattr(test_inst, "longitude"))
        self.assertEqual(test_inst.longitude, 200)
        self.assertEqual(type(test_inst.longitude), float)

    def test_update_with_Review_attr3(self):
        test_inst = Review()
        test_inst.save()
        attr_dict = {"place_id": "a random id", "user_id": "a random user id"}
        cmd = f"Review.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "place_id"))
        self.assertEqual(test_inst.place_id, "a random id")
        self.assertEqual(type(test_inst.place_id), str)
        self.assertTrue(hasattr(test_inst, "user_id"))
        self.assertEqual(test_inst.user_id, "a random user id")
        self.assertEqual(type(test_inst.user_id), str)
        attr_dict = {"text": "this is so boring"}
        cmd = f"Review.update({test_inst.id}, {attr_dict})"
        HBNBCommand().onecmd(cmd)
        self.assertTrue(hasattr(test_inst, "text"))
        self.assertEqual(test_inst.text, "this is so boring")
        self.assertEqual(type(test_inst.text), str)


if __name__ == "__main__":
    unittest.main()
