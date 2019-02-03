package helperClasses;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.util.stream.IntStream;
import java.io.IOException;

public class inputParser {

    private static final String path = "D:\\\\Git\\AoC2018\\javaSolutions\\src\\";

    public static Stream getLines(String fileName) {
        try {
            return Files.lines(Paths.get(path + fileName));
        } catch (IOException e) {
            e.printStackTrace();
            return Stream.of();
        }
    }

    public static IntStream getLinesAsInts(String fileName) {
        try {
            return Files.lines(Paths.get(path + fileName)).mapToInt(i -> Integer.parseInt(i));
        } catch (IOException e) {
            e.printStackTrace();
            return IntStream.of();
        }
    }

}
