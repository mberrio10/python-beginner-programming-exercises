# ✅↓ Write your code here ↓✅
def number_of_bottles(): 
    numberOfBottles = 5 
    for i in range(numberOfBottles, 0, -1): 
        bottle_word = "bottle" if number_of_bottles == 1 else "bottles"
        print(f"{numberOfBottles} {bottle_word} of milk on the wall, {numberOfBottles} {bottle_word} of milk.") 
        numberOfBottles -= 1 
        bottle_word = "bottle" if number_of_bottles == 1 else "bottles"
        if numberOfBottles == 0:
            print ("No more bottles of milk on the wall, no more bottles of milk.")
            print ("Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(f"Take one down and pass it around, {numberOfBottles} {bottle_word} of milk on the wall.")

number_of_bottles()