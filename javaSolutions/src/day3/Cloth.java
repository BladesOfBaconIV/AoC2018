package day3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Cloth {

    private int[][] space;
    private ArrayList<Integer> overlapping = new ArrayList<Integer>();
    private Set<Integer> claimIDs = new HashSet<Integer>();

    public Cloth(int x, int y) {
        this.space = new int[y][x];
    }

    public void addClaim(int id, int x, int y, int width, int height) {
        for (int i = x; i < x+width; i++) {
            for (int j = y; j < y+height; j++) {
                if (this.space[j][i] != 0) {
                    this.overlapping.add(this.space[j][i]);
                }
                this.space[j][i] = id;
                this.claimIDs.add(id);
            }
        }
    }

    public void addClaim(ArrayList<Integer> args) {
        addClaim(
                args.get(0),
                args.get(1),
                args.get(2),
                args.get(3),
                args.get(4)
        );
    }

    public int numOfOverlaps() {
        return this.overlapping.size();
    }

    public ArrayList<Integer> overlappedClaims() {
        return new ArrayList<Integer>(
                new HashSet<Integer>(this.overlapping)
        );
    }

    public Set<Integer> getClaimIDs() {
        return this.claimIDs;
    }

    public ArrayList<Integer> getOverlapping() {
        return this.overlapping;
    }
}
