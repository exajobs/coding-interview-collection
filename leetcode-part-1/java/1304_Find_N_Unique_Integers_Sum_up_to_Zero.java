public int[] sumZero(int n) {
    int[] res = new int[n];
    // place negative sum(from 1 to n-1) in 0
    for (int i = 1; i < n; i++) {
        res[i] = i;
        res[0] -= i;
    }
    return res;
}
