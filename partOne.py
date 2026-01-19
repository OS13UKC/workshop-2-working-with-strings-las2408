def main():
    slow = input("Input ")
    myFunction(slow)

def myFunction(text):
    NewText = text.replace (" ","...")    # .replace replaces the first part before the comma with anything placed after 
    print NewText                        # prints the new version of the text

main()
