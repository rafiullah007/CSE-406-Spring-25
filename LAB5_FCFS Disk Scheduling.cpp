#include <iostream>
#include <cmath>

using namespace std;

int main() {

    int request[] = {0, 16, 24, 43, 50, 82, 100, 140, 150, 170, 190, 199};
    int n = sizeof(request) / sizeof(request[0]);
    int initial_head = 50;
    int total_head_movement = 0;


    int current_position = initial_head;


    cout << "Request sequence: ";
    for(int i = 0; i < n; i++) {
        cout << request[i] << " ";
    }
    cout << endl;


    for(int i = 0; i < n; i++) {

        total_head_movement += abs(current_position - request[i]);


        current_position = request[i];
    }


    cout << "Total head movement: " << total_head_movement << endl;

    return 0;
}
