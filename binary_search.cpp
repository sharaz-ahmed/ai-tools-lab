#include <iostream>

int binarySearch(const int numbers[], int size, int key) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (numbers[mid] == key) {
            return mid;
        } else if (numbers[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int key = 30;
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int result = binarySearch(numbers, size, key);

    std::cout << "Element found at index: " << result << std::endl;
    return 0;
}
