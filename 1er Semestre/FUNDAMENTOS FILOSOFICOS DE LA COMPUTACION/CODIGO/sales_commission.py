#Program 5 -c1 page 160
#This program calculates sales commissions
keep_going = 'y'

#Calculate a series of commisions.
while keep_going == 'y':
    #Get a salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))

    #Calculte the commission
    commission= sales*comm_rate

    #Display the commission
    print('The commission is $', \
          format(commission,',.2f'),sep=' ')

    #See if the user wants to do another one.
    keep_going = input('Do you want to calculate anoher '+\
                       'commission (Enter y for yes): ')
