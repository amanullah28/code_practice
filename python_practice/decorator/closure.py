from random import choice

def make_laugh_func(person):
	def get_laugh():
		laugh = choice(('HAHAHAHA', 'lol', 'tehehe'))
		return f"{laugh} {person}"
	return get_laugh

laugh_at = make_laugh_func("Aman")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())