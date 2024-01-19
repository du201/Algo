import java.util.HashMap;

public class HashTable {
    public static void main(String[] args) {
        HashMap<String, String> capitalCities = new HashMap<String, String>();
        capitalCities.put("England", "London");
        capitalCities.put("Germany", "Berlin");
        capitalCities.put("Norway", "Oslo");
        capitalCities.put("USA", "Washington DC");
        System.out.println(capitalCities.size());

        // Print keys
        for (String i : capitalCities.keySet()) {
            System.out.println(i);
        }

        // Print values
        for (String i : capitalCities.values()) {
            System.out.println(i);
        }
        System.out.println(capitalCities.containsKey("England"));
        System.out.println(capitalCities.get("England"));
        capitalCities.remove("England");
        System.out.println(capitalCities.containsKey("England"));

        HashMap<Location, Integer> locIslandSizeMap = new HashMap<>();
        locIslandSizeMap.put(new Location(2, 3), 4);
        System.out.println(locIslandSizeMap.containsKey(new Location(2, 3)));
    }
}

class Location {
    int x;
    int y;

    public Location(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
