def blend(color1, color2, per):
    color3 = []
    for x in range(3):
        y = int(((color1[x]*per)+(color2[x]*(1-per))))
        color3.append(y)
    return color3

print(blend([255, 200, 50], [255, 100, 0], .3))
