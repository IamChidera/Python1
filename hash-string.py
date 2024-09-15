# Define the hash function and constants
def hash_string(s, m, p, x):
    h = 0
    for i in range(len(s)):
        h = (h * x + ord(s[i])) % p
    return h % m

# Initialize the hash table
def initialize_hash_table(m):
    return [[] for _ in range(m)]

# Add a string to the hash table
def add_string(table, s, m, p, x):
    hash_value = hash_string(s, m, p, x)
    if s not in table[hash_value]:
        table[hash_value].insert(0, s)

# Delete a string from the hash table
def delete_string(table, s, m, p, x):
    hash_value = hash_string(s, m, p, x)
    if s in table[hash_value]:
        table[hash_value].remove(s)

# Find a string in the hash table
def find_string(table, s, m, p, x):
    hash_value = hash_string(s, m, p, x)
    if s in table[hash_value]:
        return "yes"
    else:
        return "no"

# Check the content of a specific chain and return it as a space-separated string
def check_chain(table, i):
    if len(table[i]) == 0:
        return ""
    return " ".join(table[i])

# Main function to process queries
def process_queries(m, queries):
    table = initialize_hash_table(m)
    results = []

    for query in queries:
        command = query[0]

        if command == "add":
            add_string(table, query[1], m, p, x)
        elif command == "del":
            delete_string(table, query[1], m, p, x)
        elif command == "find":
            results.append(find_string(table, query[1], m, p, x))
        elif command == "check":
            chain_index = int(query[1])
            results.append(check_chain(table, chain_index))

    return results

# Input
m = int(input())
n = int(input())
queries = [input().split() for _ in range(n)]

# Constants
p = 10 ** 9 + 7
x = 263

# Process queries and print results
results = process_queries(m, queries)
for result in results:
    print(result)
