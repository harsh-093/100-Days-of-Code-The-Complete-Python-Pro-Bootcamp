import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user=int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSOR."))
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("INVALID CHOICE.")

rps = random.randint(0,2)
print(f"Computer chose: {rps}")
if rps == 0:
    print(rock)
elif rps == 1:
    print(paper)
else:
    print(scissors)

if user == 0 and rps==2:
    print("YOU WIN!")
elif user > rps:
    print("YOU WIN!")
elif user == rps:
    print("TIE.")
else:
    print("YOU LOSE.")