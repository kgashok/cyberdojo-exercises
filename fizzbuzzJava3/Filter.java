import java.util.*;

public class Filter implements Comparable<Filter> {
  private int divisor;
  private String return_s;

  Filter(int i, String s) {
    this.divisor = i;
    this.return_s = s;
  }

  public String apply(int integer) {
    return (integer % divisor == 0) ? return_s : "";
  }

  public int getDivisor() {
    return divisor;
  }

  public String getString() {
    return return_s;
  }

  @Override
  public int compareTo(Filter CompareF) {
    int compareDiv = CompareF.getDivisor();
    return this.divisor - compareDiv;
  }

  @Override
  public String toString() {
    return "[" + divisor + "," + return_s + "]";
  }
}
