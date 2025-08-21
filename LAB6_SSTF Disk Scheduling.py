def SSTF(requests, head):
    total_seek = 0
    seek_sequence = []
    requests = requests.copy()  

    while requests:
        distances = [abs(r - head) for r in requests]
        min_index = distances.index(min(distances))
        closest_request = requests.pop(min_index)
        distance = abs(closest_request - head)
        total_seek += distance
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
