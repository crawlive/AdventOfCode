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
array1, array2 = read_and_split_file(file_path)

array1.sort()
array2.sort()

distances = []

for i in range(len(array1)):
    distances.append(abs(array1[i]-array2[i]))

totalDistance = sum(distances)
print(totalDistance)