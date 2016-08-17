#!/usr/bin/env python3
def numbered_lines():
    with open('small.txt', 'r') as f_1:
        lines = (f_1.readlines())
        with open('small_2.txt', 'w') as f_2:
            num = 0
            for line in lines:
                num += 1
                f_2.write(str(num) + ' ' + line)




def main():
    numbered_lines()

if __name__ == "__main__":
    main()
