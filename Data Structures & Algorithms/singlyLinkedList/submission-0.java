class Node {
    int val;
    public Node next = null;

    public Node(int val) {
        this.val = val;
    }
}

class LinkedList {
    Node head = null;
    Node tail = null;
    int size = 0;

    public LinkedList() {}

    public int get(int index) {
        if (index < 0 || index >= size) { return -1; }

        Node returnNode = head;

        for (int i = 0; i < index; i++) {
            returnNode = returnNode.next;
        }

        return returnNode.val;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = head;
        
        if (head == null) {
            tail = newNode;   
        }
        head = newNode;

        size++;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        newNode.next = null;

        if (tail == null) {
            tail = newNode;
            head = newNode;
        }
        else {
            tail.next = newNode;
            tail = newNode;
        }

        tail.next = null;
        size++;
    }

    public boolean remove(int index) {
        if (head == null || index < 0 || index >= size) { return false; };
        if (index == 0) {
            head = head.next;
            size--;
            return true;
        }
        
        Node currentNode = head;

        Node previousNode = null;
        for (int i = 0; i < index; i++) {
            previousNode = currentNode;
            currentNode = currentNode.next;
        }
        previousNode.next = currentNode.next;

        size--;

        if (currentNode.next == null) {
            tail = previousNode;
        }
        if (head == null) tail = null;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> returnThis = new ArrayList<>();
        Node currentNode = head;

        for (int i = 0; i < size; i++) {
            returnThis.add(currentNode.val);
            currentNode = currentNode.next;
        }

        return returnThis;
    }
}
