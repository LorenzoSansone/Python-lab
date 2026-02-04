def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n #Use n + n to test the error -> I have made an error to trigger the error test

if __name__ == "__main__":
    main()
