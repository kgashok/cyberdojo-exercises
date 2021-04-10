public class DigitFilter extends Filter {

  DigitFilter(int i, String s) {
    super(i, s);
  }

  public String apply(int integer) {
    Boolean digitPresent = Integer.toString(integer).contains(String.valueOf(getDivisor()));

    return digitPresent ? getString() : "";
  }
}
