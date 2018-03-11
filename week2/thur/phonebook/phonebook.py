import json
with open('phonebook.json', 'r') as fh:
    data = json.load(fh)
print('Electronic Phone Book')
while True:
    print('=' * 20)
    print('1. Look up an entry')
    print('2. Set an entry')
    print('3. Delte an Entry')
    print('4. List all entries')
    print('5. Save entries')
    print('6. Restore entries')
    print('7. Quit')
    choice = input('What would you like to do? ')
    if choice == '1':
        who = input('Look up who? ').lower()
        found = False
        for key, value in data.items():
            if who == key.lower():
                print('\n\nFound entry for {}:'.format(key.capitalize()))
                print('Phone: '+ data[key]['phone'])
                print('Address: '+ data[key]['address'])
                print('Email: '+ data[key]['email'])
                found = True
            else:
                pass
        if found != True:
            print('\n\nNo entry found')
        else:
            pass
    elif choice == '2':
        name = input('Name: ').lower()
        num = input('Phone number: ')
        address = input('Address: ').upper()
        email = input('Email: ')
        data[name] = {'phone':num,'address':address,'email':email}
        print('\n\nAdded')
    elif choice == '3':
        who = input('Delete which entry: ').lower()
        del data[who]
        print("\n\nDeleted")
    elif choice == '4':
        print("\nPhonebook")
        print('-'*20)
        for key, value in data.items():
            print(key.capitalize() + ': Phone: '+ data[key]['phone']+ ' Address: '
            + data[key]['address']+ ' Email: ' + data[key]['email'])
    elif choice == '5':
        with open('phonebook.json', 'w') as fh:
            json.dump(data, fh)
    elif choice == '6':
        with open('phonebook.json', 'r') as fh:
            json.load(data, fh)
    elif choice == '7':
        break