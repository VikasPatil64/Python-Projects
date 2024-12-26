import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = "https://en.wikipedia.org/wiki/Microsoft"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    for element in soup.find_all('h2'):
        data.append(element.text.strip())
        
    with open("data.csv", "w", newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Header'])
        for row in data:
            writer.writerow(row)
            
    print("Data has been successfully written to 'data.csv' file.")
    
if __name__ == "__main__":
    main()
    