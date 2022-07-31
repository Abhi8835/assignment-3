def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
sentence= input("enter the sentence:")
print("The reversed string is : ", sentence)
print(reverse(sentence))
