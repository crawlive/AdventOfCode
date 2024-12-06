def read_and_split_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    array1 = []
    array2 = []

    for line in lines:
        values = line.strip().split()  # Split the line by whitespace
        if len(values) >= 2:
            array1.append(int(values[0]))
            array2.append(int(values[1]))

    return array1, array2

file_path = './input/day1Input24.txt' 
left, right = read_and_split_file(file_path)

left.sort()
right.sort()

occurrences = []

for num in set(left):
    count = right.count(num)
    occurrences.append(num*count)

sumOccurrences = sum(occurrences)
print(sumOccurrences)