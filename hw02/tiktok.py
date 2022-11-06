def tik(tok):
    def insta(gram):
        print(tok, " ", gram)
    return insta

tik(tik(5)(print(6)))(print(7))