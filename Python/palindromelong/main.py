def isPalindrome(s):
    return s == s[::-1]


def longPalindrome(s):
    long = s[0]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                if len(s[i:j+1]) > len(long):
                    long = s[i:j+1]

    return long


print(longPalindrome("cddb"))
