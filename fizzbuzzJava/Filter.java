public class Filter { 
    private int dividend; 
    private String return_s; 
    
    Filter (int i, String s) {
        this.dividend = i;
        this.return_s = s;  
    }

    public String apply (int integer) {
        return (integer% dividend == 0) ? return_s : "";
    }

}
