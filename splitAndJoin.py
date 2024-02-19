def split_and_join(line):
    # write your code here
    return line.replace(' ', '-')

if __name__ == '__main__':
    line = "This is a string";
    result = split_and_join(line)
    print(result)