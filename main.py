def pal(str):
    for i in range(0, int(len(str)/2)):
        if str[i] !=str[len(str)-i-1]:
            return False
    return True
s=input()
ans=pal(s)
if(ans):
    print("palindrome")
else:
    print("Not a palindrome")
