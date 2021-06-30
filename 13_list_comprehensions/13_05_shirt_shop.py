'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cartesian_product_list = [size + ', ' + color for size in sizes for color in colors]
print(cartesian_product_list)


# combinations_list = []
# for color in colors:
#     for size in sizes:
#         pair_together = color + ', ' + size
#         combinations_list.append(pair_together)
# print(combinations_list)
