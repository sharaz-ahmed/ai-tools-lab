class BinarySearch {
    public static int binarySearch(int[] numbers, int key) {
        int low = 0;
        int high = numbers.length - 1;

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

    public static void main(String[] args) {
        int[] numbers = {10, 20, 30, 40, 50};
        int key = 30;

        int result = binarySearch(numbers, key);

        System.out.println("Element found at index: " + result);
    }
}
