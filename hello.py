import random

name=input("whats you name")
goal=input("gonna build first project")
experience=int(input("what is your experience?"))


boosts=["start working","first line","first file","first Project","Delivered"]

print(f"Hey {name}")
print(f" in {goal}")
print(f" my experience is {experience}")

print(f"{random.choice(boosts)}")


