from ex_5_2 import digits

def sum_digits(num: int):
    if num < 10:
        return num
    tot = sum(digits(num))
    return sum_digits(tot)

def main():
    while n := input("n? "):
        n = int(n)
        print(sum_digits(n))

if __name__ == "__main__":
    main()