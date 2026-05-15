def is_mirror_image(s1, s2):
    result = ""

    for ch in reversed(s1):

        if ch == '[':
            result += ']'
        elif ch == ']':
            result += '['

        elif ch == '{':
            result += '}'
        elif ch == '}':
            result += '{'

        elif ch == '(':
            result += ')'
        elif ch == ')':
            result += '('

        elif ch == '<':
            result += '>'
        elif ch == '>':
            result += '<'

        elif ch == 'b':
            result += 'd'
        elif ch == 'd':
            result += 'b'

        elif ch == 'p':
            result += 'q'
        elif ch == 'q':
            result += 'p'

        else:
            result+= ch  # invalid character

    return result == s2
print(is_mirror_image("[HOW]", "[WOH]"))