import csv 
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year, country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    query = f'date.str.startswith("{year}") and iso_a3 == "{country_code.upper()}"'
    filtered_data = df.query(query)
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    df = pd.read_csv('big-mac-full-index.csv')
    query = f'iso_a3 == "{country_code.upper()}"'
    filtered_data = df.query(query)
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query = f'date.str.startswith("{year}")'
    filtered_data = df.query(query)
    min_price = filtered_data['dollar_price'].idxmin()
    cheapest_country = df.loc[min_price, 'name']
    cheapest_country_code = df.loc[min_price, 'iso_a3']
    cheapest_price = df.loc[min_price, 'dollar_price']
    return f"{cheapest_country}({cheapest_country_code}): ${cheapest_price:.2}"

    

def get_the_most_expensive_big_mac_price_by_year(year):
    df = pd.read_csv('big-mac-full-index.csv')
    query = f'date.str.startswith("{year}")'
    filtered_data = df.query(query)
    max_price = filtered_data['dollar_price'].idxmax()
    expensive_country = df.loc[max_price, 'name']
    expensive_country_code = df.loc[max_price, 'iso_a3']
    expensive_price = df.loc[max_price, 'dollar_price']
    return f"{expensive_country}({expensive_country_code}): ${expensive_price:.2}"

   

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010, "arg")
    print(result_a)
    
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
