import java.util.ArrayList; 
import java.util.*;

public class FizzBuzz {

    private ArrayList<Filter> filters = new ArrayList<Filter>(); 

    public Object[] filter(int[] integers) {
        Object [] res = new Object [integers.length]; 
        for (int i = 0; i < integers.length; i++) 
            res[i] = convert(integers[i]);
        
        return res;
    }

    public Object convert (int number) {
        String res = ""; 
 
        for (Filter f: filters)
            if (!res.contains(f.apply(number) ) )
                res += f.apply(number);
        
        return (res.length() == 0) ? number : res;
    }

    public void addFilter (Filter f) {
        filters.add(f); 
    } 
    // http://www.javatpoint.com/Sorting-in-collection-framework

    public void sortFilter(){
        Collections.sort(filters);
    }
    
}
