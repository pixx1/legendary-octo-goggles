freq_sum = 0
with open("frequency", "r") as freq:
    for single_line in freq:
        freq_sum += int(single_line)
print(freq_sum)
