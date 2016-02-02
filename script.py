import png
import random
import colorsys
import sys

imageToModify = "1941277.png"
newImageName = "newWallpaper1.png"


colorHue = random.random()*360.0;
colorSaturation = random.random()*50.0 + 50.0;
colorValueRangeMin = 0.10;

def apply_color():
    image = open(imageToModify)
    r=png.Reader(file=image)
    imageArray = list(r.read()[2])
    newImage = open(newImageName,"wb")
    w=png.Writer(len(imageArray[0]),len(imageArray))
    newArray = list()
    width = len(imageArray[0])
    for y in range(len(imageArray)):
        newArray.append(list())
        for x in range(width):
            color = imageArray[y][x]
            hsv = colorsys.rgb_to_hsv(color/255.0,color/255.0,color/255.0)
            rgb = colorsys.hsv_to_rgb(colorHue/360.0,colorSaturation/100.0, hsv[2]*(1-colorValueRangeMin) + colorValueRangeMin)
            for i in range(3):
                newArray[y].append(rgb[i]*255)
    png.from_array(newArray,'RGB').save(newImage)
    return imageArray
    
if "__main__" == __name__:
    apply_color()
    
    
