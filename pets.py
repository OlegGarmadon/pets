def descride_pet(animal_type, pet_name):
	"""Выводит информацию о животном"""
	print(F"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

descride_pet('hamster', 'harry')

# МНОГОКРАТНЫЙ ВЫЗОВ ФУКЦИИ.

def descride_pet(animal_type, pet_name):
	"""Выводит информацию о животном"""
	print(F"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

descride_pet('hamster', 'harry')
descride_pet('dog', 'vrot')

# ИМЕНОВАННЫЕ АРГУМЕНТЫ.

def descride_pet(animal_type, pet_name):
	"""Выводит информацию о животном"""
	print(F"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

descride_pet(animal_type= 'hamster', pet_name= 'harry')
descride_pet(pet_name= 'harry', animal_type= 'hamster')

# ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ

def descride_pet(pet_name, animal_type= 'dog'):
	"""Выводит информацию о животном"""
	print(F"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")
descride_pet(pet_name= 'wille')
descride_pet('wille')
descride_pet('sargan')

# ЭКВИВАЛЕНТНЫЕ ВЫЗОВЫ ФУНКЦИИ

def descride_pet(pet_name, animal_type= 'dog'):
	print(F"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")
descride_pet('wille')

"""Хомяк по имени Гарри"""
descride_pet('harry', 'hamster')
descride_pet(animal_type= 'hamster', pet_name= 'harry')
descride_pet(pet_name= 'harry', animal_type= 'hamster')
