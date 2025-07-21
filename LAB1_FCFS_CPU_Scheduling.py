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

    for p in processes:
        # If the CPU is idle
        if clock < p.arrival_time:
            clock = p.arrival_time

        p.start_time = clock
        p.completion_time = clock + p.burst_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        clock = p.completion_time

    # Print the results
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t{p.turnaround_time}\t{p.waiting_time}")

# Taking user input
n = int(input("Enter number of processes: "))
processes = []

for i in range(n):
    pid = f"P{i}"
    arrival_time = int(input(f"Enter arrival time for process {pid}: "))
    burst_time = int(input(f"Enter burst time for process {pid}: "))
    processes.append(Process(pid, arrival_time, burst_time))

FCFS_Non_Preemptive(processes)
