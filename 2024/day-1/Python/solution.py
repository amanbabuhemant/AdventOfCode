# Preparing input

input_file = open("input.txt")
left_list = []
right_list = []

for line in input_file.readlines():
    l, r = map(int, line.split("   "))
    left_list.append(l)
    right_list.append(r)

left_list.sort()
right_list.sort()

# Part 1

total_distance = 0

for l, r in zip(left_list, right_list):
    total_distance += abs(l-r)

print(total_distance)

# Part 2

similarity_score = 0

for l in left_list:
    similarity_score += (l*right_list.count(l))

print(similarity_score)
