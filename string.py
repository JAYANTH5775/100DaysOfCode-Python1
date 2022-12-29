


def function (s):
    duplicate = 0
    st = ' '
    m = 1
    for i in range(1, len(s)):
        for j in range(1, len(s)):
            if s[i] == s[j]:
                duplicate = -1

            else:
                st[m] = s[i]
                m = m + 1
                m = m + 1

                duplicate = st[1]
    return duplicate


s = input("enter the string")
result = function(s)
if result == -1:
    print("the string contains the duplicate entries")
else:
    print("the first non repeated element is "+s[1])






