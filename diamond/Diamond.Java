import java.io.*;

public class Diamond {

    protected char start; 
    public Diamond () { this.start = 'A';} 
    
    public String[] alphaStrings (char widest) { 
        String[] sArray = new String[sizeOf(widest)];
        
        int i = 0;
        // builds the top half of the diamond
        for (char c: tokenStream(widest) )
             sArray[i++] = forToken (c, widest);

        // Copy strings to the bottom half
        for (int j = i-2; j >= 0; j--)
            sArray[i++] = new String(sArray[j] );
        return sArray;
    }

    public char[] tokenStream (char widest) {
         char[] stream = new char[widest - start +1];
         char c = start;
         for (int i = 0; c <= widest; c = (char)(c+1), i++)
            stream[i] = c;
         return stream;
    }

    public String forToken (char c, char widest, Boolean...params) {
        String pads  = space(widest-c);
        String inner = space(sizeOf(c)-2);
        if (c == start)
            return pads + String.valueOf(c) + pads;
        else
            return pads+String.valueOf(c) + inner + String.valueOf(c)+pads;
    }

    public int sizeOf (char input) {
        int inner = 2* ((char)input - (char)start) - 1;
        int size  = (inner < 1) ? 1 : inner + 2;
        return size;
    }
    public String space (int len) { 
         String s =""; 
         for (int i = 0; i < len; i++) 
            s = s + " ";
         return s;
    }    
    
    /* Legacy */
    public String[] Output(char input) {
        
        int inner = 2* (input - 65) - 1;
        int size  = (inner < 1) ? 1 : inner + 2;

        String[] result = new String[size];

        char first = 'A';
        int i = 0;

        char [] alphabets = {'A', 'B', 'C'};

        
        for (String s: alphaStrings(input)) 
            System.out.println (s);
        
        if (input == 'A')
            result[i] = String.valueOf(first);

        if (input == 'B') {
            result[i]   = space(inner) + String.valueOf(first) + space(inner);
            result[inner] = String.valueOf(itoa(first+1)) + space(inner) + 
                            String.valueOf(itoa(first+1));

            result[i+2] = space(inner) + String.valueOf(first) + space(inner);
        }
        if (input == 'C') {
            result[i]   = space(inner-1) + String.valueOf(first) + space(inner-1);
            result[i+1] = space(inner-2) + String.valueOf(itoa(first+1)) + space(inner-2) + 
                            String.valueOf(itoa(first+1)) + space(inner/2);

            result[inner-1] = String.valueOf(itoa(first+2)) + space(inner) + String.valueOf(itoa(first+2));


            result[i+3] = space(inner-2) + String.valueOf(itoa(first+1)) + space(inner-2) + 
                            String.valueOf(itoa(first+1)) + space(inner-2);
            result[i+4] = space(inner-1) + String.valueOf(first) + space(inner-1);
        }

        return result; 

    }

    public char itoa (int number) {
         return (char)number;
    }


}