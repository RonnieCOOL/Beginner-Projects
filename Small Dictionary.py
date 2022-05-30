# Q) Create a dictionary and take input from the user and return the meaning  of the word from the dictionary provided that user writes word that are in the dictionary

dict = {"Abandon": "to turn away from or to discontinue", "Immortal": "not susceptible to death", "Tangible": "touchable; able to touch or felt", "Intelligent": "of high or especially quick cognitive", "Permission": "authorisation; consent(especiallt fromal consent from someone in authority)"}

print("Enter a word you want to search meaning among 'Abandon', 'Immortal', 'Tangible', 'Intelligent', 'Permission'")
inpword = input()

print("The meaning of", inpword, "is", dict[inpword], ".")
