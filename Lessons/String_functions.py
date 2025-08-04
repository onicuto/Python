word = "Hello"
print(word[1])
print(len(word))
print(word.count("l"))
print(word.upper())
print(word.isupper())
print(word.islower())
print(word.lower())
print(word.capitalize())
print(word.find("ll"))
print(word[0:4])

word_str = "Football,basketball,skate"
hobby = word_str.split(",")
print(hobby[1])
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)
result = ", ".join(hobby)
print(result)
