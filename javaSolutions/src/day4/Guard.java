package day4;

import java.util.ArrayList;

public class Guard {

    int id;
    ArrayList<Integer> timesAsleep;

    Guard(int id) {
        this.id = id;
        this.timesAsleep = new ArrayList<Integer>();
    }

    public void addSleepTime(int[] minutes) {
        for (int minute: minutes) {
            this.timesAsleep.add(minute);
        }
    }

    @Override
    public boolean equals(Object obj) {
        boolean isEqual = false;

        if (obj instanceof Guard) {
            isEqual = (this.id == ((Guard) obj).id);
        }

        return isEqual;
    }

    public ArrayList<Integer> getTimesAsleep() {
        return this.timesAsleep;
    }
}
