#address = {
    #"location":"Kerimbwi",
    #"district":"Juja",

#print(address["location"])

#NESTED DICTIONARIES:

place = {
    "district 1":{"location":"Juja"},
    "district 2":{"location":"Doni"}
}
print(place["district 1"]["location"])



sneakers = {
    "lebrons":{"type":"soldier"},
    "westbrooks":{"type":"why not"}
}

print(sneakers["lebrons"]["type"])