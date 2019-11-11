gunnar = input()
emma = input()
gunnar1,gunnar2,gunnar3,gunnar4 = gunnar.split(" ")
emma1,emma2,emma3,emma4 = emma.split(" ")
gunnartotal = int(gunnar1) + int(gunnar2) + int(gunnar3) + int(gunnar4)
emmatotal = int(emma1) + int(emma2) + int(emma3) + int(emma4)
if gunnartotal > emmatotal:
    print("Gunnar")
elif gunnartotal < emmatotal:
    print("Emma")
else:
    print("Tie")