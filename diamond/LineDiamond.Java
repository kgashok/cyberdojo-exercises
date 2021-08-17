import java.io.*;
import java.util.*;

class LineDiamond extends StarDiamond {
    private char end;

    public LineDiamond () {
        this.start = '^';
        this.end   = 'v';
    }

    public String[] alphaStrings (char widest) { 
        String[] sArray = new String[sizeOf(widest)];
        
        int i = 0;
        char[] ts = tokenStream(widest);
        
        for (char c: ts )
             sArray[i++] = forToken (c, widest);

        for (int j = i-2; j >= 1; j--)
            sArray[i++] = new StringBuilder(sArray[j]).reverse().toString();
        sArray[i] = forToken(start, widest, true);
        
        return sArray;
    }
    
    public String forToken (char c, char widest, Boolean...params) {
      boolean reverse = params.length > 0 ? params[0].booleanValue() : false;
      String pads  = space(widest-c);
      String inner = space(sizeOf(c)-2);

      String res;

      if (reverse)
        res = pads + String.valueOf(end) + pads;
      else if (c == start)
        res = pads + String.valueOf(start) + pads;
        
      else if (c == widest)
        res = String.valueOf('|') + inner + String.valueOf('|');
      else
        res = pads+String.valueOf('/') + inner + String.valueOf('\\')+pads;
 
      return res;
    }    

}