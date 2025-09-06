class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.TAT = 0
        self.wt = 0

def SJF_Non_Preemptive(Ps): 
    Ps.sort(key=lambda x: x.arrival_time)
    n = len(Ps)
    Done_Ps = 0
    current_time = 0
    ready_queue = []

    while Done_Ps < n:  // empty 
        for p in Ps:
            if p.arrival_time <= current_time and p not in ready_queue and p.completion_time == 0:
                ready_queue.append(p)

        ready_queue.sort(key=lambda x: x.burst_time)

        if not ready_queue:
            current_time += 1
            continue

        current_P = ready_queue.pop(0)
        current_time += current_P.burst_time
        current_P.completion_time = current_time
        current_P.TAT = current_P.completion_time - current_P.arrival_time
        current_P.wt = current_P.TAT - current_P.burst_time
        Done_Ps += 1

    total_wt = sum(p.wt for p in Ps)

    print("-----------------------------------------------------------------------")
    print("| Process   | Arrival AT | BurstT | CompTime | TurnATime | WaitingTime|")
    print("-----------------------------------------------------------------------")

    for p in Ps:
        print("| {:<9} | {:<10} | {:<6} | {:<8} | {:<9} | {:<10} |".format(
            f'P{p.pid}',
            p.arrival_time,
            p.burst_time,
            p.completion_time,
            p.TAT,
            p.wt
        ))

    print("-----------------------------------------------------------------------")
    
    print(f"\nAverage Waiting Time   : {total_wt / n:.2f}")

if __name__ == "__main__":
    n = int(input("Enter the number of processes: "))
    Ps = []

    for i in range(n):
        print(f"\nEnter details for Process P{i+1}:")
        at = int(input("Arrival Time: "))
        bt = int(input("Burst Time: "))
        Ps.append(Process(i+1, at, bt))

    SJF_Non_Preemptive(Ps)
