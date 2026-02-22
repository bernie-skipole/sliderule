
from working import Rule



if __name__ == "__main__":


    rl = Rule(xvalue = 8, right = False, hairline=6,
                   topruleheight = 0,
                   midruleheight = 120,
                   btmruleheight = 240)

    # Add a D scale
    rl.addDscale()

    # Add a C scale
    rl.addCscale()

    # Add a LL3 scale
    rl.addLL3scale()

    filename = "ll3.svg"

    rl.write(filename)

    print(f'{filename} created')
