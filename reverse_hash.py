
letters = "acdfgilmnoprstuw"


def hash(string):
    h = 7
    for i in range(len(string)):
        h = h * 23 + letters.index(string[i])
    return h


def unhash(number):
    if number < 7*23:
        return
    string = []
    while number != 7:
        q, r = divmod(number, 23)
        string.append(r)
        number = q
    string.reverse()
    return ''.join(letters[i] for i in string)


if __name__ == "__main__":
    assert hash("tortilla") == 593846452632
    assert unhash(hash("tortilla")) == "tortilla"
    assert unhash(292681030017238) == "crowdgifts"
    assert hash(unhash(292681030017238)) == 292681030017238
