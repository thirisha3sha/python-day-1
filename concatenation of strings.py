def concatenation(str1,str2):
    try:
        concat=str1+" "+str2
        return concat
    except TypeError as te:
        print(f"error occured.{te}")
    except ValueError as ve:
        print(f"error occured.{ve}")
def main():
    str1=input("enter the first string:")
    str2=input("enter the string2:")
    result=concatenation(str1,str2)
    if result:
        print(f"concatention of two strings:{result}")
if __name__=="__main__":
    main()
#method 2
str1=input("enter the string1:")
str2=input("enter the string2:")
result=str1+" "+str2
print(f"concatenation of two strings:",result)