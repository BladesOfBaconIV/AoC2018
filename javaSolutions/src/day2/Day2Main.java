package day2;

import helperClasses.inputParser;

import java.util.*;
import java.util.function.Supplier;
import java.util.stream.Stream;

public class Day2Main {

    static int numTwos = 0;
    static int numThrees = 0;

    public static void main(String[] args) {
        Supplier<Stream<String>> lines = () -> inputParser.getLines("day2\\input.txt");

        // Part 1
        lines.get().forEach(Day2Main::numRepeats);
        int checksum = numTwos * numThrees;

        // Part 2
        String mostSimilar = "";
        boolean found = false;
        for (String a : lines.get().toArray(String[]::new)) {
            for (String b : lines.get().filter(s -> !s.equals(a)).toArray(String[]::new)) {
                if (differences(a, b) == 1) {
                    char[] a_arr = a.toCharArray();
                    char[] b_arr = b.toCharArray();
                    for (int i = 0; i < a.length(); i++) {
                        if (a_arr[i] == b_arr[i]) {
                            mostSimilar += a_arr[i];
                        }
                    }
                    found = true;
                    break;
                }
            }
            if (found) {
                break;
            }
        }
        System.out.printf("Part 1: %d\nPart 2: %s", checksum, mostSimilar);
    }

    public static void numRepeats(String s) {
        Integer[] freqarray = new Integer[26];
        Arrays.fill(freqarray, 0);
        s = s.toUpperCase();
        for(int i=0;i<s.length();i++)
        {
            freqarray[s.charAt(i)-'A']+=1;
        }
        Set<Integer> frequencies = new HashSet(Arrays.asList(freqarray));
        for ( int n : frequencies) {
            if (n == 2) {
                numTwos++;
            }
            if (n == 3) {
                numThrees++;
            }
        }
    }

    // returns the number of differences between a and b
    public static int differences(String a, String b) {
        char[] a_arr = a.toCharArray();
        char[] b_arr = b.toCharArray();
        int diffs = 0;
        for (int i = 0; i < a_arr.length; i++){
            if (a_arr[i] != b_arr[i]) {
                diffs++;
            }
        }
        return diffs;
    }
}
