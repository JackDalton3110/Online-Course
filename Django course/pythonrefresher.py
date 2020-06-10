age = 12
name = "Julie"
sentence = "Hi my name is {} and I am {} years old".format(name, age)
TodayIsCold = True

"""if age > 18:
    #print("You can access the ride")
else:
    #print("No way boiii")

if TodayIsCold:
    #print("Better bring a jacket")
else:
    #print("Jaysus tis roasting")

year = 2120

if year >= 2000 and year <= 2100:
    #print("Welcome to the 21st Century")
else:
    #print("You are before or after the 21st century")


def trippleprint(theString):
    return(theString+theString+theString)

response=trippleprint("Hello")
print(response)

dognames=["Fito", "Max", "Molly", "Charlie"]
print(dognames)
dognames.insert(0,"Petal")
print(dognames[3])
del(dognames[3])
print (dognames)

shoes = ["Spizikes", "Air Force 1", "Curry 2 ", "Melo 5"]
print(shoes)

for i in range(0,4):
    print(dognames[i])

numbers=[110,12,53,9230,2034,41,72,99,90,108,120]
for i in numbers:
    if i > 90:
        print(i)


dogs = {"Fido":8, "Sally": 17, "Max": 11}
print(dogs["Max"])
del(dogs["Sally"])
print(dogs)

words=["Ice", "Sun", "Beer", "Phone"]
definitions=["Frozen Water", "Hot", "Tasty", "Screen"]
Max = len(words)
coolDictionary={}
for i in range(0, Max):
    coolDictionary[words[i]]=definitions[i]

print(coolDictionary)"""

class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print("WOOF")

mydog = Dog("Max", 11, "West highland terrier")


mydog.bark()
print(mydog.name)
print(mydog.age)
print(mydog.breed)


class Car:
    def __init__(self, age=10):
        self.age = age

    def returnAge (self):
        return self.age

myCar = Car()
print(myCar.age)