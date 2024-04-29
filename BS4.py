from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/"  

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    title_element = soup.find('title')


    if title_element:
        title = title_element.text.strip()
        print(title)
    else:
        print("Title not found on the webpage.")

else:
    print("Error: Failed to retrieve the web page. Status code:", response.status_code)
    
    
"""
Output:

Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!

"""

