def merge_dicts_with_duplicates(*dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                # Қайталанатын мәндерді жалқаулау
                if isinstance(merged_dict[key], list):
                    merged_dict[key].append(value)
                else:
                    merged_dict[key] = [merged_dict[key], value]
            else:
                merged_dict[key] = value
    return merged_dict

# Проверка
dict1 = {'а': 1, 'б': 2, 'в': 3}
dict2 = {'б': 4, 'в': 5, 'г': 6}
dict3 = {'а': 7, 'в': 8, 'д': 9}
dict4 = {'а': 10, 'в': 12, 'c': 13}
merged = merge_dicts_with_duplicates(dict1, dict2, dict3,dict4)
print(merged)
