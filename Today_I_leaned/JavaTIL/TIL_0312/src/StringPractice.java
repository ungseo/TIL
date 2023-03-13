public class StringPractice {
    public static void main(String[] args) {
        String a = "Happy Java";
        String b = "a";
        String c = "123";

        //equals 내장함수 연습

        String a1 = "hello";
        String b1 = "java";
        String c1 = "hello";
        System.out.println(a1.equals(c1));
        System.out.println(a1.equals(b1));

        // indexOf 내장함수 연습

        String a2 = "Hello Java";
        System.out.println(a2.indexOf("Java"));

        // contains 내장함수 연습

        String a3 = "Hello Java";
        System.out.println(a3.contains("Java")); // a3에 "Java"가 있니? == true


    }
}
