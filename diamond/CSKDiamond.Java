import java.io.*;
import java.util.*;

public class CSKDiamond {

    protected char start;
    public CSKDiamond () {} 
    
    public String[] alphaStrings (int widest) { 
        String[] sArray = new String[widest];
        
        // builds the top half of the diamond
        char [] ts = tokenStream(widest);
        int i;
        for (i = 0; i < widest/2; i++) {
            sArray[i] = forToken (ts[i], widest, i);
        }
        
        // Copy strings to the bottom half
        for (int j = i-1; i < widest; j--) {
            String cs = new String(sArray[j]);
            cs = cs.replaceAll("[a-zA-Z]", "K");
            sArray[i++] = cs;
        }

        System.out.println();
        for (String s: sArray) 
            System.out.println (s); 
        return sArray;
    }

    public char[] tokenStream (int widest) {
        char[] stream = new char[widest];
        char[] csk = "CSSKKKKKK".toCharArray();

        for (int i = 0; i < widest/2; i++) {
            stream[i] = csk[i];
        }
        
        return stream;
    }

    public String forToken (char c, int widest, int row) {
        String inner  = getPads(row*2);
        String pads   = getPads((widest - inner.length()-2)/2);

        return pads + String.valueOf(c)+ inner + String.valueOf(c) + pads;

    }

    public String getPads (int n) {
        char[] charArray = new char[n];
        Arrays.fill(charArray, '.');
        return new String(charArray);
    }

}
