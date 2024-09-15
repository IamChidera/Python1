# Function to manage the phone book
def phone_book_manager(queries):
    phone_book = {}  # Initialize an empty phone book

    result = []  # To store the results of find queries

    for query in queries:
        query_parts = query.split()
        command = query_parts[0]

        if command == "add":
            number, name = int(query_parts[1]), query_parts[2]
            phone_book[number] = name  # Add or overwrite the name associated with the number
        elif command == "del":
            number = int(query_parts[1])
            if number in phone_book:
                del phone_book[number]  # Delete the number if it exists
        elif command == "find":
            number = int(query_parts[1])
            if number in phone_book:
                result.append(phone_book[number])  # Find the name if the number exists
            else:
                result.append("not found")  # Number not found

    return result

# Input
N = int(input())
queries = [input() for _ in range(N)]

# Process the queries and get results
results = phone_book_manager(queries)

# Output the results
for result in results:
    print(result)
