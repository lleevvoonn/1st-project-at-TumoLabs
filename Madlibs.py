def story_1():
    Number = int (input ("Enter a number"))
    Measure_of_time = (input ("Enter the Measure of time"))
    Mode_of_transportation = input ("Enter a Mode of transportation")
    Adjective = input  ("Enter an adjective")
    Adjective2 = input  ("Enter an adjective")
    Noun = input  ("Enter a noun")
    Color = input  ("Enter a color")
    Part_of_the_body = input  ("Enter a part of the body")
    Verb = input  ("Enter a verb")
    Noun2 = input  ("Enter a noun")
    Number2 = int (input  ("Enter a number"))
    Noun3 = input ("Enter a noun")
    Part_of_the_body2 = input  ("Enter a Part of the body")
    Verb = input  ("Enter a verb")
    Noun4 = input  ("Enter a noun")
    Adjective3 = input  ("Enter an adjective")
    Silly_word = input  ("Enter a Silly word")
    Noun = input  ("Enter a noun")

    story1 = f"It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_transportation}. The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here who have {Color} {Part_of_the_body}. If someone wants to come into my room I told them that they have to {Verb} first. I have decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their {Part_of_the_body2}. I heard that all doctors {Verb} {Noun4} every day for breakfast. The most {Adjective3} thing about being in the hospital is the {Silly_word} {Noun} !"
    print(story1)


def story_2():
    Persons_name = input  ("Enter a persons name")
    Noun = input  ("Enter a noun")
    Feeling = input  ("Enter a feeling")
    Verb = input  ("Enter a verb")
    Feeling2 = input  ("Enter a feeling")
    Animal = input  ("Enter a animal")
    Verb2 = input  ("Enter a verb")
    Color = input  ("Enter a color")
    Verb3 = input  ("Enter a verb")
    Adverb = input  ("Enter a adverb")
    Number = int (input  ("Enter a feeling"))
    Measure_of_time = int (input  ("Enter a Measure of time"))
    Color2 = input  ("Enter a color")
    Animal2 = input  ("Enter a animal")
    Noun = input  ("Enter a noun")
    Silly_word = input  ("Enter a silly word")
    Noun2 = input  ("Enter a noun")

    story2 = f"This weekend I am going camping with {Persons_name}. I packed my lantern, sleeping bag, and {Noun}. I am so {Feeling} to {Verb} in a tent. I am {Feeling2} we might see a(n) {Animal}, I hear they are kind of dangerous. While we were camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color} lake is great for ,{Verb3}. Then we will {Adverb} hike through the forest for {Number} {Measure_of_time}. If I see a {Color} {Animal} while hiking, I am going to bring it home as a pet! At night we will tell {Number} {Silly_word} stories and roast {Noun2} around the campfire!! "
    print(story2)

def story_3():
    Persons_name = input  ("Enter a persons name")
    Adjective = input  ("Enter an adjective")
    Color = input  ("Enter a color")
    animal = input  ("Enter an animal")
    place = input  ("Enter a place")
    Adjective2 = input  ("Enter an adjective")
    Magical_creature = input  ("Enter a magical creature")
    Adjective3 = input  ("Enter an adjective")
    Magical_creature2 = input  ("Enter a magical creature")
    Room_in_a_house = input  ("Enter a room in a house")
    Noun = input  ("Enter a noun")
    Noun2 = input  ("Enter a noun")
    Noun3 = input  ("Enter a noun")
    Adjective4 = input  ("Enter an adjective")
    Noun4 = input  ("enter a number")
    Number = int ( input  ("enter a number"))
    Measure_of_time = int ( input  ("enter a measure of time"))
    Verb = input  ("enter a verb")
    Adjective5 = input  ("enter an adjective")
    Noun5 = input  ("enter a noun")

    story3 = f"Dear {Persons_name}, I am writing to you from a {Adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {Color} {animal} in {place}. There are {Adjective2} {Magical_creature} and {Adjective3} {Magical_creature2} here! In the {Room_in_a_house} there is a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun3} and dream of {Adjective4} {Noun4}. It feels as though I have lived here for {Number} {Measure_of_time}. I hope one day you can visit, although the only way to get here now is {Verb} on a {Adjective5} {Noun5}!!"
    print(story3)

a = input("Do you want to play MadLibs? y/n")
if a == "yes":
    print("Ok, let's get started")
    b = input("Choose template,  ")
    if b == "3":
        story_3()
    elif b == "1":
        story_1()
    elif b == "2":
        story_2()
    elif b == "random":
        import random
        b = random.randint(1, 3)
        print (b)
        if b == 3:
            story_3()
        elif b == 1:
            story_1()
        elif b == 2:
            story_2()

    
