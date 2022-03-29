#ALL DONE

from requests import get
from pprint import PrettyPrinter

#this is url return response and this api key from https://free.currencyconverterapi.com/free-api-key this website
BASE_URL = "https://free.currconv.com/"
API_KEY ="eea412017c362877e6b3"

printer = PrettyPrinter()
#it will return currencies id by this URL
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()
    return data


# this will print all id's
def print_currencies(currencies):
    for name,currency in currencies:
        name = currency['currencyName']
        symbol = currency.get('currencySymbol',"")
        _id = currency['id']
        print(f"{_id}-{name}-{symbol}")

        #this part shows how much exchange rate
def exchange_rate(currency1_id,currency2_id):
    endpoint =  f"api/v7/convert?q={currency1_id}_{currency2_id}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL+endpoint
    data = get(url).json()
    if len(data)==0:
        print("invalid currencies")
        return

    rate = list(data.values())[0]
    print(f"{currency1_id} -> {currency2_id} = {rate}")

    return rate
#it  converts one currency to another

def convert(currency1_id,currency2_id,amount):

    rate =exchange_rate(currency1_id,currency2_id)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("invalid amount")
        return
    converted_amount = rate*amount
    print(f"{currency1_id}-{amount} = {currency2_id} is equal to {converted_amount}")

def main():
    currencies = get_currencies()
    print("Welcome to currency converter")
    print("List : list different types of currencies")
    print("Convert : convert currencies from one to another")
    print("Rate : exchange rate of two currencies")
    print()

    while True:
        command = input("Enter command 'q' to quit:").lower()
        if command =='q':
            break
        elif command =='list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1_id = input("Enter you first currency id ").upper()
            currency2_id = input("Enter you second currency id").upper()
            amount = input("Enter your amount")
            convert(currency1_id,currency2_id,amount)
        elif command =='rate':
            currency1_id = input("Enter you first currency id ").upper()
            currency2_id = input("Enter you second currency id").upper()
            exchange_rate(currency1_id,currency2_id)
        else:
            print("invalid input")

if __name__ == '__main__':
    main()




