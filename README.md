# Algo
Small tips:
1. How to use a Python Dictionary as a Key of another Python dictionary
https://stackoverflow.com/a/1600806
frozenset(my_dict.items()) is the best solution. Compared to tuple(sorted(my_dict.items())), using frozenset doesn't require us to sort the dictionary. The reason we use frozenset instead of set is that frozenset is immutable.
2. small infinity in python is: float("-inf")
3. big infinity in python is: float('inf')