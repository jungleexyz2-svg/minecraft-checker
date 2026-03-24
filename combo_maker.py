from faker import Faker;import random
f=Faker();c=[]
for _ in range(25000):
 n=f.name().lower().replace(" ","")+str(random.randint(1000,9999))
 c.append(f"{n}@hotmail.com:{random.choice([n,'minecraft123','hypixel456'])}")
with open("minecraft_hotmail_combos.txt","w")as x:[x.write(l+"\n")for l in c]
print("✅ 25k combos generated!")
