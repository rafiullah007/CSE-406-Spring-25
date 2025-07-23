n = int(input("Enter number of processes : "))
d = dict()

for i in range(n):
    key = "P" + str(i + 1)
    a = int(input("Enter arrival time of process " + str(i + 1) + ": "))
    b = int(input("Enter burst time of process " + str(i + 1) + ": "))
    d[key] = [a, b]

PS_sort = sorted(d.items(), key=lambda item: item[1][0])

CT = []
for i in range(len(PS_sort)):
    if i == 0:
        CT.append(PS_sort[i][1][1])
    else:
        CT.append(max(CT[i - 1], PS_sort[i][1][0]) + PS_sort[i][1][1])

TAT = []
for i in range(len(PS_sort)):
    TAT.append(CT[i] - PS_sort[i][1][0])

WT = []
for i in range(len(PS_sort)):
    WT.append(TAT[i] - PS_sort[i][1][1])

avg_WT = sum(WT) / n


print("\n-----------------------------------------------------------------------")
print("| Process   | Arrival AT | BurstT | CompTime | TurnATime | WaitingTime|")
print("\n-----------------------------------------------------------------------")

for i in range(n):
    print("| {:<9} | {:<10} | {:<6} | {:<8} | {:<9} | {:<10} |".format(
        PS_sort[i][0],
        PS_sort[i][1][0],
        PS_sort[i][1][1],
        CT[i],
        TAT[i],
        WT[i]
    ))

print("\n-----------------------------------------------------------------------")
print("\nAverage Waiting Time: {:.2f}".format(avg_WT))

print("By -")
print("Name : MD. Raafiullah Al Naim")
print("ID : 22101150")

