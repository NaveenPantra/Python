// Java Code

import java.util.*;

public class Main{

     public static void main(String []args) {

        Set<String> s = new HashSet<String>();
        String str = "abcde";
        long count = 0;
        for (int i = 0; i < str.length(); i++) {
            String sub = str.substring(i);
            for (int j = 0; j < sub.length(); j++) {
                String subStr = sub.substring(0, sub.length() - j);
                if (s.contains(subStr)) {
                    continue;
                }
                count++;
                s.add(subStr);
            }
        }
        System.out.println(s);
        System.out.println(count);

     }
}