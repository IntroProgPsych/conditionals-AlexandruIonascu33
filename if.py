# if = does some code ONLY IF a condition is True
# Else is going to do nothing

age = int(input("Type you age"))
if age>=18 and age<100:
    print("You are an adult")
elif age>=100:
    print("You are too old")
elif age<0:
    print("You have`nt been born yet")
else:
    print("You are a child")