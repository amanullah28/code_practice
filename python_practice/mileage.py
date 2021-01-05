# print('How many kilometer did you cycle today?');
kms = input("How many kilometer did you cycle today?");
miles = round(float(kms)/1.60934, 2);
print(f'Your {kms}km ride was {miles}mi ')