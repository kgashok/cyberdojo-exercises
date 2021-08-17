import org.junit.*;
import static org.junit.Assert.*;
public class IntDiamondTest {
    @Test
    public void numberTwo() {
        String[] expected = {
                " 1 ",
                "2 2",
                " 1 ",
        };
        assertArrayEquals(expected, new IntDiamond().alphaStrings('2') );
    }

    @Test
    public void starThreeWideLong() {
        String[] expected = {
               "  *  ",
               " * * ",
               "*   *",
               " * * ",
               "  *  ",
        };

        assertArrayEquals(expected, new StarDiamond().alphaStrings(3) );
    }


    @Test
    public void lineThreeWideLong() {
        String[] expected = {
           "  ^  ",
            " / \\ ",
            "|   |",
            " \\ / ",
            "  v  ",
        };
        String [] actual = new LineDiamond().alphaStrings(3);
        System.out.println("Three Wide Long Diamond!");
        for (String s: actual)
            System.out.println(s);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void lineFiveWideLong() {
    String[] expected = {
            "   ^   ",
            "  / \\  ",
            " /   \\ ",
            "|     |",
            " \\   / ",
            "  \\ /  ",
            "   v   ",
    };
    String [] actual = new LineDiamond().alphaStrings(4);
    System.out.println("Five wide long diamond!");
    for (String s: actual)
    System.out.println(s);
    assertArrayEquals(expected, actual);
    }

    @Test
    public void SmallLineDiamond() {
    String [] actual = new LineDiamond().alphaStrings(2);
    System.out.println();
    for (String s: actual)
    System.out.println(s);
    }

    @Test
    public void BigLineDiamond() {
        System.out.println();
        String [] actual = new LineDiamond().alphaStrings(11);
        for (String s: actual)
            System.out.println(s);
    }
}
