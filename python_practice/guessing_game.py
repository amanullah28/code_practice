import random

# print(guess_difference)

while True:
	random_number = random.randint(1,10);
	print(random_number);
	user_input = input("Enter a guessing number from 1 to 10:  ");
	user_input = int(user_input);
	guess_difference = user_input-random_number;
	guess_message = None;
	if guess_difference == 0:
		guess_message = 'You guessed it!!';
	elif guess_difference>0:
		if guess_difference>2:
				guess_message = 'Too high';
		else: 
			guess_message = 'Almost there';
	elif guess_difference<0: 
		if guess_difference<-2:
			guess_message = 'Too low';
		else:
			guess_message = 'Almost there'

	print(guess_message);

	play_again = input("Want to play again? (y/n)");
	if play_again == 'y':
		continue;
	else:
		print("Thank you for playing!")
		break;

