package day5;

import java.util.ArrayList;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import helperClasses.inputParser;

public class Day5Main {

    public static void main(String[] args) {
        Supplier<IntStream> chars = () -> inputParser.getLineAsChars("day5//input.txt");

        // Part 1
        int part1Ans = reducedLength(chars.get());

        // Part 2
        int shortestLength = 50000;
        for (int i = 97; i < 123; i ++) { // from char a to z inclusive
            Integer I = new Integer(i); // needs to be effectively final for lambda
            int size = reducedLength(chars.get().filter(c -> c!=I && c!=I+32));
            System.out.println(size);
            if (size < shortestLength) {
                shortestLength = size;
            }
        }

        System.out.printf("Part 1: %d\nPart 2: %d", part1Ans, shortestLength);
    }

    public static int reducedLength(IntStream chars) {
        ArrayList<Integer> letters = new ArrayList<>();
        letters.addAll(chars.boxed().collect(Collectors.toList()));
        //System.out.println(letters.size());
        boolean reduced;
        do {
            reduced = false;
            for (int i = 1; i < letters.size(); i++) {
                if (Math.abs(letters.get(i-1)-letters.get(i)) == 32) {
                    letters.remove(i);
                    letters.remove(i-1);
                    reduced = true;
                }
            }
        } while (reduced);

        return letters.size();
    }
}
