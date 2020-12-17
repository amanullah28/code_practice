class Pet:
	allowed = ['cat', 'dog', 'hen']
	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have {species} pet!")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have {species} pet!")
		self.species = species





pet1 = Pet('jingle', 'cat')
pet2 = Pet('jhandu', 'dog')
print(pet2.species)
# pet2.species = "dfjdf"
pet2.set_species('cat')
print(pet2.species)

pet2.species = 'dfndf'
print(pet2.species)

# print(cat.name, cat.species)
