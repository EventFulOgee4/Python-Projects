def main():
    print('This program converts US dollard to Pounds Sterling')
    print()
    
    dollars = float(input('Enter amount in dollars: '))
    
    pounds = convert_to_pounds(dollars)
    
    print('That is', pounds, 'pounds.')
    

convert_to_pounds = lambda dollars: dollars * 0.82

main()