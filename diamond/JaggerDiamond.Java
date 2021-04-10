public class Diamond {

    private char widest;
    private int radius;
    private int diameter;

    public Diamond(char widest) {
        this.widest = widest;
        this.radius = widest - 'A';
        this.diameter = radius * 2 + 1;
    }

    public String[ ] getStrings() {
        char[ ][ ] matrix = new char[diameter][];
        for (int i = 0; i < diameter; i++) {
            matrix[i] = new char[diameter];
            for (int j = 0; j < diameter; j++) {
                if (onEdge(i,j))
                    matrix[i][j] = edgeChar(i);
                else
                    matrix[i][j] = ' ';
            }
        }
        String[ ] result = new String[diameter];
        for(int i = 0; i < diameter; i++) {
            result[i] = new String(matrix[i]);
        }
        return result;
    }

    private boolean onEdge(int i, int j) {
        return Math.abs(i-radius) + Math.abs(j-radius) == radius;
    }

    private char edgeChar(int i) {
        return (char)((int)widest - Math.abs(i - radius));
    }
}
