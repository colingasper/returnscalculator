def main():

    print('++++++++++++++++++++++++++++++++')
    pricebuy = float(input('Price of currency at purchase:'))
    shares = float(input('Number of shares purchased:'))

    investment = float(pricebuy) * float(shares)
    print('++++++++++++++++++++++++++++++++')
    print('Price of currency at purchase: $' + str(pricebuy))
    print('Number of shares purchased:' + str(shares))
    print('Total investment cost: $' + str(investment))
    print('++++++++++++++++++++++++++++++++')
    pricesell = float(input('Price of currency at sale:'))


    return1= pricesell-pricebuy
    return2 = return1/pricebuy
    percentreturn = float(return2 * 100)
    portfoliototal = (1 + return2) * investment


    print('Total return on investment:' + str(percentreturn) + '%')
    print('Current investment value: $' + str(portfoliototal))
    print('Total profit from investment: $' + str(portfoliototal-investment))
    print('++++++++++++++++++++++++++++++++')
    print('++++++++++++++++++++++++++++++++')

    repeat = input('Would you like to run again? (Y/N)')
    if repeat == 'Y' or 'y' or 'yes' or 'Yes' or 'YES':
        main()
    else:
        print('Goodbye!')
        exit()
main()
