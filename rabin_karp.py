def rabin_karp(pattern, text):
    p = 31  # A prime number
    m, n = len(pattern), len(text)
    results = []

    # Calculate the hash of the pattern and the first window of the text
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % 10**9 + 7
        window_hash = (window_hash * p + ord(text[i])) % 10**9 + 7

    p_power = p**m  # Precompute p^m for rolling hash

    for i in range(n - m + 1):
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            results.append(i)

        if i + m < n:
            window_hash = (window_hash * p + ord(text[i + m]) - p_power * ord(text[i])) % (10**9 + 7)

    return results

# Input
pattern = input()
text = input()

# Find occurrences and print the results
occurrences = rabin_karp(pattern, text)
print(" ".join(map(str, occurrences)))
