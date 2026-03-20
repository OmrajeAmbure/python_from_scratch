def String_plaidrom(value):
    if value is None:
        return False
    else:
        if value[::-1] == value:
            return True
        else:
            return False
print(String_plaidrom("om"));
print(String_plaidrom("nayan"));

def String_plaidrom_without_slicing(value) -> str:
    rev = [];
    n = len(value);
    if value is None:
        return 1;
    while n > 0:
        rev.append(value[n-1]);
        n = n-1;
    return str.join('', rev);

string = "omraje";
check_Reverse = str(String_plaidrom_without_slicing(string));

print(f" reversed -> {check_Reverse} : original -> {string}");
if(str(check_Reverse) == string):
    print("String is Palindrome");
else:
    print("String is not Palindrome");