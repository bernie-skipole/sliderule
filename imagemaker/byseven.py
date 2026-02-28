

from working import Rule


if __name__ == "__main__":

    # xvalue is where the C scale index is placed over the D value
    # right is True if the mid scale is moved to the right
    # right is False if the mid scale is moved to the left
    # hairline is the D value on which the hairline cursor is placed, or zero if no hairline is used 

    rl = Rule(xvalue = 7.0, right = False, hairline=1.4)

    # Add a C scale
    rl.addCscale(100, midrule=20)  # indicates this scale is put on the middle rule 20 pixels down from the top of the middle rule. Rule at least 100 height

    # Add a D scale
    rl.addDscale(120, btmrule=0) # indicates this scale is put on the bottom rule 0 pixels down from the top of the bottom rule. Rule at least 120 height

    filename = "byseven.svg"

    rl.write(filename)

    print(f'{filename} created')
