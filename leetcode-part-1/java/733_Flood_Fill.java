class Solution {
    /*public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;
        dfs(image, sr, sc, image[sr][sc], newColor);
        return image;
    }

    private void dfs(int[][] image, int r, int c, int color, int newColor) {
        // Recursively DFS
        if (image[r][c] == color) {
            image[r][c] = newColor;
            if (r - 1 >= 0) dfs(image, r - 1, c, color, newColor);
            if (r + 1 < image.length) dfs(image, r + 1, c, color, newColor);
            if (c - 1 >= 0) dfs(image, r, c - 1, color, newColor);
            if (c + 1 < image[0].length) dfs(image, r, c + 1, color, newColor);
        }
    }*/

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        Queue<Node> queue = new LinkedList<Node>();
        int color = image[sr][sc];
        if (color == newColor) return image;
        queue.add(new Node(sr, sc));
        // BFS with queue
        while (!queue.isEmpty()) {
            Node curr = queue.remove();
            int r = curr.r, c = curr.c;
            if (image[r][c] == color) {
                image[r][c] = newColor;
                if (r - 1 >= 0) queue.add(new Node(r - 1, c));
                if (r + 1 < image.length) queue.add(new Node(r + 1, c));
                if (c - 1 >= 0) queue.add(new Node(r, c - 1));
                if (c + 1 < image[0].length) queue.add(new Node(r, c + 1));
            }
        }
        return image;
    }

    class Node {
        int r;
        int c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
