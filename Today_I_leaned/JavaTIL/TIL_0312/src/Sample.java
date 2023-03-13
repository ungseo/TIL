public class Sample {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        System.out.println(a + b);
        System.out.println(a - b);
        System.out.println(a * b);
        System.out.println(a / b);
        System.out.println(a % b);

        int i = 0;
        int j = 10;
        i++;
        j--;

        System.out.println(i); // i == 1 출력
        System.out.println(j); // j == 9 출력

        int k = 0;
        System.out.println(k++); // 0 출력, k == 1
        System.out.println(k); // k == 1 출력
    }

}
