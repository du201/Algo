import java.util.*;

public class ComparatorExample {

    public static void main(String[] args) {
        List<Player> footballTeam = new ArrayList<>();
        Player player1 = new Player(59, "John", 24);
        Player player2 = new Player(67, "Roger", 22);
        Player player3 = new Player(45, "Steven", 20);
        footballTeam.add(player1);
        footballTeam.add(player2);
        footballTeam.add(player3);

        PlayerAgeComparator compAge = new PlayerAgeComparator();
        PlayerRankingComparator compRanking = new PlayerRankingComparator();

        System.out.println("Before Sorting : " + footballTeam);

        // using comparator gives us the flexibility of choosing different ordering
        // strategy during runtime. Comparable simply cannot achive this because
        // comparable is directly related to the class itself.
        if (false) {
            Collections.sort(footballTeam, compAge);
        } else {
            Collections.sort(footballTeam, compRanking);
        }

        System.out.println("After Sorting : " + footballTeam);
    }
}

class PlayerAgeComparator implements Comparator<Player> {

    @Override
    public int compare(Player firstPlayer, Player secondPlayer) {
        return Integer.compare(firstPlayer.age, secondPlayer.age);
    }

}

class PlayerRankingComparator implements Comparator<Player> {

    @Override
    public int compare(Player firstPlayer, Player secondPlayer) {
        return Integer.compare(firstPlayer.ranking, secondPlayer.ranking);
    }

}

class Player {
    int ranking;
    String name;
    int age;

    // constructor, getters, setters
    public Player(int ranking, String name, int age) {
        this.ranking = ranking;
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "age: " + age + ". ranking: " + ranking;
    }
}
