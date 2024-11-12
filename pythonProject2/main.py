def has_duplicates(path):
    visited = set()
    for x, y in path:
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False

def has_diagonal_crossing(path):
    for i in range(len(path) - 1):
        for j in range(i + 1, len(path)):
            if abs(path[i][0] - path[j][0]) == abs(path[i][1] - path[j][1]):
                return True
    return False

def check_path(path):
    if has_duplicates(path) or has_diagonal_crossing(path):
        return "INVALID"
    return "VALID"

def main(input_file, output_file):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        num_paths = int(fin.readline())
        results = []

        for _ in range(num_paths):
            coordinates = list(map(int, fin.readline().split()))
            path = [(coordinates[i], coordinates[i + 1]) for i in range(0, len(coordinates), 2)]
            result = check_path(path)
            results.append(result)

        fout.write("\n".join(results))
        print("Results written to", output_file)

if __name__ == "__main__":
    input_file = r"C:\Users\Fabi\PycharmProjects\pythonProject2\date.in"
    output_file = r"C:\Users\Fabi\PycharmProjects\pythonProject2\date.out"
    main(input_file, output_file)
