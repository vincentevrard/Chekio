def checkio(game):
    for i in range(len(game)):
        if game[i][0] == game[i][1] == game[i][2]!=".":
            return game[i][0]
        if game[0][i]==game[1][i]==game[2][i]!=".":
            return game[0][i]
        if game[0][0]==game[1][1]==game[2][2]!="." or game[0][2]==game[1][1]==game[2][0]!=".":
            return game[1][1]
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

