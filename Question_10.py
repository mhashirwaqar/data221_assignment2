def find_lines_containing(filename, keyword):
    results = []

    with open(filename, "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                results.append((idx, line.strip()))

    return results


file_path = "sample-file.txt"

matches = find_lines_containing(file_path, "data")

print("Number of matching lines:", len(matches))

for line_num, text in matches[:3]:
    print(f"{line_num}: {text}")
