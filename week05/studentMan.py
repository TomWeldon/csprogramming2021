def displayMenu():
    print('What would you like to do ?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (q) Quit')
    choice = input('type on letter (a/v/q) : ').strip()

    return choice

choice = displayMenu()

#print('You chose {}'.format(choice))

def doAdd():

    print('in adding')

def doView():

    print('in viewing')

# main program

choice = displayMenu()

while(choice != 'q'):
    if choice == 'a':
        doAdd()
        
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print('\n\nplease select either a,v or q')
    choice = displayMenu()
       


