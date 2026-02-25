
import math

from working import Rule


if __name__ == "__main__":


    rl = Rule(xvalue = math.log(4), right = True, hairline=math.log(64),
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 260)

    # Add a D scale
    rl.addDscale()

    # Add a C scale
    rl.addCscale()

    # Add a LL3 scale
    rl.addLL3scale()

    # Add a LL2 scale
    rl.addLL2scale()

    filename = "ll2.svg"

    rl.write(filename)

    print(f'{filename} created')
