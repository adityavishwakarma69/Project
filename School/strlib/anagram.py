def anag(s1,s2):
    if sorted(s1)==sorted(s2):
        print("it is an anagram")
    else:
        print("it is not an anagram")
    return
s1=str(input("enter first string: "))
s2=str(input("enter second string: "))
anag(s1,s2)
