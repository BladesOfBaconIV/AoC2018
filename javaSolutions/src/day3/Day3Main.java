package day3;

import helperClasses.inputParser;

import java.util.ArrayList;
import java.util.Set;
import java.util.function.Supplier;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class Day3Main {

    public static Cloth cloth = new Cloth(1000, 1000);
    public static Pattern p = Pattern.compile("-\\d+|\\d+");

    public static void main(String[] args) {
        Supplier<Stream<String>> claims = () -> inputParser.getLines("day3\\input.txt");


        // Part 1
        claims.get().forEach(Day3Main::insertClaim);
        int overlap = cloth.numOfOverlaps();

        // Part 2
        Set<Integer> ids = cloth.getClaimIDs();
        ArrayList<Integer> overlappingClaims = cloth.overlappedClaims();
        ids.removeAll(overlappingClaims);
        int uniqueID = -1;
        if (!ids.isEmpty() && ids.size() < 2) {
            for (int id: ids) {
                uniqueID = id;
            }
        }
        else {
            System.out.printf("Size of ids is %d\n\n", ids.size());
        }

        System.out.printf("Part 1:\n%d, Part 2: %d", overlap, uniqueID);
    }

    public static void insertClaim(String c) {
        Matcher mathches = p.matcher(c);
        ArrayList<Integer> args = new ArrayList<Integer>();
        while (mathches.find()) {
            args.add(Integer.parseInt(mathches.group(0)));
        }
        cloth.addClaim(args);
    }

}
