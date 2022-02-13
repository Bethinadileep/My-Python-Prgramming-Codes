for _ in range(int(input())):
    x = int(input())
    s = str(input())
    price = 0;
    if s.count("C")>s.count("N"):
        price = 60 * x;
    elif s.count("N")>s.count("C"):
        price = 40*x;
    elif s.count("C")==s.count("N"):
        price = 55*x;
    print(price)
