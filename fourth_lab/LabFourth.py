def generate_permutations(lst):
    if len(lst) <= 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        current_element = lst[i]
        print("current_element", current_element)
        remaining_elements = lst[:i] + lst[i + 1:]
        print("remaining_elements",remaining_elements)
        permutations_of_remaining = generate_permutations(remaining_elements)
        print("permutations_of_remaining", permutations_of_remaining)
        for perm in permutations_of_remaining:
            result.append([current_element] + perm)
    return result


my_list = [1,2, 3,4,5]
permutations = generate_permutations(my_list)

for perm in permutations:
    print(perm)
