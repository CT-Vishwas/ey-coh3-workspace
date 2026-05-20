inp_str = input("Enter a string: ")

freq_dict = {}
for char in inp_str:
    # if char in freq_dict:
    #     freq_dict[char] += 1
    # else:
    #     freq_dict[char] = 1
    freq_dict[char] = freq_dict.get(char, 0) + 1

print("Character Frequency:")
for char, freq in freq_dict.items():
    print(f"{char}: {freq}")