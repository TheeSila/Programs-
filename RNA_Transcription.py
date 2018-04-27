def changeDNA():
    new = input('''
Enter a DNA strand to be traslated to RNA:
''')
    x = new
    for char in x:
        if char == 'A':
            print('U')
        elif char == 'T':
            print('A')
        elif char == 'C':
            print('G')
        elif char == 'G':
            print('C')
        else:
            print('That is not a valid base. Please recheck your spelling.')
changeDNA()
