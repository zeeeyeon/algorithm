class Solution {
    public int solution(int n, int w, int num) {
        boolean leftToRight = true;
        
        int box = 0;
        int totalRow = (n + w - 1) / w;
        int currentColumn = 0;
        int currentRow = 0;
        int targetColumn = 0;
        int targetRow = 0;
        
        int[][] grid = new int[totalRow][w];
        
        for (int i = 1; i <= n; i++) {
            if (i == num) {
                targetColumn = currentColumn;
                targetRow = currentRow;
            }
            
            grid[currentRow][currentColumn] = i;
            
            if (leftToRight) {
                if (currentColumn == w - 1) {
                    currentRow++;
                    leftToRight = false;
                } else {
                    currentColumn++;
                }
            } else {
                if (currentColumn == 0) {
                    currentRow++;
                    leftToRight = true;
                } else {
                    currentColumn--;
                }
            }
        }
        
        while (targetRow < totalRow) {
            if (grid[targetRow][targetColumn] != 0) {
                box++;
            }
            targetRow++;
        }
        return box;
    }
}