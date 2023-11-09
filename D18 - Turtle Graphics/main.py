import colorgram

colors = colorgram.extract("image.jpg", 30)
colors = [tuple(color.rgb) for color in colors]

print(colors)
