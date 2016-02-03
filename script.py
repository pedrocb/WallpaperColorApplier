import png
import random
import colorsys
import sys
import argparse

colorValueRangeMin = 0.10;

def apply_color():
    image = open(args.original_file)
    r=png.Reader(file=image)
    imageArray = list(r.read()[2])
    newImage = open(args.new_file,"wb")
    w=png.Writer(len(imageArray[0]),len(imageArray))
    newArray = list()
    width = len(imageArray[0])
    for y in range(len(imageArray)):
        newArray.append(list())
        for x in range(width):
            color = imageArray[y][x]
            hsv = colorsys.rgb_to_hsv(color/255.0,color/255.0,color/255.0)
            rgb = colorsys.hsv_to_rgb(args.hue[0]/360.0,args.saturation[0]/100.0, hsv[2]*(1-colorValueRangeMin) + colorValueRangeMin)
            for i in range(3):
                newArray[y].append(rgb[i]*255)
    png.from_array(newArray,'RGB').save(newImage)
    return imageArray
    
if "__main__" == __name__:
    parser = argparse.ArgumentParser()
    parser.add_argument('hue', metavar='H', type=int, nargs='+',
                        help='hue of the color')
    parser.add_argument('saturation', metavar='S', type=int, nargs='+', help='saturation of the color')
    parser.add_argument('original_file', metavar='i', help='File to modify')
    parser.add_argument('new_file', metavar='o', help="New File")
    args = parser.parse_args()
    print args.hue
    print args.saturation
    apply_color()
    
    
