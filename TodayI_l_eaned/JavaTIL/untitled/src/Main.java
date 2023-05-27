class Solution {

    public int solution(int[] array, int height) {
        int[] high_me = array.filter(ele -> ele > height);
        int answer = high_me.length;

        return answer;
    }
    public static void main(String[] args) {
        solution([1,2,3,4,5], 5)
    }
}