import csv 
import pandas as pd

big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year, country_code):

    data = pd.read_csv(big_mac_file)
    filtered_data = data[(data['date'] == year) & (data['iso_a3'] == country_code.upper())]
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    data = pd.read_csv(big_mac_file)
    filtered_data = data[data['iso_a3'] == country_code.upper()]
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    data = pd.read_csv(big_mac_file)
    filtered_data = data[data['date'] == year]
    min_price = filtered_data['dollar_price'].min()
    return round(min_price, 2)

def get_the_most_expensive_big_mac_price_by_year(year):
    data = pd.read_csv(big_mac_file)
    filtered_data = data[data['date'] == year]
    max_price = filtered_data['dollar_price'].max()
    return round(max_price, 2)

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010, "arg")
    print(result_a)
    
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)
