
def main():
    V, a, b, c = map(int, input().split())
    
    while True:
        V -= a
        if V < 0:
            print("F")
            break
        V -= b
        if V < 0:
            print("M")
            break
        V -= c
        if V < 0:
            print("T")
            break

if __name__ == "__main__":
    main()