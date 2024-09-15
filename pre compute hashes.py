def precompute_hashes(s, m1, m2, x):
    n = len(s)
    h1 = [0] * (n + 1)
    h2 = [0] * (n + 1)
    x1 = [1] * (n + 1)
    x2 = [1] * (n + 1)

    for i in range(1, n + 1):
        x1[i] = (x1[i - 1] * x) % m1
        x2[i] = (x2[i - 1] * x) % m2

    for i in range(1, n + 1):
        h1[i] = (x * h1[i - 1] + ord(s[i - 1])) % m1
        h2[i] = (x * h2[i - 1] + ord(s[i - 1])) % m2

    return h1, h2, x1, x2

def are_substrings_equal(s, a, b, l, h1, h2, x1, x2, m1, m2):
    h1_a_l = (h1[a + l] - x1[l] * h1[a]) % m1
    h2_a_l = (h2[a + l] - x2[l] * h2[a]) % m2
    h1_b_l = (h1[b + l] - x1[l] * h1[b]) % m1
    h2_b_l = (h2[b + l] - x2[l] * h2[b]) % m2

    return h1_a_l == h1_b_l and h2_a_l == h2_b_l

# Input
s = input().strip()
q = int(input())

# Constants
m1 = 10**9 + 7
m2 = 10**9 + 9
x = 263

# Precompute hashes
h1, h2, x1, x2 = precompute_hashes(s, m1, m2, x)

# Process queries
for _ in range(q):
    a, b, l = map(int, input().split())
    if are_substrings_equal(s, a, b, l, h1, h2, x1, x2, m1, m2):
        print("Yes")
    else:
        print("No")
