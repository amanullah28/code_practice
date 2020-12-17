# A User class with both instance attributes and instance methods
class User:
	# active_users = 0

	# @classmethod
	# def display_active_users(cls):
	# 	return f"There are currently {cls.active_users} active users"

	# @classmethod
	# def from_string(cls, data_str):
	# 	first,last,age = data_str.split(",")
	# 	return cls(first, last, int(age))
	active_users = 0
	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"


	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))	

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"



# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())

# tom = User.from_string("Tom,Jones,89")
# print(tom.first)
# print(tom.full_name())
# print(tom.birthday())


class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		Moderator.total_mods += 1
		super().__init__(first, last, age)
		self.community  = community

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active mods"

	def remove_post(self):
		return f"{self.full_name()} removed a post from the {self.community} community"


u1 = User("aman", "arman", 27)
u2 = User("aman", "arman", 27)
u3 = User("aman", "arman", 27)
m1 = Moderator("aman", "arman", 27, "facebook")
m2 = Moderator("aman", "arman", 27, "facebook")
print(User.display_active_users())
print(Moderator.display_active_mods())

print(m1.remove_post())














