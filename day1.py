with open("day_1_in.txt", "r") as f:
    content = f.readlines()
    depths = [int(i.strip()) for i in content]

up = 0
for i, j in enumerate(depths[1:]):
    if j > depths[i]:
        up += 1

triplets = [depths[i] + depths[i+1] + depths[i+2] for i,j in enumerate(depths[:-2])]

up3 = 0
for i, j in enumerate(triplets[1:]):
    if j > triplets[i]:
        up3 += 1


print(up)
print(up3)
