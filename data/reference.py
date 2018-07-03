from .ENUMS import *

total = 0
pool = list()

for x in range(0, len(test_candy)):
    for y in range(0, len(test_color)):
        for z in range(0, len(test_variant)):
            for a in range(0, len(test_texture)):
                for b in range(0, len(test_conditionning)):
                    total += 1
                    pool.append("Ref #{} - Candy: {}, Color: {}, Variant: {}, Texture: {}, Conditionning: {}".format(
                        total, test_candy[x], test_color[y], test_variant[z],
                        test_texture[a], test_conditionning[b]))

for line in pool:
    print(line)
