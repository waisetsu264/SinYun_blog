def test(inp):
    inp2 = str(inp)
    inp2 = list(inp2)
    inp2 = inp2[::-1]
    print(inp2)
    inp2 = "".join(inp2)
    print(inp2)
    inp2 = int(inp2)
    outp = inp + inp2
    print(outp)
    return outp


if __name__ == '__main__':
    test(123)
