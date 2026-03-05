import xml.etree.ElementTree as ET

import math


def _vertical(doc, length, xpos, ybot, col="black") -> dict:
    """length is the length of the vertical line
       ybot is the ending y position
       xpos is the x position
       col is the colour of the line"""
    # get xpos to the nearest .25
    xpos = round(xpos*4)/4.0
    vline = {"x1":str(xpos), "y1":str(ybot), "x2":str(xpos), "y2":str(ybot-length), "style":f"stroke:{col};stroke-width:1"}
    ET.SubElement(doc, 'line', vline)

def _text(doc, textstr, xpos, texty, fontsize):
    if textstr:
        if len(textstr) == 1:
            textpos = round(xpos - 4)    #  textpos This is in pixels
        else:
            textpos = round(xpos - 6)    # three characters, such as 1.5
        
        tel = ET.SubElement(doc, 'text', {"x":str(textpos), "y":str(texty),"fill":"black", "font-size":str(fontsize)})
        tel.text = textstr




def addLL2scale(rl, rightmove) -> ET.Element:
    "Adds the LL2 scale to the rule, returns the scale element"

    ybot = 0

    doc = ET.Element('g')

    # LL2 mark
    LLmark = ET.SubElement(doc, 'text', {"x":str(rightmove + 6), "y":str(ybot-30), "fill":"black", "font-size":"24"})
    LLmark.text = "LL"
    LL3mark = ET.SubElement(doc, 'text', {"x":str(rightmove + 34), "y":str(ybot-28), "fill":"black", "font-size":"12"})
    LL3mark.text = "2"

    # e**0.1x mark
    emark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 14), "y":str(ybot-36),"fill":"black", "font-size":"16"})
    emark.text = "e"
    exmark = ET.SubElement(doc, 'text', {"x":str(rightmove  + rl.leftmargin + rl.scalewidth + 22), "y":str(ybot-44),"fill":"black", "font-size":"12"})
    exmark.text = "0.1x"


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin + rl.scalewidth

    xpos = m*math.log10(math.log(1.11)) + c
    textstr = "1.11"
    fontsize = 14
    texty = ybot-30
    _text(doc, textstr, xpos, texty, fontsize)

    xpos = c
    textstr = "e"
    fontsize = 14
    texty = ybot-55
    _text(doc, textstr, xpos, texty, fontsize)
    length = 40
    _vertical(doc, length, xpos, ybot, col="black")


    # x from 1.105 to 2.0 in steps of 0.001
    for r in range(1105, 2000):
        textstr = ''
        length = 0
        x = r/1000.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 45
            textstr = str(x)
            fontsize = 16
            texty = ybot-50
        elif r % 50 == 0:
            length = 35
            if r < 1500:
                textstr = str(x)
                fontsize = 14
                texty = ybot-40
        elif r % 10 == 0:
            length = 25
        elif r % 5 == 0 and r<1300:
            length = 20
        elif r < 1140:
            length = 15
        if length:
            _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)

    # x from 2 to 2.7 in steps of 0.01
    for r in range(200, 271):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 10 == 0:
            length = 45
            if r < 240 or r==250:
                textstr = str(x)
                fontsize = 12
                texty = ybot-50
        elif r % 5 == 0:
            length = 35
        if length:
            _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)

    return doc





