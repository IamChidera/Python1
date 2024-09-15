def precompute_hashes(p, n, k, x, m):
    hash_table = {}
    hash_val = 0

    for i in range(n):
        hash_val = (hash_val * x + ord(p[i])) % m

    hash_table[hash_val] = [0]

    for i in range(1, len(p) - n + 1):
        hash_val = (hash_val * x - ord(p[i - 1]) * pow(x, n, m) + ord(p[i + n - 1])) % m
        if hash_val < 0:
            hash_val += m

        if hash_val in hash_table:
            hash_table[hash_val].append(i)
        else:
            hash_table[hash_val] = [i]

    return hash_table

def pattern_matching_with_mismatches(k, t, p):
    n = len(p)
    m = 10**9 + 7
    x = 263

    hash_table = precompute_hashes(p, n, k, x, m)

    matches = []

    for i in range(len(t) - n + 1):
        substring = t[i:i + n]
        hash_val = 0

        for j in range(n):
            hash_val = (hash_val * x + ord(substring[j])) % m

        if hash_val in hash_table:
            for j in hash_table[hash_val]:
                mismatches = 0
                for l in range(n):
                    if p[l] != substring[j + l]:
                        mismatches += 1
                        if mismatches > k:
                            break
                if mismatches <= k:
                    matches.append((j, i, n))

    return matches

# Input
k, t, p = input().strip().split()

matches = pattern_matching_with_mismatches(int(k), t, p)

# Output the number of matches and their positions
print(len(matches))
for match in matches:
    print(match[0], match[1])
