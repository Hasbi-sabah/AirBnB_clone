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
	6159ed8d-8000-4a79-ae1b-054c70d1181d
	(hbnb) create Place
	b5bc6edd-f014-405a-b5b9-0ada31ae7a60

### Listing Objects:

You can list objects of a specific class using the all command:

	(hbnb) all User
	["[User] (6159ed8d-8000-4a79-ae1b-054c70d1181d) {'id': '6159ed8d-8000-4a79-ae1b-054c70d1181d', 'created_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55305), 'updated_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55325)}", 
	"[User] (366d52c8-7c93-44f0-9a3b-84f767fa78ad) {'id': '366d52c8-7c93-44f0-9a3b-84f767fa78ad', 'created_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747106), 'updated_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747126)}", 
	"[User] (0dde3a8e-a607-41db-b1ac-ea04c91f059f) {'id': '0dde3a8e-a607-41db-b1ac-ea04c91f059f', 'created_at': datetime.datetime(2023, 8, 8, 10, 21, 19, 766357), 'updated_at': datetime.datetime(2023, 8, 8, 10, 21, 19, 766431)}"]

Or by using: ```<class name>.all()```

	(hbnb) User.all()
	["[User] (6159ed8d-8000-4a79-ae1b-054c70d1181d) {'id': '6159ed8d-8000-4a79-ae1b-054c70d1181d', 'created_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55305), 'updated_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55325)}", 
	"[User] (366d52c8-7c93-44f0-9a3b-84f767fa78ad) {'id': '366d52c8-7c93-44f0-9a3b-84f767fa78ad', 'created_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747106), 'updated_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747126)}", 
	"[User] (0dde3a8e-a607-41db-b1ac-ea04c91f059f) {'id': '0dde3a8e-a607-41db-b1ac-ea04c91f059f', 'created_at': datetime.datetime(2023, 8, 8, 10, 21, 19, 766357), 'updated_at': datetime.datetime(2023, 8, 8, 10, 21, 19, 766431)}"]

### Updating an Object:

You can update an object's attributes one at a time using the update command followed by the class name, object ID, attribute name and attribute value:

	(hbnb) update User 1d1cf00e-7865-4723-ab87-3baa70879489 email "aibnb@mail.com"

Or by using ```<class name>.update(<id>, <attribute name>, <attribute value>)``` or ```<class name>.update(<id>, <dictionary representation>)``` to update multiple attributes at a time:

	(hbnb) User.update("6159ed8d-8000-4a79-ae1b-054c70d1181d", "first_name", "Betty", "age", 24, "budget", "400$")
	(hbnb) User.update("366d52c8-7c93-44f0-9a3b-84f767fa78ad", {"first_name": "Betty", "age": 24, "budget": "400$"})

### Displaying Object Details:

You can display all attributes of an object based on its class anme and ID using the show command:

	(hbnb) show User 6159ed8d-8000-4a79-ae1b-054c70d1181d
	[User] (6159ed8d-8000-4a79-ae1b-054c70d1181d) {'id': '6159ed8d-8000-4a79-ae1b-054c70d1181d', 
		'created_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55305), 
		'updated_at': datetime.datetime(2023, 8, 8, 10, 20, 49, 55325), 
		'first_name': 'Betty', 'age': 24, 'budget': '400$'}

Or by using ```<class name>.show(<id>)```:

	(hbnb) User.show(366d52c8-7c93-44f0-9a3b-84f767fa78ad)
	[User] (366d52c8-7c93-44f0-9a3b-84f767fa78ad) {'id': '366d52c8-7c93-44f0-9a3b-84f767fa78ad', 
		'created_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747106), 
		'updated_at': datetime.datetime(2023, 8, 8, 10, 21, 18, 747126)}

### Deleting an Object:

You can delete an object using the destroy command followed by the class name and object ID:

   	(hbnb) destroy User 6159ed8d-8000-4a79-ae1b-054c70d1181d

Or by using ```<class name>.destroy(<id>)```:

	(hbnb) User.destroy(6159ed8d-8000-4a79-ae1b-054c70d1181d)

### Counting instances of a Class:

You can retrieve the  number of instances of a class using the ```<class name>.count()``` command:

	(hbnb) User.count()
	2
