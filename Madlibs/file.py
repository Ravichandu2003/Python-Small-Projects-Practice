story = """Most doctors agree that riding a bicycle is an excellent form of exercise. 
A bicycle enables you to develop your leg muscles and increase the rate of your heartbeat. 
More people around the world use bicycles than drive cars. 
No matter what kind of person you are, always be sure to wear a good helmet. 
Make sure to have yellow reflectors too!"""

#inputs
name = input("Enter your name: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
part_of_body = input("Enter a body part: ")
adverb = input("Enter an adverb: ")
noun = input("Enter a noun: ")
animals = input("Enter an animal (plural): ")
color = input("Enter a color: ")

#filling blanks
mad_lib_story = f"Most doctors agree that riding a bicycle of {verb} is a/an {adjective} form of exercise. {verb} a bicycle enables you to develop your {part_of_body} muscles as well as {adverb} increase the rate of a {part_of_body} beat. More {noun} around the world {verb} bicycles than drive {animals}. No matter what kind of {noun} you {verb}, always be sure to wear a/an {adjective} helmet. Make sure to have {color} reflectors too!"

#display output
print(mad_lib_story) 
