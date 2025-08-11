#include <iostream>
#include <iomanip>
using namespace std;

struct Process {
    string pid;
    int at;
    int bt;
    int priority;
    int ct;
    int tat;
    int wt;
};

void priority_scheduling(Process Ps[], int n) {
    int time = 0;
    bool completed[100] = {false};
    int completedCount = 0;

    while (completedCount < n) {
        int idx = -1;
        int highestPriority = 999999;  

       
        for (int i = 0; i < n; i++) {
            if (!completed[i] && Ps[i].at <= time) {
                if (Ps[i].priority < highestPriority) {
                    highestPriority = Ps[i].priority;
                    idx = i;
                }
                else if (Ps[i].priority == highestPriority) {
                  
                    if (Ps[i].at < Ps[idx].at) {
                        idx = i;
                    }
                }
            }
        }

        if (idx != -1) {
            if (time < Ps[idx].at)
                time = Ps[idx].at;

            time += Ps[idx].bt;
            Ps[idx].ct = time;
            completed[idx] = true;
            completedCount++;
        } else {
          
            time++;
        }
    }
//Naim 150
    for (int i = 0; i < n; i++) {
        Ps[i].tat = Ps[i].ct - Ps[i].at;
        Ps[i].wt = Ps[i].tat - Ps[i].bt;
    }
}

int main() {
    int n;
    cout << "Enter number of processes: ";
    cin >> n;

    Process Ps[100];

    for (int i = 0; i < n; i++) {
        cout << "\nProcess P" << i+1 << ":\n";
        Ps[i].pid = "P" + to_string(i+1);
        cout << "Enter Arrival Time: ";
        cin >> Ps[i].at;
        cout << "Enter Burst Time: ";
        cin >> Ps[i].bt;
        cout << "Enter Priority (Lower number = Higher priority): ";
        cin >> Ps[i].priority;
        Ps[i].ct = Ps[i].tat = Ps[i].wt = 0;
    }

    priority_scheduling(Ps, n);

    cout << "\nPID\tAT\tBT\tPriority\tCT\tTAT\tWT\n";
    for (int i = 0; i < n; i++) {
        cout << Ps[i].pid << "\t"
             << Ps[i].at << "\t"
             << Ps[i].bt << "\t"
             << Ps[i].priority << "\t\t"
             << Ps[i].ct << "\t"
             << Ps[i].tat << "\t"
             << Ps[i].wt << "\n";
    }

    double avg_tat = 0, avg_wt = 0;
    for (int i = 0; i < n; i++) {
        avg_tat += Ps[i].tat;
        avg_wt += Ps[i].wt;
    }
    avg_tat /= n;
    avg_wt /= n;

    cout << fixed << setprecision(2);
    cout << "\nAverage Turnaround Time: " << avg_tat;
    cout << "\nAverage Waiting Time: " << avg_wt << endl;

    return 0;
}
