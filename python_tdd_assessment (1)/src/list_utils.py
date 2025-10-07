# src/list_utils.py

# TODO: Implement list filtering helpers
n = [-2, -1, 0, 1, 2]
def filter_even(numbers):
    # TODO: Return only even numbers
    empy_ls = []
    for i in numbers:
        if i%2 == 0:
            empy_ls.append(i)

    return empy_ls

def filter_positive(numbers):
    # TODO: Return only positive numbers
    empy_ls2 = []
    for i in numbers:
        if i > 0:
            empy_ls2.append(i)

    return empy_ls2
# print(filter_even(n))
# print(filter_positive(n))