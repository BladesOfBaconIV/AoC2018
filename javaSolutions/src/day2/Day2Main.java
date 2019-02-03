package day2;

import helperClasses.inputParser;

import java.util.*;
import java.util.stream.Stream;

public class Day2Main {

    public static void main(String[] args) {
        Stream<String> lines = inputParser.getLines("day2\\input.txt");

        // Part 1
        int checksum = lines.mapToInt(Day2Main::partialChecksum).reduce(1, (x, y) -> x*y);


        System.out.printf("Day 1: %d", checksum);
    }

    public static int partialChecksum(String s) {
        Integer[] freqarray = new Integer[26];
        Arrays.fill(freqarray, 0);
        s = s.toUpperCase();
        for(int i=0;i<s.length();i++)
        {
            freqarray[s.charAt(i)-'A']+=1;
        }
        Set<Integer> frequencies = new HashSet(Arrays.asList(freqarray));
        int checksum = 1;
        for (int n : frequencies) { // Assumes there is never a frequency of 4 or more
            checksum *= n;
        }
        return checksum;
    }
}
