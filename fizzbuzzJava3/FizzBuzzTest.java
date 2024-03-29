import org.junit.*;
import static org.junit.Assert.*;

public class FizzBuzzTest {

  FizzBuzz fb = new FizzBuzz();
  private static String Fizz = "Fizz";
  private static String Buzz = "Buzz";
  private static String Mix = "Mix";

  @Before
  public void addFilters() {
    fb.addFilter(new Filter(3, Fizz));
    fb.addFilter(new Filter(5, Buzz));
  }

  @Test
  public void returnsFizzFor3to3() {
    Object[] expected = {"Fizz"};
    Object[] actual = fb.filter(range(3, 3));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returns1And2For1and2() {
    Object[] expected = {1, 2};
    Object[] actual = fb.filter(range(1, 2));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFizzAndBuzzFor3to5() {
    Object[] expected = {Fizz, 4, Buzz};
    Object[] actual = fb.filter(range(3, 5));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returns13and14andFizzBuzzFor13to15() {
    Object[] expected = {13, 14, Fizz + Buzz};
    Object[] actual = fb.filter(range(13, 15));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFizzToFizzBuzzFor3to30() {
    Object[] expected = {
      "Fizz",
      4,
      "Buzz",
      "Fizz",
      7,
      8,
      "Fizz",
      "Buzz",
      11,
      "Fizz",
      13,
      14,
      "FizzBuzz",
      16,
      17,
      "Fizz",
      19,
      "Buzz",
      "Fizz",
      22,
      23,
      "Fizz",
      "Buzz",
      26,
      "Fizz",
      28,
      29,
      "FizzBuzz"
    };

    Object[] actual = fb.filter(range(3, 30));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void Print3to30() {
    Object[] res = fb.filter(range(3, 30));

    for (Object r : res)
      if (r.getClass() == java.lang.String.class) System.out.print("\"" + r + "\"" + ", ");
      else System.out.print(r + ", ");

    assertTrue(true);
  }

  @Test
  public void returnsFIZZandFIZZBUZZMIXfor102to105() {
    fb.addFilter(new Filter(7, "Mix"));

    Object[] expected = {Fizz, 103, 104, Fizz + Buzz + Mix};
    Object[] actual = fb.filter(range(102, 105));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZand22For21to22() {

    Object[] expected = {Fizz, 22};
    Object[] actual = fb.filter(range(21, 22));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZBUZZAndFIZZFor30to31() {

    fb.addFilter(new DigitFilter(3, "Fizz"));

    Object[] expected = {Fizz + Buzz, Fizz};
    Object[] actual = fb.filter(range(30, 31));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZMIX_FIZZ_FIZZFor37to39() {

    fb.addFilter(new DigitFilter(3, "Fizz"));
    fb.addFilter(new DigitFilter(7, "Mix"));

    Object[] expected = {Fizz + Mix, Fizz, Fizz};
    Object[] actual = fb.filter(range(37, 39));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZBUZZMIXFor1357and1358_withDigitChecksFor3and5and7() {
    fb.addFilter(new DigitFilter(3, "Fizz"));
    fb.addFilter(new DigitFilter(5, "Buzz"));
    fb.addFilter(new Filter(7, "Mix"));
    fb.addFilter(new DigitFilter(7, "Mix"));

    Object[] expected = {Fizz + Buzz + Mix, Fizz + Buzz + Mix};
    Object[] actual = fb.filter(range(1357, 1358));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZBUZZMIXFor137and135_withDigitChecksFor3and5and7() {
    fb.addFilter(new DigitFilter(3, "Fizz"));
    // fb.addFilter(new DigitFilter(5, "Buzz") );
    // fb.addFilter(new Filter(7, "Mix") );
    fb.addFilter(new DigitFilter(7, "Mix"));

    Object[] expected = {Fizz + Buzz, Fizz, Fizz + Mix};
    Object[] actual = fb.filter(range(135, 137));
    assertArrayEquals(expected, actual);
  }

  @Test
  public void returnsFIZZMIXFor137and135_withDigitChecksFor3and7() {
    fb.addFilter(new DigitFilter(7, "Mix"));
    fb.addFilter(new DigitFilter(3, "Fizz"));
    fb.sortFilter();
    Object[] expected = {Fizz + Buzz, Fizz, Fizz + Mix};
    Object[] actual = fb.filter(range(135, 137));
    assertArrayEquals(expected, actual);
  }

  private int[] range(int start, int end) {
    int[] range = new int[end - start + 1];
    for (int i = 0; i < range.length; i++) range[i] = start + i;
    return range;
  }
}
