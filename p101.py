import random

dice_probability = [
    f'''[   ]
[ 0 ]
[   ]''',
    f'''[   ]
[0 0]
[   ]''',
    f'''[   ]
[000]
[   ]''',
    f'''[0 0]
[   ]
[0 0]''',
    f'''[0 0]
[ 0 ]
[0 0]''',
    f'''[0 0]
[0 0]
[0 0]''',
]

run = True

while run:
    rolled = input("pres y to roll again and n to exit : ")

    if rolled == "y":
        ran = random.randint(0,5)
        print(dice_probability[ran])
    elif rolled == "n":
        run = False