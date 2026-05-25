#palindrome

text ="racecar"

def check_is_palindrome(text):
    # return text == text[::-1]

    left = 0
    right = len(text) -1
    print(right)

    while left < right:
        if text[left] != text[right]:
            return False
        
        left += 1
        right -=1

    return True





res = check_is_palindrome(text) 

if res is True:
    print("yes it is palindrome")
else:
    print("Not a palindrome")    
