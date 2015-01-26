public class QuickUnionUF {
    private int[] id;
    private int[] sz;

    public QuickUnionUF(int N) {
        id = new int[N];    // stores the parent of each object
        sz = new int[N];    // stores the size of the tree
        for (int i = 0; i < N; i++) {
            id[i] = i;
            sz[i] = 1;
        }
    }

    private int root(int i) {
        while (i != id[i]) {
            id[i] = id[id[i]];    // path compression, make every other node in the path point to its grandparent (thereby halving path length)
            i = id[i];
        }
        return i;
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        if (sz[i] < sz[j]) {    // make smaller tree point to larger tree
            id[i] = j;
            sz[j] += sz[i];
        } else {
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}
