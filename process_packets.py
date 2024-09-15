from collections import deque

def process_packets(S, n, packets):
    buffer = deque()
    current_time = 0
    result = []

    for packet in packets:
        arrival_time, processing_time = packet

        # Clear the buffer from packets that have finished processing
        while buffer and buffer[0] <= arrival_time:
            buffer.popleft()

        if len(buffer) < S:
            # The buffer is not full, so process the packet
            start_time = max(current_time, arrival_time)
            result.append(start_time)
            current_time = start_time + processing_time
            buffer.append(current_time)
        else:
            # The buffer is full, drop the packet
            result.append(-1)

    return result

# Input
S, n = map(int, input().split())
packets = [list(map(int, input().split())) for _ in range(n)]

# Process the packets and print the results
results = process_packets(S, n, packets)
for result in results:
    print(result)
