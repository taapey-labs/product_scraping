# sssdfd

def find_duplicate_char(s):
    """
    find last index of highly repeated character in a string

    """
    # create a dictionary to store the count of each character
    char_count = {}

    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1

    # find the character with the highest count
    max_count = 0
    max_char = ''
    print(char_count)
    for key in char_count:
        if char_count[key] > max_count:
            max_count = char_count[key]
            max_char = key
    # return max_char
    # find the last index of the character with the highest count
    for i in range(len(s)-1, -1, -1):
        if s[i] == max_char:
            return i
    return -1


if __name__ == '__main__':
    print(find_duplicate_char('sdfdsdfd'))
