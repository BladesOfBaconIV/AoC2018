package day4;

import helperClasses.inputParser;
import jdk.internal.dynalink.linker.ConversionComparator;

import java.util.*;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day4Main {

    public static ArrayList<Guard> guards = new ArrayList<Guard>();
    public static Guard currentGuard;
    public static int sleepStartTime;
    public static final Pattern guardID = Pattern.compile("(?<=#)\\d+");
    public static final Pattern minute = Pattern.compile("(?<=:)\\d+");

    public static void main(String[] args) {
        Supplier<Stream<String>> lines = () -> inputParser.getLines("day4//input.txt");

        lines.get().sorted().forEach(Day4Main::updateGuardList);

        // Part 1
        guards.sort((g1, g2) ->
                        String.valueOf(g1.getTimesAsleep().size())
                            .compareTo(String.valueOf(g2.getTimesAsleep().size())));
        Collections.reverse(guards); // Change to descending order
        Guard sleepiestGuard = guards.get(0);
        int sleepiestMinute = sleepiestGuard.getTimesAsleep()
                .stream()
                .collect(Collectors.groupingBy(m -> m, Collectors.counting()))
                .entrySet()
                .stream()
                .max((m1, m2) -> m1.getValue().compareTo(m2.getValue()))
                .orElseGet(null).getKey();
        int part1Ans = sleepiestMinute * sleepiestGuard.id;

        // Part 2
        Map<Integer, Map.Entry<Integer, Long>> idMinuteFreqMap = new HashMap<>();
        for (Guard g: guards) {
            if (g.getTimesAsleep().size() > 0) {
                idMinuteFreqMap.put(g.getID(), g.getTimesAsleep()
                        .stream()
                        .collect(Collectors.groupingBy(m -> m, Collectors.counting()))
                        .entrySet()
                        .stream()
                        .max((m1, m2) -> m1.getValue().compareTo(m2.getValue()))
                        .orElseGet(null));
            }
        }
        int mostRegularSleeper = idMinuteFreqMap
                .entrySet()
                .stream()
                .max((e1, e2) -> e1.getValue().getValue().compareTo(e2.getValue().getValue()))
                .orElseGet(null).getKey();
        int mostFreqMinute = idMinuteFreqMap.get(mostRegularSleeper).getKey();
        int part2Ans = mostRegularSleeper * mostFreqMinute;

        System.out.printf("Part 1: %d\nPart 2: %d", part1Ans, part2Ans);
    }

    public static void updateGuardList(String s) {
        Matcher matches;
        if (s.contains("#")) { // if a guard swap line
            matches = guardID.matcher(s);
            matches.find();
            int id = Integer.parseInt(matches.group());
            Guard testGuard = new Guard(id);
            if (guards.contains(testGuard)) { // if guard already exists set current guard
                for (Guard g: guards) {
                    if (g.equals(testGuard)) {
                        currentGuard = g;
                    }
                }
            }
            else { // else add guard and set current guard
                guards.add(testGuard);
                currentGuard = testGuard;
            }
        }
        else if (s.contains("falls")) { // else if a guard falls asleep set start time
            matches = minute.matcher(s);
            matches.find();
            sleepStartTime = Integer.parseInt(matches.group(0));
        }
        else if (s.contains("wakes")){ // guard must be waking up
            matches = minute.matcher(s);
            matches.find();
            int sleepEndTime = Integer.parseInt(matches.group(0));
            int[] sleepTimes = new int[sleepEndTime - sleepStartTime];
            for (int i = 0; i < sleepTimes.length; i++) {
                sleepTimes[i] = sleepStartTime+i;
            }
            currentGuard.addSleepTime(sleepTimes);
        }
    }
}
