
import math

from working import Rule


if __name__ == "__main__":

    # place C10 and hairline on LL02 root of six

    # index on LL02 root of six
    # e**0.1x = math.sqrt(6)
    # 0.1x = math.log(math.sqrt(6))

    x = 10*math.log(math.sqrt(6))
    rl = Rule(xvalue = x, right = False, hairline=x,
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 270)

    # Add a D scale
    rl.addDscale(btmrule=0)

    # Add a C scale
    rl.addCscale(midrule=20)

    # Add a LL3 scale
    rl.addLL3scale(btmrule=70)

    # Add a LL2 scale
    rl.addLL2scale(btmrule=160)

    filename = "ll2.svg"

    rl.write(filename)

    print(f'{filename} created')
