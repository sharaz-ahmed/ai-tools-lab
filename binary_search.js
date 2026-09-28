function binarySearch(numbers, key) {
    let low = 0;
    let high = numbers.length - 1;

    while (low <= high) {
        const mid = Math.floor((low + high) / 2);

        if (numbers[mid] === key) {
            return mid;
        } else if (numbers[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return -1;
}

const numbers = [10, 20, 30, 40, 50];
const key = 30;

const result = binarySearch(numbers, key);

console.log("Element found at index:", result);
