#create convert function

def convert(str):
    str=str.replace(":)","🙂")
    str=str.replace(":(","🙁")
    return(str)


#create main function
def main():
    n=input("type input   ")
    print(convert(n))

#call main
main()

