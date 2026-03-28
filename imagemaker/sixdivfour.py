

from slideruleimages import Rule


if __name__ == "__main__":

    # xvalue is where the C scale index is placed over the D value
    # right is True if the mid scale is moved to the right
    # right is False if the mid scale is moved to the left
    # hairline is where the hairline cursor is placed over the D value, or zero if no hairline is used 

    rl = Rule(xvalue = 1.5, right = True, hairline=6.0,
              topruleheight = 0,                               # No top rule
              midruleheight = 120,
              btmruleheight = 120)

    # Add a C scale
    rl.addCscale(midrule=20)  # indicates this scale is put on the middle rule 20 pixels down from the top of the middle rule.

    # Add a D scale
    rl.addDscale(btmrule=0) # indicates this scale is put on the bottom rule 0 pixels down from the top of the bottom rule.

    filename = "sixdivfour.svg"

    rl.write(filename)

    print(f'{filename} created')
