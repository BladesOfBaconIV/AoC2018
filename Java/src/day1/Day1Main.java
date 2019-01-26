package day1;

import java.util.stream.Stream;
import helper.HelperFunctions;

public class Day1Main {

    public static void main(String[] args) {
        Stream<String> lines = HelperFunctions.getLines("input.txt");

        lines.forEach(System.out::println);
    }
}
