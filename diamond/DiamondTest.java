import org.junit.*;
import static org.junit.Assert.*;

public class DiamondTest {

  @Test
  public void ArrayOfOneContainingAForA() {
    String[] expected = {"A"};

    assertArrayEquals(expected, new Diamond().alphaStrings('A'));
  }

  @Test
  public void ArrayOfThreeContainingABBAForB() {
    String[] expected = {" A ", "B B", " A "};

    assertArrayEquals(expected, new Diamond().alphaStrings('B'));
  }

  @Test
  public void ArrayofFiveContainingABBCCBBAForC() {
    String[] expected = {
      "  A  ", " B B ", "C   C", " B B ", "  A  ",
    };
    assertArrayEquals(expected, new Diamond().alphaStrings('C'));
  }

  @Test
  public void ArrayofSevenContainingABBCDDCBBAForD() {
    String[] expected = {
      "   A   ", "  B B  ", " C   C ", "D     D", " C   C ", "  B B  ", "   A   ",
    };
    assertArrayEquals(expected, new Diamond().alphaStrings('D'));
  }

  @Test
  public void ArrayofFourContainingCSKKFor4() {
    String[] expected = {
      ".CC.", /* i = 0, inner = 0; */ "S..S", /* i = 1, inner = 2; */ "K..K", ".KK.",
    };
    assertArrayEquals(expected, new CSKDiamond().alphaStrings(4));
  }

  @Test
  public void ArrayofFourContainingCSKKFor6() {
    String[] expected = {
      "..CC..", /* i = 0, inner = 0; */ ".S..S.", /* i = 1, inner = 2; */
      "S....S", /* i = 2, inner = 4; */ "K....K", ".K..K.", "..KK..",
    };
    assertArrayEquals(expected, new CSKDiamond().alphaStrings(6));
  }

  @Test
  public void ArrayofFourContainingCSKKFor8() {
    String[] expected = {
      "...CC...", /* i = 0, inner = 0; */
      "..S..S..", /* i = 1, inner = 2; */
      ".S....S.", /* i = 2, inner = 4; */
      "K......K", /* i = 2, inner = 6; */
      "K......K", /* i = 2, inner = 6; */
      ".K....K.", /* i = 2, inner = 4; */
      "..K..K..", /* i = 1, inner = 2; */
      "...KK...", /* i = 0, inner = 0; */
    };
    assertArrayEquals(expected, new CSKDiamond().alphaStrings(8));
  }
}
