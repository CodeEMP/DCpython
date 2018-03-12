class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.greeted = []
    
    def greet(self, other_person):
        print('Hello {}, I am {}'.format(other_person.name, self.name))
        self.greeting_count += 1
        if other_person.name not in self.greeted:
            self.greeted.append(other_person.name)
        else:
            pass
    
    def print_contact_info(self):
        print('{}\'s Email:{} Phone:{}'.format(self.name, self.email, self.phone))
        
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        print(len(self.friends))
        
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)
        
    def number_of_unique_people_greeted(self):
        print(len(self.greeted))

if __name__ == "__main__":        
    sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
    jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')
    print(sonny.greeting_count)
    sonny.greet(jordan)
    jordan.greet(sonny)
    print(sonny.greeting_count)
    print('{}\'s Email:{} Phone:{}'.format(sonny.name, sonny.email, sonny.phone))
    print('{}\'s Email:{} Phone:{}'.format(jordan.name, jordan.email, jordan.phone))
    jimbo = Person('Jimbo', 'jimbony@yahoo.com', '466-821-5164')
    sonny.greet(jordan)
    sonny.number_of_unique_people_greeted()
    sonny.greet(jimbo)
    sonny.number_of_unique_people_greeted()