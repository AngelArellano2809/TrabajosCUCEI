#ARELLANO GRANADOS ANGEL MARIANO
#Table showing the numbers 1 through 10
#and their squares.

def main():
    #print the table headings.
    print ('Number\tSquare')
    print ('--------------')

    #print the number 1 through 10
    #and their squares.
    for number in range (1,11):
        square = number**2
        print(number,'\t',square)

#Call the main function
main()
