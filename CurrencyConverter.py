import requests

def convertCurrency():
    initCurrency = input('Enter an inital currency [Example: USD/EUR/GBP/BRL]: ')
    targetCurrency = input('Enter a target currency [Example: USD/EUR/GBP/BRL]: ')
    
    while True:
        try:
            amount = float(input('Enter the amount: '))
        except:
            print('The amount must be a numeric value!')
            continue
        
        if not amount > 0:
            print("The amount must be greater than 0")
            continue
        else:
            break
    
    url = ('https://api.apilayer.com/fixer/convert?to=' + targetCurrency + '&from=' + initCurrency + '&amount=' + str(amount))
    payload = {}
    headers = {'apikey': '3iHp9NmHC27V2ol1okXz6hwExomXyUEk'}
    response = requests.request('GET', url, headers=headers, data=payload)
    status = response.status_code
    
    if status != 200:
        print('Uh oh, there was a problem. Please try again later')
        quit()
    
    result = response.json()
    print('Conversion result: ' + str(result['result']))

convertCurrency()