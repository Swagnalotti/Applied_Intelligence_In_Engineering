def is_palindrome(input):
    input = input.replace(" ", "").lower()
    print(f"input string is {input}")
    if len(input) <= 1:
        return True

    elif input[0] == input[-1]:
        return is_palindrome(input[1: len(input) - 1])
    else:
        return False

print(is_palindrome("Race car"))