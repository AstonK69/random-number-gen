from random import randint

print(""" /$$$$$$$                            /$$                         /$$   /$$                          /$$$$$$                     
| $$__  $$                          | $$                        | $$$ | $$                         /$$__  $$                    
| $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$ | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$  \__/  /$$$$$$  /$$$$$$$ 
| $$$$$$$/ |____  $$| $$__  $$ /$$__  $$ /$$__  $$| $$_  $$_  $$| $$ $$ $$| $$  | $$| $$_  $$_  $$| $$ /$$$$ /$$__  $$| $$__  $$
| $$__  $$  /$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$| $$ \ $$ \ $$| $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$|_  $$| $$$$$$$$| $$  \ $$
| $$  \ $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$\  $$$| $$  | $$| $$ | $$ | $$| $$  \ $$| $$_____/| $$  | $$
| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$| $$ \  $$|  $$$$$$/| $$ | $$ | $$|  $$$$$$/|  $$$$$$$| $$  | $$
|__/  |__/ \_______/|__/  |__/ \_______/ \______/ |__/ |__/ |__/|__/  \__/ \______/ |__/ |__/ |__/ \______/  \_______/|__/  |__/
                                                                                                                                
                                                                                                                                
                                                                                                                                """)

amount = input('How many numbers do you want? ')
low = input('\nWhat do you want the number to be above? ')
high = input('\nWhat do you want the number to be below? ')

number1 = amount.isnumeric()
number2 = amount.isnumeric()
number3 = amount.isnumeric()

if number1 is True:
    if number2 is True:
        if number3 is True:
            for i in range(int(amount)):
                print(randint(int(low), int(high)))
        else:
            print('Write numbers dumbass!')
    else:
        print('Write numbers dumbass!')
else:
    print('Write numbers dumbass!')
input('Press Enter To Exit!')


