import random
import collections
queue_customers = []
dict_cust_info = {}

def randomName() :
    asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander",
    "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman",
    "Singing Bush"]
    iRandomNum = random.randint(0,8)
    return asCustomers[iRandomNum]

def randomBurgers() :
    return random.randint(1, 20)

for i in range(100):
    cust_name = randomName()
    cust_burgers = randomBurgers()
    queue_customers.append(cust_name)

for cust_name in queue_customers:
    if cust_name not in dict_cust_info:
        dict_cust_info[cust_name] = randomBurgers()
    else:
        dict_cust_info[cust_name] += randomBurgers()


