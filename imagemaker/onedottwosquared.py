
import math

from slideruleimages import Rule


if __name__ == "__main__":


    # getting 1.2 squared

    rl = Rule(xvalue = 10*math.log(1.2), right = True, hairline=10*math.log(1.44),
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 180)

    # Add a D scale
    rl.addDscale(btmrule=0)

    # Add a C scale
    rl.addCscale(midrule=20)

    # Add a LL2 scale
    rl.addLL2scale(btmrule=70)

    filename = "onedottwosquared.svg"

    rl.write(filename)

    print(f'{filename} created')
