package day2;

import helperClasses.inputParser;

import java.util.*;
import java.util.stream.Stream;

public class Day2Main {

    static int numTwos = 0;
    static int numThrees = 0;

    public static void main(String[] args) {
        Stream<String> lines = inputParser.getLines("day2\\input.txt");

        // Part 1
        lines.forEach(Day2Main::numRepeats);
        int checksum = numTwos * numThrees;

        // Part 2

        System.out.printf("Day 1: %d", checksum);
    }

    // returns 0 for only no 2 or 3 repeats, 2 for a 2 repeats and 3 for 3 repeats,
    // and 5 for 2 and 3 repeats
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
}
