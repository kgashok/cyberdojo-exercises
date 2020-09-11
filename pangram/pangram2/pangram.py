from orderedset import OrderedSet
from string import ascii_lowercase as letters


class Checker:

    def test(self, text):

        alpha = OrderedSet(c for c in text.lower() if c.isalpha())

        out = "".join(alpha)
        print(out)

        return len(out) == 26 or self.test_partial(out)

    def test_partial(self, pt):

        return letters.find(pt) >= 0 \
            or letters.find(pt[::-1]) >= 0
