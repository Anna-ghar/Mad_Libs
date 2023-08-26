import random

nouns = ["chair", "tree", "apple", "car", "mountain", "table", "book", "light", "river", "park", "sun", "bicycle"]
template = int(input("Which template do you want? 1 or 2? "))


if template == 1:
    PersonName = input("Input PersonName: ")
    Noun = random.choice(nouns)
    Adjective1 = input("Input adjective (feeling): ")
    Verb1 = input("Input verb: ")
    Adjective2 = input("Input adjective (feeling): ")
    Animal1 = input("Input an animal: ")
    Verb2 = input("Input verb: ")
    Color1 = input("Input a color: ")
    Verb3 = input("Input a verb + ing: ")
    Adverb = input("Input an adverb + ly: ")
    Number1 = input("Input a number: ")
    Time = input("Measure of time: ")
    Color2 = input("Input a color: ")
    Animal2 = input("Input an animal: ")
    Number2 = input("Input a number: ")
    SillyWord = input("Input a silly word: ")
    Noun2 = random.choice(nouns)
    

    mad_libs = '''This weekend I am going camping with {PersonName}. I packed my lantern, sleeping bag, and {Noun}.
    I am so {Adjective1} to {Verb1} in a tent. I am {Adjective2} we might see a(n) {Animal1}, I hear they are kind of
    dangerous. While we are camping, we are going to hike, fish, and {Verb2}. I have heard that the {Color1} lake is
    great for {Verb3}. Then we will {Adverb} hike through the forest for {Number1} {Time}. If I see a {Color2}
    {Animal2} while hiking, I am going to bring it home as a pet! At night we will tell {Number2} {SillyWord} stories
    and roast {Noun2} around the campfire!!'''

    print(mad_libs)

elif template == 2:
    Number1 = input("Input a number: ")
    Time_measure = input("Input a measure of time: ")
    Transportation_mode = input("Input a mode of transportation: ")
    Adjective1 = input("Input an adjective: ")
    Adjective2 = input("Input another adjective: ")
    Noun1 = random.choice(nouns)
    Color = input("Input a color: ")
    Body_part1 = input("Input a part of body: ")
    Verb1 = input("Input a verb: ")
    Number2 = input("Input another number: ")
    Noun2 = random.choice(nouns)
    Noun3 = random.choice(nouns)
    Body_part2 = input("Input a part of body: ")
    Verb2 = input("Input a verb: ")
    Noun4 = random.choice(nouns)
    Adjective3 = input("Input an adjective: ")
    SillyWord = input("Input a silly word: ")
    Noun5 = random.choice(nouns)

    mad_libs = f'''It was about {Number1} {Time_measure} ago when I arrived at the hospital in a {Transportation_mode}.
     The hospital is a/an {Adjective1} place, there are a lot of {Adjective2} {Noun1} here. There are nurses here who
     have {Color} {Body_part1}. If someone wants to come into my room I told them that they have to {Verb1} first. I’ve
     decorated my room with {Number2} {Noun2}. Today I talked to a doctor and they were wearing a {Noun3} on their
     {Body_part2}. I heard that all doctors {Verb2} {Noun4} every day for breakfast. The most {Adjective3} thing about
      being in the hospital is the {SillyWord} {Noun5} !'''

    
    print(mad_libs)
else:
    print("Invalid template choice. Please choose 1 or 2.")
