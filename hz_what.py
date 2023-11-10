# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#     def introduce(self):
#         return f"Hello, my name is {self.name} and i am {self.age} years old"
    
# Person1 = Person("Alice",30)

# print("name:", Person1.name)
# print("age:", Person1.age)

# print(Person1.introduce())
#afasfasfasfasf VERSION

import psycopg2

conn = psycopg2.connect(host = '127.0.0.1',
                        database = 'postgres',
                        user = 'postgres',
                        password = '123')

cur = conn.cursor()
#cur.execute('Select first_name from actor limit 5;')
#username = [r[0] for r in cur.fetchall()]
#print(username)

usernames= ['Arlan','Tatzhik','Sanzhik']
Found= False
while not Found:
    username = input('Введите свой логин: ')
    if username in usernames:
        print('Поздравляю вы в списке')
        Found=True
    else:
       print('Вы не местный. Зарегестрируйтесь правельно)')
def binary_search(username):
    if (username) in usernames:
        return True
    else:
        return False

#fdfsdgfsd




conn.commit()
cur.close()
conn.close()