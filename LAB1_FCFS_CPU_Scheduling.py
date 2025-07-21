class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def FCFS_Non_Preemptive(processes):
    # Sort by arrival time
    processes.sort(key=lambda p: p.arrival_time)

    clock = 0

    total_tat = 0  # Total Turnaround Time
    total_wt = 0   # Total Waiting Time

    for p in processes:
        # If the CPU is idle
        if clock < p.arrival_time:
            clock = p.arrival_time

        p.start_time = clock
        p.completion_time = clock + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        clock = p.completion_time

        total_tat += p.turnaround_time
        total_wt += p.waiting_time

    # Print the results
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}")

    avg_tat = total_tat / len(processes)
    avg_wt = total_wt / len(processes)

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

# Taking user input
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    pid = f"P{i}"
    arrival_time = int(input(f"Enter arrival time for process {pid}: "))
    burst_time = int(input(f"Enter burst time for process {pid}: "))
    processes.append(Process(pid, arrival_time, burst_time))

FCFS_Non_Preemptive(processes)
