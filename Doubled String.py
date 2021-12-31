def double_chars(x):
    tmp_str=""
    for i in x:
        tmp_str+=2*i
    return tmp_str

try:
    user_input=input()
    print(double_chars(user_input))
except:
    print("Something went wrong, please try again")
    quit()
