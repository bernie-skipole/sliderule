
import math

from working import Rule


if __name__ == "__main__":


    rl = Rule(xvalue = math.log(4), right = True, hairline=math.log(64),
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 180)

    # Add a D scale
    rl.addDscale(btmrule=0)

    # Add a C scale
    rl.addCscale(midrule=20)

    # Add a LL3 scale
    rl.addLL3scale(btmrule=70)

    filename = "ll3.svg"

    rl.write(filename)

    print(f'{filename} created')
