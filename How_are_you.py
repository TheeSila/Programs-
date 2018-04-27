#Input function
person = input('''Hello, what's your name? : ''')
print('Hello,', person, ',how are you doing today?')

#Define the function and print '___'
def printme( sample ):
    "This prints a passed string into this function"
    print (sample)
    return

printme('-----------------------------------------------------------')

#Define the function
def emotion():
    operation = input('''
Please type in the number of the corresponding emotion you feel
1 for happiness
2 for joyfull
3 for anxiety
4 for depression
''')

#Check input with an IF statement
    if operation == '1':
        print('That is very good. I hope you feel like this forever.')
    elif operation == '2':
        print('That is just delightfull. Please continue to have fun.')
    elif operation == '3':
        print('That is to bad. Try to take a break or tackle the problem directly.')
    elif operation == '4':
        print('I am sorry to hear that. You should try talking about your feelings to friends or family.')
    else:
        print('You have not typed a valid emotion number, please retype the number.')
        emotion()
# Present the information outside of the function
emotion()
