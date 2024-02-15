from operator import index, indexOf
import random
l = ['rocks','papers','scissors']
run = 'y'
while run.lower()=='y':
    bot_output = random.choice(['rocks','papers','scissors'])   
    user_input = input('Enter your choice : ')
    print(f'bot choose -> {bot_output}')
    print(f'------------------------{l.index(user_input)} {l.index(bot_output)} --->{l.index(user_input) == l.index(bot_output)-1}')
    if bot_output==user_input:
        print('draw , try again!')
    elif abs(l.index(user_input) - l.index(bot_output)) == 1:
        print('--')
    # else :
    #     if l.index(user_input) == l.index(bot_output)-1:
    #         print('bot wins')
    #     else:
    #         # print(f'{l.index(bot_output) == (l.index(user_input)-1)}')
    #         print('user wins')
    # elif l.index(bot_output) == (l.index(user_input)-1):
    #     print('bot +1')
    # elif (l.index(bot_output)-1) == (l.index(user_input)):
    #     print('user +1')
    # run = input('wish to continue? [y/n] : ') 