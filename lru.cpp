#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class LRU {
    int capacity;                         // Maximum number of pages that can be in memory
    list<int> order;                      // Keeps pages in LRU order (front = least recent)
    unordered_map<int, list<int>::iterator> cache; // Maps page number to its position in the list

public:
    LRU(int cap) {
        capacity = cap;
    }

    void refer(int page) {
        // If page not present
        if (cache.find(page) == cache.end()) {
            // If cache is full, remove least recently used page
            if (order.size() == capacity) {
                int lru_page = order.front();    // Get LRU page
                order.pop_front();               // Remove it from list
                cache.erase(lru_page);           // Remove from map
            }
        } 
        else {
            // If page already exists, remove it to update its position
            order.erase(cache[page]);
        }

        // Add the current page to the back (most recently used)
        order.push_back(page);
        cache[page] = --order.end(); // Update iterator in map
    }

    void display() {
        cout << "Current Pages in Memory (LRU): ";
        for (int p : order)
            cout << p << " ";
        cout << endl;
    }
};

int main() {
    int capacity, n;

    cout << "Enter cache capacity: ";
    cin >> capacity;

    cout << "Enter number of pages: ";
    cin >> n;

    int pages[n];
    cout << "Enter " << n << " page numbers: ";
    for (int i = 0; i < n; i++)
        cin >> pages[i];

    LRU lru(capacity);
    cout << "\nLRU Page Replacement Simulation:\n";

    for (int i = 0; i < n; i++) {
        cout << "\nRefer page: " << pages[i] << endl;
        lru.refer(pages[i]);
        lru.display();
    }

    return 0;
}