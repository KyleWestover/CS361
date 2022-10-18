#!/usr/bin/env python
from urllib.request import urlopen
import certifi
import json
import ssl

def init_app():
    func_input = input("Main Menu: enter 'Q' to get a stock quote using a ticker symbol,"
    " enter 'S' to search for a ticker symbol using a company name, or enter 'E' to exit the program: ")

    if func_input.capitalize() == 'Q':
        stock_quote()
    elif func_input.capitalize() == 'S':
        symbol_search()
    elif func_input.capitalize() == 'E':
        quit()
    else:
        print("Please enter a valid response.")
        init_app()


def stock_quote():
            symbol_input = input("Stock Quote Menu: enter ticker symbol for stock quote, enter 'M' to return to main menu, or enter 'E' to exit: ")

            if symbol_input.capitalize() == "M":
                init_app()
            elif symbol_input.capitalize() == "E":
                print("Goodbye!")
                exit()
            else:
                try:
                    stock_data = get_jsonparsed_data("https://financialmodelingprep.com/api/v3/quote/%s?apikey=003809bd1c3fe691bf6135487a696621"%symbol_input)
                    stock_price = stock_data[0]["price"]
                    stock_symbol = stock_data[0]["symbol"]
                    stock_name = stock_data[0]["name"]
                except:
                    print("The ticker symbol entered does not exist. Try again.")
                    stock_quote()
                else:

                    pstring = "Company Name: " + stock_name + "\n" + "Symbol: " +  stock_symbol + "\n" + "Price: $" + str(stock_price) + "\n"
                    print(pstring+"\n")

                    quote_again = input("Would you like to check another stock quote? Enter 'Q' to enter another stock symbol, 'M' to return to main menu, or 'E' to exit the program: ")
                    if quote_again.capitalize() == 'Q':
                        stock_quote()
                    elif quote_again.capitalize() == 'M':
                        init_app()
                    elif quote_again.capitalize() == 'E':
                        print("Goodbye!")
                        quit()
                    else:
                        print("You entered an invalid response. Returning to main menu.")
                        init_app()



def symbol_search():
    name_input = input("Symbol Search Menu: enter Company Name (search term can only be one word), enter 'M' to return to main menu, or enter 'E' to exit the program: ")

    if name_input.title() == "M":
        init_app()
    elif name_input.capitalize() == "E":
        print("Goodbye!")
        exit()
    else:
        try:
            lookup_results = get_jsonparsed_data("https://financialmodelingprep.com/api/v3/search?query=%s&limit=100&apikey=003809bd1c3fe691bf6135487a696621"%name_input)

            for i in range(len(lookup_results)):
                company_name = lookup_results[i]["name"]
                company_symbol = lookup_results[i]["symbol"]
                exchange = lookup_results[i]["exchangeShortName"]

                print("\nCompany Name: %s\nTicker Symbol: %s\nExchange: %s\n"%(company_name, company_symbol, exchange))
        except:
            print("The company entered does not exist or was entered improperly. Try again.")
            symbol_search()
        else:
            search_again = input("Would you like to search for another stock or get a stock quote?\nEnter 'S' to search for another symbol, 'Q' to get a stock quote, 'M' to return to main menu, or 'E' to exit the program: ")
            if search_again.capitalize() == 'S':
                symbol_search()
            elif search_again.capitalize() == 'Q':
                stock_quote()
            elif search_again.capitalize() == 'M':
                init_app()
            elif search_again.capitalize() == 'E':
                print("Goodbye!")
                quit()
            else:
                print("You entered an invalid response. Returning to main menu.")
                init_app()

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    context = ssl.create_default_context(cafile=certifi.where())
    response = urlopen(url, context=context)
    data = response.read().decode("utf-8")
    return json.loads(data)

if __name__ == "__main__":

    init_app()

