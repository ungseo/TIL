package problemsolving;

public class WhileEx2 {
    public static void main(String[] args) {
        int num = 0;
        while (num != 10) {
            num++;
            System.out.println(2 * num);
        }
        num = 2;
        for (int i = 1; i <= 10; i++) {
            System.out.println(i * num);
        }
    }
}
