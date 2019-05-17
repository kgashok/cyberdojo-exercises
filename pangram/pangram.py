class Checker:

    def test(self, text):

        alpha = set ()
        for i in text.lower():
            if i.isalpha(): alpha.add(i)


        print (alpha, len(alpha) )
        return len(alpha) == 26
