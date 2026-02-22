
from working import make_rule



if __name__ == "__main__":


    rl = make_rule(xvalue = 8, right = False, hairline=6,
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 240)

    # Add a dscale
    rl.addDscale()

    # Add a cscale
    rl.addCscale()

    # Add a cscale
    rl.addLL3scale()

    filename = "ll3.svg"

    rl.write(filename)

    print(f'{filename} created')
