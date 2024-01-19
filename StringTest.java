public class StringTest {
    public static void main(String[] args) {
        String Str1 = new String("Welcome to Tutorialspoint.com");
        String Str2 = new String("Tutorials");

        System.out.print("String Length :");
        System.out.println(Str1.length());

        System.out.print("String Length :");
        System.out.println(Str2.length());

        String txt = "Hello World";
        System.out.println(txt.toUpperCase()); // Outputs "HELLO WORLD"
        System.out.println(txt.toLowerCase()); // Outputs "hello world"

        String txt2 = "Please locate where 'locate' occurs!";
        System.out.println(txt2.indexOf("locate")); // Outputs 7
        System.out.println(txt2.indexOf('a'));

        String firstName = "John";
        String lastName = "Doe";
        System.out.println(firstName + " " + lastName);

        System.out.println(firstName.charAt(2));

        char[] ch = firstName.toCharArray();

        // Traverse the character array
        for (int i = 0; i < ch.length; i++) {

            // Print current character
            System.out.print(ch[i] + " ");
        }

        for (int i = 0; i < firstName.length(); i++) {
            System.out.print(firstName.charAt(i));
        }
    }
}
