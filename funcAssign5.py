# Andrew Grant
# 105226219

def palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])


temp = input("Enter word: ")
print(f'Result: {palindrome(temp)}')
