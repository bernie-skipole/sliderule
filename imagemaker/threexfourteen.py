

from slideruleimages import Rule


if __name__ == "__main__":

    # xvalue is where the C scale index is placed over the D value
    # right is True if the mid scale is moved to the right
    # right is False if the mid scale is moved to the left
    # hairline is where the hairline cursor is placed over the D value, or zero if no hairline is used 

    rl = Rule(xvalue = 4.2/3.0, right = True, hairline=0.0,
              topruleheight = 120,
              midruleheight = 200,
              btmruleheight = 120)

    # Add a DF scale
    rl.addDFscale(toprule=20)  # indicates this scale is put on the top rule 20 pixels down from the top

    # Add a CF scale
    rl.addCFscale(midrule=0)  # indicates this scale is put on the top of the mid rule

    # Add a C scale
    rl.addCscale(midrule=100)  # indicates this scale is put on the mid rule, 100 pixels down

    # Add a D scale
    rl.addDscale(btmrule=0)  # indicates this scale is put on the top of the bottom rule

    filename = "threexfourteen.svg"

    rl.write(filename)

    print(f'{filename} created')
