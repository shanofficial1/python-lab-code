text=input("Enter the string")
def is_fun(text):
    if text[0:2]=="is":
        print(text)
    else:
        text="is"+text
        print(text)
is_fun(text)

