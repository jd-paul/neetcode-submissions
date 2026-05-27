class DynamicArray {
    private Integer[] array;
    private int capacity = 0;
    private int size;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.array = new Integer[capacity];
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if(size >= capacity) {
            resize();
        }

        array[size] = n;
        size++;
    }

    public int popback() {
        int returnThis = array[size - 1];
        size--;
        return returnThis;
    }

    private void resize() {
        capacity = capacity == 0 ? 1 : capacity * 2; // Handle edge case for capacity 0
        Integer[] newArray = new Integer[capacity];

        for (int i = 0; i < size; i++) {
            newArray[i] = array[i];
        }

        array = newArray;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
