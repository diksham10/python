#custom exception:
class i_hate_5(Exception):
    pass

def inp():
    num=int(input("enter a number:"))
    try:
        if num==5:
            raise i_hate_5("5 thichis ki maris")
        else:
            print("Thanks for not entering 5")
    except i_hate_5 as e:
        print(e)
        print("aba feri thich:")
        inp()
inp() 

#custom exception is done by inheriting Exception class into your custom class and pass and then call it by using raise and as e
