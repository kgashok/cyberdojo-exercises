import org.junit.*;
import static org.junit.Assert.*;

public class DigitFilterTest {

  // static private String Fizz = "Fizz";
  DigitFilter d3 = new DigitFilter(3, "Fizz");
  DigitFilter d5 = new DigitFilter(5, "Buzz");
  DigitFilter d7 = new DigitFilter(7, "Mix");

  @Test
  public void returnsFizzFor31() {
    String expected = "Fizz";
    String actual = d3.apply(31);

    assertEquals(expected, actual);
  }

  @Test
  public void returnsFizzFor51() {
    String expected = "Buzz";
    String actual = d5.apply(51);

    assertEquals(expected, actual);
  }

  @Test
  public void returnsFizzFor71() {
    String expected = "Mix";
    String actual = d7.apply(71);

    assertEquals(expected, actual);
  }
}
