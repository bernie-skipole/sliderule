import xml.etree.ElementTree as ET

import math


def _vertical(length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    # get xpos to the nearest .25
    xpos = round(xpos*4)/4.0
    return {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}


def _text(doc, textstr, xpos, texty, fontsize):
    if textstr:
        if len(textstr) == 1:
            textpos = round(xpos - 4)    #  textpos This is in pixels
        else:
            textpos = round(xpos - 6)    # three characters, such as 1.5
        
        tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
        tel.text = textstr




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


    m = rl.scalewidth/math.log10(math.log(10))

    # start at x = e
    xpos = rightmove + rl.leftmargin
    length = 30
    textstr = "e"
    fontsize = 18
    texty = ybot-40

    vline = _vertical(length, xpos, ybot, col="black")
    ET.SubElement(doc, 'line', vline)

    _text(doc, textstr, xpos, texty, fontsize)

    # x from 2.72 to 2.99 in steps of 0.1
    for r in range(272, 300):
        x = r/100.0
        xpos = rightmove + rl.leftmargin + m*math.log10(math.log(x))
        textstr = ''
        length = 0
        if r % 10 == 0:
            length = 20
            textstr = str(x)
            fontsize = 16
            texty = ybot-30
        elif r % 5 == 0:
            length = 15
        else:
            length = 10


        if length:
            vline = _vertical(length, xpos, ybot, col="black")
            ET.SubElement(doc, 'line', vline)

        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)


    return doc





