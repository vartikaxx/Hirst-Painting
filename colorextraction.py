import colorgram

# EXTRACTION OF COLORS FROM IMAGE
rgb_colors=[]
color = colorgram.extract("image.webp",20)
# print(color)
for c in color:
    r=c.rgb.r
    g=c.rgb.g
    b=c.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)
    # rgb_colors.append(c.rgb)
print(rgb_colors)