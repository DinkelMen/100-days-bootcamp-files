import colorgram

colors = colorgram.extract('Hirst_painting.jpg', 15)

lis = []

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    lis.append(new_color)
print(lis)

lis = [(188, 19, 46), (244, 233, 64), (252, 232, 237), (217, 239, 245), (195, 76, 34)
    , (218, 66, 106), (13, 143, 89), (18, 125, 173), (196, 176, 17), (108, 182, 209), (12, 167, 214), (208, 154, 91), (238, 232, 3)]
