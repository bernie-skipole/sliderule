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




def addLL3scale(rl, rightmove) -> ET.Element:
    "Adds the LL3 scale to the rule, returns the scale element"

    ybot = 0

    doc = ET.Element('g')

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


    # scaling with y = mx+c
    m = rl.scalewidth
    c = rightmove + rl.leftmargin

    # start at x = e
    xpos = c
    length = 35
    textstr = "e"
    fontsize = 18
    texty = ybot-40
    _vertical(doc, length, xpos, ybot, col="black")
    _text(doc, textstr, xpos, texty, fontsize)

    # x from 2.75 to 4.0 in steps of 0.05
    for r in range(275, 400, 5):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 35
            textstr = "3"
            fontsize = 16
            texty = ybot-40
        elif r % 50 == 0:
            length = 25
            textstr = str(x)
            fontsize = 16
            texty = ybot-30
        elif r % 10 == 0:
            length = 20
        else:
            length = 14
        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)
    # x from 4.0 to 10.0 in steps of 0.1
    for r in range(400, 1000):
        textstr = ''
        length = 0
        x = r/100.0
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            length = 35
            textstr = str(int(x))
            fontsize = 16
            texty = ybot-40
        elif r % 50 == 0:
            length = 25
        elif r % 25 == 0 and r > 700:
            length = 20
        elif r % 10 == 0 and r < 700:
            length = 14
        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)
    # x from 10.0 to 100.0 in steps of 1
    for r in range(10, 100):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 10 == 0:
            if r <= 50:
                length = 35
                textstr = str(int(x))
                fontsize = 16
                texty = ybot-40
            else:
                length = 25
        elif r % 5 == 0:
            if r <= 50:
                length = 25
            else:
                length = 20
            if r == 15:
                textstr = "15"
                fontsize = 16
                texty = ybot-30
        elif r < 40:
            length = 14
        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, xpos, texty, fontsize)

    # x from 100 to 1000 in steps of 10
    for r in range(100, 1000, 10):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 100 == 0:
            if r in (100, 200, 500):
                length = 35
                textstr = str(r)
                fontsize = 16
                texty = ybot-40
                textpos = xpos-10
            else:
                length = 25
        elif r % 50 == 0:
            length = 20
        elif r < 200:
            length = 14

        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, textpos, texty, fontsize)

    # x from 1000 to 5000 in steps of 100
    for r in range(1000, 5000, 100):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 1000 == 0:
            if r in (1000, 2000, 3000):
                length = 35
                fontsize = 16
                texty = ybot-40
                textpos = xpos
                if r == 1000:
                    textstr = '1k'
                elif r == 2000:
                    textstr = '2k'
                else:
                    textstr = '3k'
            else:
                length = 25
        elif r % 500 == 0:
            length = 20
        elif r < 2000:
            length = 14

        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, textpos, texty, fontsize)

    # x from 5000 to 20000 in steps of 1000
    for r in range(5000, 20001, 1000):
        textstr = ''
        length = 0
        x = float(r)
        xpos = m*math.log10(math.log(x)) + c
        if r % 5000 == 0:
            if r == 15000:
                length = 20
            elif r in (5000, 10000, 20000):
                length = 35
                fontsize = 16
                texty = ybot-40
                if r == 5000:
                    textpos = xpos
                else:
                    textpos = xpos-10
                textstr = f'{int(r/1000)}k'
        else:
            length = 14
        if length:
            vline = _vertical(doc, length, xpos, ybot, col="black")
        if textstr:
            _text(doc, textstr, textpos, texty, fontsize)







    return doc





