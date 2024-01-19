import java.util.*;

public class Generics {
    public static void main(String[] args) {
        // without generics
        List list = new LinkedList();
        list.add(new Integer(1));
        list.add('a'); // without specifying generics, it can store any Object.
        Integer i = (Integer) list.iterator().next(); // need explicit type conversion, cuz the compiler does not know
                                                      // that the list stores integers. The list can store any Object.

        // with generics
        List<Integer> list2 = new LinkedList<>();
        list2.add(new Integer(1));
        // list2.add('b'); // this triggers error because now list2 can only store
        // Integer.
        Integer i2 = list2.iterator().next(); // needn't explicit type conversion

        fromArrayToList(3);
    }

    // an example generics method (type parameters are right before the return type)
    public static <T, K, E, B> void fromArrayToList(int a) {
        System.out.println("haha");
    }
}
