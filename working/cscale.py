import xml.etree.ElementTree as ET

import math


def _vertical(length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    return {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}




def addCscale(doc, rl) -> ET.Element:
    "Adds the C scale to the middle rule, returns the doc"

    ybot = rl.topruleheight + rl.midruleheight # y value of bot of scale
    rightmove = rl.slidermove

    # C mark
    Cmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 8), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    Cmark.text = "C"

    # Pi mark
    xpos = round(rightmove + rl.leftmargin + rl.scalewidth*math.log10(math.pi))
    Pimark = ET.SubElement(doc, 'text', {"x":str(xpos-4), "y":str(ybot-47), "fill":"black", "font-size":"16"})
    Pimark.text = "\u03C0"
    ET.SubElement(doc, 'line', _vertical(40, xpos, ybot))

    # x mark
    xmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 12), "y":str(ybot-32),"fill":"black", "font-size":"16"})
    xmark.text = "x"

    for r in range(0, 90000+1):
        # r is 0 to 90000   - this is along rule length
        # x is 1 to 10 inclusive
        x = 1 + r/10000
        xpos = round(rightmove + rl.leftmargin + rl.scalewidth*math.log10(x))
        length = 0
        textstr = ''
        fontsize = 16
        texty = ybot-80
        if not r:                   # at x == 1, r = 0
            length = 70
            textstr = "1"
            fontsize = 18
        elif r == 90000:            # at x == 10, r= 90000
            length = 70
            textstr = "10"
            fontsize = 18
        elif r % 10000 == 0:         # at x = 2, 3, etc 
            length = 60
            textstr = str(round(x))
            fontsize = 18
            texty = ybot-66
        elif r % 5000 == 0:         # at x = 1.5, 2.5, 3.5, etc 
            length = 50
            textstr = str(x)
            fontsize = 14
            texty = ybot-55
        elif r % 1000 == 0:         # at x = 1.1, 1.2, etc 
            length = 30
            if r < 10000:           # only do text for x<2, r <10000  
                textstr = str(x)
                fontsize = 12
                texty = ybot-33
        elif r < 20000:             # x < 3, r < 20000
            if r % 500 == 0:        # at x =1.05, 1.15, etc
                length = 20

        if length:
            vline = _vertical(length, xpos, ybot, col="black")
            ET.SubElement(doc, 'line', vline)
        if textstr:
            if len(textstr) == 1:
                textpos = xpos - 4    #  textpos This is in pixels
            else:
                textpos = xpos - 6    # three characters, such as 1.5
            tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
            tel.text = textstr

    return doc





