class Solution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int[][] newGrid = new int[grid.length][grid[0].length];
        int m = grid.length;
        int n = grid[0].length;
        // Compute final move
        int true_k = k % (m * n);
        // Row move
        int move_i = true_k / n;
        // Column move
        int move_j = true_k % n;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int new_i = i + move_i;
                int new_j = (j + move_j) % n;
                // Move 1 row if (move_j + j >= n
                if (move_j + j >= n) new_i ++;
                new_i %= m;
                newGrid[new_i][new_j] = grid[i][j];
            }
        }
        // Copy the grid into a list for returning.
        List<List<Integer>> result = new ArrayList<>();
        for (int[] row : newGrid) {
            List<Integer> listRow = new ArrayList<>();
            result.add(listRow);
            for (int v : row) listRow.add(v);
        }
        return result;
    }
}
