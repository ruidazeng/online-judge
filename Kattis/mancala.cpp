#include <iostream>
#include <vector>

int main() {
    // Get number of cases
    int kases;
    std::cin >> kases;

    while(kases--) {
        // Take in input
        int c;
        std::cin >> c;
        int beads;
        std::cin >> beads;

        // Reverse engineer board
        std::vector<int> board(1000, 0);
        int j = 0;
        while(beads--) {
            for(int i = 1; i <= board.size(); i++) {
                j = std::max(i, j);
                if(board[i] == 0) {
                    board[i] = i;
                    break;
                }
                else {
                    board[i]--;
                }
            }
        }

        // Print board
        std::cout << c << " " << j << std::endl;
        for(int i = 1; i <= j; i++) {
            std::cout << board[i] << " ";
            if(i % 10 == 0 && i != j) {
                std::cout << std::endl;
            }
        }
        std::cout << std::endl;
    }
}