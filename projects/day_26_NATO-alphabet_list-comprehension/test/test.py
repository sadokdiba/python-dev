
with open("./file1.txt", "r") as file1:
    file1_list = [int(line.strip()) for line in file1.readlines()]

with open("./file2.txt", "r") as file2:
    file2_list = [int(line.strip()) for line in file2.readlines()]

result = [common for common in file1_list if common in file2_list]

print(result)


