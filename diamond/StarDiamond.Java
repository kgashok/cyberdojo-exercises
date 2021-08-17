import java.io.*; 

class StarDiamond extends Diamond { 

    public StarDiamond () { 
        this.start = '*';
    }

    public String[] alphaStrings (int number) {
          return alphaStrings ((char)(start + number-1) );          
    }

    public String forToken (char c, char widest, Boolean...params) {
        String pads  = space(widest-c);
        String inner = space(sizeOf(c)-2);
        if (c == start)
            return pads + String.valueOf(c) + pads;
        else
            return pads+String.valueOf('*') + inner + String.valueOf('*')+pads;
        
    }
}
