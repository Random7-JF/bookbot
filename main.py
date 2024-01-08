def main():
    with open("books/frankenstein.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(f"{line}")

if __name__ == "__main__":
    main()