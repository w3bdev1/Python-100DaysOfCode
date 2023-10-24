print(r'''
                          _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print('Welcome to Treasure Island')
print('Your mission is to find the treasure')

right_or_left = input("You're at a crossroad. 'Right' or 'Left'?\n")
if right_or_left.lower() == 'left':
    swim_or_wait = input("You've come to a lake. 'Wait' for a boat or 'Swim' across\n")
    if swim_or_wait.lower() == 'wait':
        door = input("You've reached an island. There's a house with 3 different coloured doors. 'Red', 'Yellow' or 'Blue'\n")
        if door.lower() == 'yellow':
            print('Glittering treasures... Congrats you won!')
        else:
            print('Room full of beasts! Game Over :(')
    else:
        print("You're drowning! Game Over :(")
else:
    print("Falling into a hole. Game Over :(")


