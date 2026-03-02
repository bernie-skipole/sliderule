

from working import Rule


if __name__ == "__main__":

    # xvalue is where the C scale index is placed over the D value
    # right is True if the mid scale is moved to the right
    # right is False if the mid scale is moved to the left
    # hairline is where the hairline cursor is placed over the D value, or zero if no hairline is used 

    rl = Rule(xvalue = 1.0, right = True, hairline=0.0,
              topruleheight = 120,
              midruleheight = 0,
              btmruleheight = 0)

    # Add a DF scale
    rl.addDFscale(toprule=20)  # indicates this scale is put on the top rule 20 pixels down from the top

    filename = "df.svg"

    rl.write(filename)

    print(f'{filename} created')
