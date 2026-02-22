import xml.etree.ElementTree as ET

import math


def _vertical(length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the starting y position
       xpos is the x position
       col is the colour of the line"""
    # get xpos to the nearest .25
    xpos = round(xpos*4)/4.0
    return {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}


def addDFscale(doc, rl) -> ET.Element:
    "Adds the DF scale to the top rule, returns the doc"

    ybot = rl.topruleheight # y value of bottom of the top scale
    rightmove = rl.mainmove

    # DF mark
    DFmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":str(ybot-25),"fill":"black", "font-size":"24"})
    DFmark.text = "DF"

    # Pi mark
    xpos = rightmove + rl.leftmargin
    xpos = round(xpos*4)/4.0
    Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(ybot-45),"fill":"black", "font-size":"16"})
    Pimark.text = "\u03C0"
    ET.SubElement(doc, 'line', _vertical(40, xpos, ybot))

    # pix mark
    pixmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":str(ybot-30),"fill":"black", "font-size":"16"})
    pixmark.text = "\u03C0x"

    # start r
    # r = (x-1)x10000
    # r = (3.13 -1)x 10000  -- 3.13 to get beyond 3.1 but befor pi
    # r = 21300

    # end r
    # r = (31 - 1)x 10000
    # r = 300000


    for r in range(21300, 300000+1):
        # r is 0 to 90000   - this is along rule length
        # x is 1 to 10 inclusive
        x = 1 + r/10000
        # move to the left by log pi
        xpos = rightmove + rl.leftmargin + rl.scalewidth*math.log10(x) - rl.scalewidth*math.log10(math.pi)
        length = 0
        textstr = ''
        fontsize = 16
        texty = ybot-76
        if r == 90000 or r == 190000 or r == 290000:            # at x == 10,20,30
            length = 70
            textstr = str(round(x))
            fontsize = 18
        elif r % 10000 == 0 and r<90000:         # at x = 2, 3, etc up to x<10
            length = 60
            textstr = str(round(x))
            fontsize = 18
            texty = ybot-67
        elif r == 140000 or r == 240000:                  # at x = 15, 25, r = 140000, 240000
            length = 60
            textstr = str(round(x))
            fontsize = 14
            texty = ybot-65
        elif r % 10000 == 0:         # at x = 11, 12, etc, and r must be greater than 90000, x>10
            length = 30
            if r < 190000:           # only do text for x<20, r <190000
                textstr = f"{x:.0f}"
                fontsize = 12
                texty = ybot-35
        elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc However text only at x<10
            if r < 90000:
                length = 50         # text and long length x < 10, short length only at x>10
                textstr = str(x)
                fontsize = 14
                texty = ybot-55
            else:
                length = 20           
        elif r % 5000 == 0 and r < 200000:             # x < 30, r < 200000
                length = 20                         # at x =10.5, 11.5, etc
        elif r % 1000 == 0 and r<90000:         # at x = 1.1, 1.2, etc up to x<10, r<90000 
            length = 30


        if length:
            vline = _vertical(length, xpos, ybot, col="black")
            ET.SubElement(doc, 'line', vline)
        if textstr:
            if len(textstr) == 1:
                textpos = round(xpos - 4)    #  textpos This is in pixels
            else:
                textpos = round(xpos - 6)    # three characters, such as 1.5
            tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
            tel.text = textstr

    return doc

