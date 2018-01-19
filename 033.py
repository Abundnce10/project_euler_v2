"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

def trivialFractionReduction(numerator, denominator):
    "returns array of all possible reduced combos"
    "i.e. 49/94 -> [4, 8] (because the 9 was removed)"
    "i.e. 94/99 -> [4, 9] (because the 9 was removed)"
    "i.e. 45/54 -> [] (because not less than 1)"
    "i.e. 30/50 -> [] (trivial example)"
    "i.e. 87/90 -> [] (no like numbers)"
    results = []

    # check if it's a trivial example
    if numerator % 10 == 0 and denominator % 10 == 0:
        return []

    for num in str(numerator):
        if num in str(denominator):
            # turn 45/54 into 5/5
            n = str(numerator).replace(num, "", 1)
            d = str(denominator).replace(num, "", 1)
            # check if there's a 0 in the num/denom
            if n == "0" or d == "0":
                return []
            # create new fraction with floats
            new_fraction = [float(int(n)), float(int(d))]
            # check if new fraction is less than 1
            if (new_fraction[0] / new_fraction[1]) >= 1:
                return []
            # return new fraction
            return new_fraction
    return []


fractions = []
for i in range(10,100):
    for j in range(i+1,100):
        fractions.append([i,j])

keepers = []
for fraction in fractions:
    reduction = trivialFractionReduction(fraction[0], fraction[1])
    if reduction:
        original_fraction = float(fraction[0]) / float(fraction[1])
        new_fraction = reduction[0] / reduction[1]
        if original_fraction == new_fraction:
            keepers.append(fraction)

# multiply fractions
new_num = 1
new_denom = 1
for keeper in keepers:
    new_num *= keeper[0]
    new_denom *= keeper[1]

# find lowerst common terms
if new_denom % new_num == 0:
    answer = new_denom / new_num
else:
    answer = new_denom


print answer