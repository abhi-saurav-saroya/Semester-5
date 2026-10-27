import java.util.LinkedList;

public class DoublyLinkedList {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();

        // Insert elements
        list.add("Apple");
        list.add("Banana");
        list.add("Mango");
        list.addFirst("Orange");
        list.addLast("Grapes");

        System.out.println("Original List: " + list);

        // Insert at a specific index
        list.add(2, "Pineapple");
        System.out.println("After insertion: " + list);

        // Display first and last elements
        System.out.println("First Element: " + list.getFirst());
        System.out.println("Last Element: " + list.getLast());

        // Display in reverse order
        System.out.println("Reverse List: " + list.reversed());

        // Delete an element by value
        list.remove("Banana");
        System.out.println("After removing Banana: " + list);

        // Delete an element by index
        list.remove(2);
        System.out.println("After removing index 2: " + list);

        // Delete first and last elements
        list.removeFirst();
        list.removeLast();
        System.out.println("After removing first and last: " + list);

        // Check whether an element exists
        System.out.println("Contains Mango? " + list.contains("Mango"));

        // Display size
        System.out.println("Size: " + list.size());

        // Traverse the list
        System.out.println("Traversing the list:");
        for (String fruit : list) {
            System.out.println(fruit);
        }
    }
}