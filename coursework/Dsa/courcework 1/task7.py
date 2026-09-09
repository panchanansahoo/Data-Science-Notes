from bisect import bisect_left


def successfulPairs(spells, potions, success):

    potions.sort()

    result = []

    for spell in spells:

        required = (success + spell - 1) // spell

        index = bisect_left(potions, required)

        result.append(len(potions) - index)

    return result


spells = list(map(int, input("Enter spells: ").replace(",", " ").split()))
potions = list(map(int, input("Enter potions: ").replace(",", " ").split()))
success = int(input("Enter success: "))

print("Successful pairs:", successfulPairs(spells, potions, success))
