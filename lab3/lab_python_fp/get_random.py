import random

def get_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)

def main():
    for i in get_random(5,1,3):
        print(i)

if __name__ == "__main__":
    main()
