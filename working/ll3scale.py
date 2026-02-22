import xml.etree.ElementTree as ET

import math


def _vertical(length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    return {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}




def addLL3scale(doc, rl) -> ET.Element:
    "Adds the LL3 scale to the bottom rule, returns the doc"

    ybot = rl.topruleheight + rl.midruleheight + 200 # y value of bot of scale
    rightmove = rl.mainmove

    # LL3 mark
    LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    LLmark.text = "LL"
    LL3mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(ybot-28), "fill":"black", "font-size":"12"})
    LL3mark.text = "3"

    # e**x mark
    emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":str(ybot-36),"fill":"black", "font-size":"16"})
    emark.text = "e"
    exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":str(ybot-44),"fill":"black", "font-size":"12"})
    exmark.text = "x"
    return doc

    for r in range(0, 90000+1):
        # r is 0 to 90000   - this is along rule length
        x = 1 + r/10000
        x = math.exp(x)
        ypos = round(rightmove + rl.leftmargin + rl.scalewidth*math.log10(math.log(x)))
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





