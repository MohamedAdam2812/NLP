import re

patterns = [

("[0-9]+", "The student strength is 31 but the perfection percentage is 100."),

("[A-Z][a-z]+", "Athi and Meenakshi handle the NLP."),

("[aeiou]+", "Natural Language ProcessingEssentials."),
("[a-z]+@[a-z]+\.com", "Gmail id is person@gmail.com")]

for pattern, text in patterns: 
print("Pattern:", pattern) 
print("Text:", text) 
matches = re.findall(pattern, text)
if matches:
print("Matches found:",matches)
else:
print("not found")

