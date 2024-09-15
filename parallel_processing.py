import heapq

def assign_jobs(n, m, times):
    # Create a list of threads with their indices and next available time
    threads = [(i, 0) for i in range(n)]
    
    # Initialize a result list to store the assignment information
    assignment = []
    
    # Iterate through the jobs
    for job in times:
        # Get the thread with the earliest available time
        thread = heapq.heappop(threads)
        
        # Assign the job to the thread and update its available time
        thread_index, thread_time = thread
        assignment.append((thread_index, thread_time))
        
        # Update the thread's next available time
        heapq.heappush(threads, (thread_index, thread_time + job))
    
    return assignment

# Read input
n, m = map(int, input().split())
times = list(map(int, input().split()))

# Assign jobs to threads
assignment = assign_jobs(n, m, times)

# Print the assignment
for thread_index, start_time in assignment:
    print(thread_index, start_time)
