def SSTF(requests, head):
    total_seek = 0
    seek_sequence = []
    requests = requests.copy()  # So we don't change the original list

    while requests:
        # Calculate distance from head to each request
        distances = [abs(r - head) for r in requests]
        # Find index of closest request
        min_index = distances.index(min(distances))
        # Fetch and remove the closest request
        closest_request = requests.pop(min_index)

        # Calculate and add distance moved
        distance = abs(closest_request - head)
        total_seek += distance

        # Move head and add to sequence
        head = closest_request
        seek_sequence.append(closest_request)
#Naim150
    print("\nSeek Sequence:", seek_sequence)
    print("Total Number of Seek Operations:", len(seek_sequence))
    print("Total Seek Distance:", total_seek)


req_input = input("Enter disk request sequence (comma-separated): ")
Req_Seq = [int(x) for x in req_input.strip().split(",")]

head = int(input("Enter initial head position: "))

SSTF(Req_Seq, head)
