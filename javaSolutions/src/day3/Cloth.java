package day3;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Cloth {

    private int[][] space;
    private int[][] numClaims;
    private ArrayList<Integer> overlapping = new ArrayList<Integer>();
    private Set<Integer> claimIDs = new HashSet<Integer>();

    public Cloth(int x, int y) {
        this.space = new int[y][x];
        this.numClaims = new int[y][x];
    }

    public void addClaim(int id, int x, int y, int width, int height) {
        for (int i = x; i < x+width; i++) {
            for (int j = y; j < y+height; j++) {
                if (this.space[j][i] != 0) {
                    this.overlapping.add(this.space[j][i]);
                    this.overlapping.add(id);
                }
                this.space[j][i] = id;
                this.numClaims[j][i]++;
            }
        }
        this.claimIDs.add(id);
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
        int overalpArea = 0;
        for (int x = 0; x < this.numClaims[0].length; x++) {
            for (int y = 0; y < this.numClaims.length; y++) {
                if (this.numClaims[y][x] > 1) {
                    overalpArea++;
                }
            }
        }
        return overalpArea;
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
