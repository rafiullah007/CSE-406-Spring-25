#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    int frame_size, num_pages;

    cout << "Enter number of frames: ";
    cin >> frame_size;

    cout << "Enter number of pages: ";
    cin >> num_pages;

    vector<int> pages(num_pages);
    cout << "Enter page reference string: ";
    for (int i = 0; i < num_pages; i++) {
        cin >> pages[i];
    }

    deque<int> frames;
    int page_faults = 0;

    cout << "\nPage | Frames | Status\n";
    cout << "---------------------\n";

    for (int page : pages) {

        bool found = false;
        for (int frame : frames) {
            if (frame == page) {
                found = true;
                break;
            }
        }

        cout << "  " << page << "  | ";

        if (found) {

            cout << "[ ";
            for (int frame : frames) {
                cout << frame << " ";
            }
            cout << "] | HIT\n";
        } else {

            page_faults++;

            if (frames.size() < frame_size) {

                frames.push_back(page);
            } else {

                frames.pop_front();
                frames.push_back(page);
            }

            cout << "[ ";
            for (int frame : frames) {
                cout << frame << " ";
            }
            cout << "] | MISS\n";
        }
    }

    cout << "\nResults:\n";
    cout << "Page Faults: " << page_faults << endl;
    cout << "Page Hits: " << (num_pages - page_faults) << endl;
    cout << "Hit Rate: " << (double)(num_pages - page_faults) / num_pages * 100 << "%\n";

    return 0;
}
