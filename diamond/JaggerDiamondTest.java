import org.junit.*;
import static org.junit.Assert.*;

public class DiamondTest {

    @Test
    public void b() {
        String[ ] expected = 
        { 
            " A ", 
            "B B", 
            " A "
        };
        String[ ] actual = new Diamond('B').getStrings();
        assertArrayEquals(expected, actual);
    }

    @Test
    public void c() {
        String[ ] expected = 
        { 
            "  A  ", 
            " B B ", 
            "C   C",
            " B B ", 
            "  A  "
        };
        String[ ] actual = new Diamond('C').getStrings();
        assertArrayEquals(expected, actual);
    }
}
