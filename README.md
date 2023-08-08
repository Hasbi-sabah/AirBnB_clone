# AirBnB clone - The console

## Project Description:

This project is an Airbnb clone's command interpreter, developed in Python. The console provides a command-line interface that allows users to interact with the Airbnb clone's underlying data models and perform various actions.

### Getting Started:

To start the Airbnb clone's command interpreter, follow these steps:

1. Clone the project repository:
   ```git clone https://github.com/Hasbi-sabah/AirBnB_clone```

2. Navigate to the project directory:
   ```cd AirBnB_clone```

3. Launch the console:
   ```./console```

## Usage:

The command interpreter supports various commands that allow you to manipulate data models, perform operations, and interact with the Airbnb clone's features. Here are some example commands and their usage:

### Creating a New Object:

You can create one of 7 new model objects ```[BaseModel, User, Place, State, City, Amenity, Review]``` using the create command, The command interpreter will automatically generate a unique ID for the new instance and display it:

	(hbnb) create User
	1d1cf00e-7865-4723-ab87-3baa70879489
	(hbnb) create Place
	352dbd0e-69f5-4368-893e-6c6924b08f28

### Listing Objects:

You can list objects of a specific class using the all command:

	(hbnb) all User

Or by using: ```<class name>.all()```
	(hbnb) User.all()

### Displaying Object Details:

You can display all attributes of an object based on its class anme and ID using the show command:

	(hbnb) show User 1d1cf00e-7865-4723-ab87-3baa70879489

Or by using ```<class name>.show(<id>)```:

	(hbnb) User.show(1d1cf00e-7865-4723-ab87-3baa70879489)

### Updating an Object:

You can update an object's attributes one at a time using the update command followed by the class name, object ID, attribute name and attribute value:

	(hbnb) update User 1d1cf00e-7865-4723-ab87-3baa70879489 email "aibnb@mail.com"

Or by using <class name>.update(<id>, <attribute name>, <attribute value>) or <class name>.update(<id>, <dictionary representation>) to update multiple attributes at a time:

	(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "Betty", "age", 24, "budget", "400$")
	(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {"first_name": "Betty", "age": 24, "budget": "400$"})

### Deleting an Object:

You can delete an object using the destroy command followed by the class name and object ID:

   	(hbnb) destroy User 1d1cf00e-7865-4723-ab87-3baa70879489

Or by using ```<class name>.destroy(<id>)```:

	(hbnb) User.destroy(1d1cf00e-7865-4723-ab87-3baa70879489)

### Counting instances of a Class:

You can retrieve the  number of instances of a class using the ```<class name>.count()``` command:

	(hbnb) User.count()
	3
