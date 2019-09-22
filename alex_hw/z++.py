
def z_plus_plus(string):
    mapper = {
        '(': ')', ')': '(',
        '[': ']', ']': '[',
        '{': '}', '}': '{',
    }
    while True:
        i = 1  # resetting the index back to 1 so we can do another check
        
        found = False
        while i < len(string):
            'checking if the first character matches the current character, 1 at a time'
            first_char = string[0]
            cur_char = string[i]
            
            if first_char == mapper[cur_char]:
                found = True
                'pop first and current character from string'
                string = string[1:i] + string[i+1:]
                break
            i += 1
        
        if not found:
        	return False
        if len(string) == 1:
        	return False
        if len(string) == 0:
        	return True

if __name__ == '__main__':
    test_str = '[]{}()';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '{([])}';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '()[{}]';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '[{}()]';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '[({}))';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '([{}()]';
    x = z_plus_plus(test_str); print(test_str, x);
    test_str = '(((())))';
    x = z_plus_plus(test_str); print(test_str, x);
