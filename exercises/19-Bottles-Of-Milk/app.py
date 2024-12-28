# ✅↓ Write your code here ↓✅
def number_of_bottles(): 
    numberOfBottles = 99 
    for i in range(numberOfBottles, 0, -1):     
        bottle_word = "bottle" if numberOfBottles == 1 else "bottles"
        
        if numberOfBottles == 1:
            print (f"{numberOfBottles} {bottle_word} of milk on the wall, {numberOfBottles} {bottle_word} of milk. Take one down and pass it around, no more bottles of milk on the wall.")
            print ("No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            single_word = "bottle" if numberOfBottles - 1 == 1 else "bottles"
            print(f"{numberOfBottles} {bottle_word} of milk on the wall, {numberOfBottles} {bottle_word} of milk. Take one down and pass it around, {numberOfBottles - 1} {single_word} of milk on the wall.") 

        numberOfBottles -= 1
number_of_bottles()