public class Filter { 
    private int divisor; 
    private String return_s; 
    private Boolean digitCheck = false; 

    public int getDivisor () { 
        return divisor;
    }

    public void setDigitCheck (Boolean val) { 
        digitCheck = val;
    }

    Filter (int i, String s) {
        this.divisor= i;
        this.return_s = s;  
    }

    Filter (int i, String s, Boolean d) {
        this (i, s); 
        this.digitCheck = d; 
    }

    public String apply (int integer) {
        Boolean isMultiple = (integer% divisor== 0);
        Boolean digitPresent = Integer.toString(integer)
                                .contains(String.valueOf(divisor)); 
 
        return (isMultiple || digitCheck  && digitPresent) ?
                    return_s : "";
    }

}
