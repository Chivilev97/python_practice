import random

heads = 0
tails = 0
toss = 0

while toss < 100:
    coin = random.randint(0,1)
    toss += 1
    if coin > 0:
        heads += 1
    elif coin < 1:
        tails += 1
print(f'Мы подброcили монету 100 раз, вот сколько раз выпала решка: {tails}. А вот сколько орел: {heads}.')

