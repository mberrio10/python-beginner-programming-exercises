import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
	# ✅ ↓ your code here ↓ ✅
	bullet = spin_chamber()
	for i in range (6):
		if bullet == i:
			fire = "You are dead!"
		else:
			fire = "Keep playing!"
	return fire

print(fire_gun())
