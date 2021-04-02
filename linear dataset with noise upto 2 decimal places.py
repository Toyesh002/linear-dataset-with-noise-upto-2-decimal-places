import random


label=[]
for i in range(15):
    feature = random.randint(6, 20)
    print(feature,end=' ')

    for a in range(-2,2):
        noise=random.random()
        noise=round(noise,2)
        label.append( 3*feature + 4 + (noise))

print(f"\nlabel= {label}")

