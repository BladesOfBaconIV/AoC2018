package day4;

import helperClasses.inputParser;

import java.util.*;
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
    public static final Pattern minute = Pattern.compile("(?<=\\d\\d:)\\d+");

    public static void main(String[] args) {
        Supplier<Stream<String>> lines = () -> inputParser.getLines("day4//input.txt");

        lines.get().sorted().forEach(Day4Main::updateGuardList);

        // Part 1
        guards.sort((g1, g2) ->
                        String.valueOf(g1.getTimesAsleep().size())
                            .compareTo(String.valueOf(g2.getTimesAsleep().size())));
        Guard sleepiestGuard = guards.get(0);
        int sleepiestMinute =
                sleepiestGuard.getTimesAsleep()
                        .stream()
                        .collect(Collectors.groupingBy(m -> m, Collectors.counting()))
                        .entrySet()
                        .stream()
                        .max(Comparator.comparing(Map.Entry::getValue))
                        .get()
                        .getKey();
        int part1Ans = sleepiestMinute * sleepiestGuard.id;

        // Part 2


        System.out.printf("Part 1: %d\n Part 2:", part1Ans);
    }

    public static void updateGuardList(String s) {
        Matcher matches;
        if (s.indexOf("#") != -1) { // if a guard swap line
            matches = guardID.matcher(s);
            matches.find();
            System.out.println(s);
            System.out.println(matches.groupCount());
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
        else if (s.indexOf("falls") != -1) { // else if a guard falls asleep set start time
            matches = minute.matcher(s);
            sleepStartTime = Integer.parseInt(matches.group(0));
        }
        else if (s.indexOf("wakes") != -1){ // guard must be waking up
            matches = minute.matcher(s);
            int sleepEndTime = Integer.parseInt(matches.group(0));
            int[] sleepTimes = new int[sleepEndTime - sleepStartTime];
            for (int i = 0; i < sleepTimes.length; i++) {
                sleepTimes[i] = sleepStartTime+i;
            }
            currentGuard.addSleepTime(sleepTimes);
        }
        else {
            System.out.println("None of above matched");
        }
    }
}
