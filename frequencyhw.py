def count_frequency_get(data):
    frequency = {}
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

my_string = "hello world"
frequencies = count_frequency_get(my_string)
print(f"Frequencies (get): {frequencies}")