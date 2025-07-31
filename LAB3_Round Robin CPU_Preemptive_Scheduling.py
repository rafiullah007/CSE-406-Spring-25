#include <iostream>
#include <queue>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

struct P {
    string pid;
    int AT;
    int BT;
    int remaining;
    int CT;
    int WT;
    int turnaround;
};

int main() {
    int n, timeQuantum;
    cout << "Enter number of processes: ";
    cin >> n;

    vector<P> Ps(n);

    cout << "Enter Process ID (string), Arrival Time and Burst Time for each process:\n";
    for (int i = 0; i < n; i++) {
        cin >> Ps[i].pid >> Ps[i].AT >> Ps[i].BT;
        Ps[i].remaining = Ps[i].BT;
        Ps[i].CT = 0;
        Ps[i].WT = 0;
        Ps[i].turnaround = 0;
    }

    cout << "Enter Time Quantum: ";
    cin >> timeQuantum;

    sort(Ps.begin(), Ps.end(), [](P &a, P &b) {
        return a.AT < b.AT;
    });
//MD.Rafiullah Al Naim
    queue<int> q;
    vector<bool> inQueue(n, false);
    int currentTime = 0;
    int completed = 0;

    for (int i = 0; i < n; i++) {
        if (Ps[i].AT <= currentTime) {
            q.push(i);
            inQueue[i] = true;
        }
    }

    while (completed < n) {
        if (q.empty()) {
            for (int i = 0; i < n; i++) {
                if (!inQueue[i] && Ps[i].remaining > 0) {
                    currentTime = Ps[i].AT;
                    q.push(i);
                    inQueue[i] = true;
                    break;
                }
            }
        }

        int i = q.front();
        q.pop();

        if (Ps[i].remaining > timeQuantum) {
            Ps[i].remaining -= timeQuantum;
            currentTime += timeQuantum;
        } else {
            currentTime += Ps[i].remaining;
            Ps[i].remaining = 0;
            completed++;
            Ps[i].CT = currentTime;
            Ps[i].turnaround = Ps[i].CT - Ps[i].AT;
            Ps[i].WT = Ps[i].turnaround - Ps[i].BT;
        }

        for (int j = 0; j < n; j++) {
            if (!inQueue[j] && Ps[j].AT <= currentTime && Ps[j].remaining > 0) {
                q.push(j);
                inQueue[j] = true;
            }
        }

        if (Ps[i].remaining > 0) {
            q.push(i);
        }
    }

    cout << "\n-------------------------------------------------------------\n";
    cout << "| Process |  AT  |  BT  |  CT  |  TAT  |  WT   |\n";
    cout << "-------------------------------------------------------------\n";

    double totalWT = 0.0;
    for (const auto& p : Ps) {
        cout << " | " << setw(7) << left << p.pid
             << " | " << setw(5) << right << p.AT
             << " | " << setw(5) << right << p.BT
             << " | " << setw(5) << right << p.CT
             << " | " << setw(6) << right << p.turnaround
             << " | " << setw(6) << right << p.WT
             << " |\n";
        totalWT += p.WT;
    }
    cout << "-------------------------------------------------------------\n";

    double avgWT = totalWT / n;
    cout << fixed << setprecision(2);
    cout << "Average Waiting Time: " << avgWT << " units\n";

    return 0;
}
