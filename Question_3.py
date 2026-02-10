import string

file_path = "sample-file.txt"

text_file = open(file_path, "r", encoding="utf-8")
lines_list = text_file.readlines()
text_file.close()

group_dict = {}

for index in range(len(lines_list)):
    original = lines_list[index].rstrip("\n")
    normalized = original.lower()

    # remove punctuation
    for p in string.punctuation:
        normalized = normalized.replace(p, "")

    # remove all whitespace
    normalized = normalized.replace(" ", "").replace("\t", "")

    # ignore empty normalized lines
    if normalized == "":
        continue

    if normalized not in group_dict:
        group_dict[normalized] = []

    group_dict[normalized].append((index + 1, original))

# collect near-duplicate sets
duplicate_sets = []

for key in group_dict:
    if len(group_dict[key]) > 1:
        duplicate_sets.append(group_dict[key])

print("Number of near-duplicate sets:", len(duplicate_sets))
print()

# print first two sets
for i in range(min(2, len(duplicate_sets))):
    print("Set", i + 1)
    for line_no, text in duplicate_sets[i]:
        print(f"{line_no}: {text}")
    print()
