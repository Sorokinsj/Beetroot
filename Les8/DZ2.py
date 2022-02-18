
def nested_parentheses(incoming):
    left_s = "("
    right_s = ")"
    s = 0
    if incoming[0] == left_s:
        for i in range (0, len(incoming)):
            if incoming[i] == left_s:
                s = s + 1
            elif incoming[i] == right_s:
                s = s - 1
        print (s == 0)
    elif incoming[0] == right_s:
        print (s != 0)
    return incoming

if __name__ == "__main__":
    nested_parentheses (input('Напишите скобочки '))