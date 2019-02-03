package day1;

import helperClasses.inputParser;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day1Main {

    public static void main(String[] args) {
        final String inputFile = "day1\\input.txt";
        Supplier<IntStream> inputGet = () -> inputParser.getLinesAsInts(inputFile);
        IntStream deltas = inputGet.get();

        // Part 1
        int total = deltas.sum();

        // Part 2
        Set<Integer> seen = new HashSet<>();
        seen.add(0);
        AtomicInteger runningTotal = new AtomicInteger(0);
        int part2Ans = 0;
        while (true) {
            deltas = inputGet.get();
            IntStream frequenies = deltas.sequential().map(runningTotal::addAndGet);
            LinkedHashSet<Integer> duplicates = frequenies.boxed()
                    .filter(n -> !seen.add(n))
                    .collect(Collectors.toCollection(LinkedHashSet::new));
            if (!duplicates.isEmpty()) {
                part2Ans = duplicates.iterator().next();
                break;
            }
        }

        System.out.printf("Part 1: %d\nPart 2: %s", total, part2Ans);

    }
}
