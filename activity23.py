gutom = ['cupcake','donut','coffee','milktea','cookies']
gutom.append('gummy')   #add an item to the last of the list
print(gutom)
gutom.pop()    #remove the last item
print(gutom)
gutom.insert(0,'donut')   #add item in dif position
print(gutom)
for i in gutom:
    print(f"{i}  in the basket")    #all fruits one by one with 'in the basket' at the last

ako = 'akoy nagugutom na'
for u in ako:
    print(u)    #Will print my name from j to n
print("\nReversed\n")
for q in ako[::-1]:  #will print my name in reverse from n to j
    print(q)
