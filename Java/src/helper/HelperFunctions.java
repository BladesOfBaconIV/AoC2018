package helper;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.io.IOException;


public class HelperFunctions {

    public static Stream getLines(String fileName) {
        try {
            return Files.lines(Paths.get(fileName));
        } catch (IOException e) {
            e.printStackTrace();
            return Stream.of();
        }
    }

    public static Stream getLinesAsInts(String fileName) {
        Stream stream;
        try {
            stream = Files.lines(Paths.get(fileName));
        } catch (IOException e) {
            e.printStackTrace();
            return Stream.of();
        }
        return stream.map(n -> (int) n);
    }
}
