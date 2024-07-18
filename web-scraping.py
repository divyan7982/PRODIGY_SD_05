from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

def scrape_product_data(url):
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide the path to it
    driver.get(url)
    time.sleep(5)  # Allow time for the page to load

    products = []
    product_elements = driver.find_elements(By.CSS_SELECTOR, 'article.product_pod')
    
    for product in product_elements:
        try:
            name = product.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
            price = product.find_element(By.CSS_SELECTOR, 'p.price_color').text
            rating_element = product.find_element(By.CSS_SELECTOR, 'p.star-rating')
            rating = rating_element.get_attribute('class').split()[-1]
            
            print("Debug - Name:", name)  # Debugging statement
            print("Debug - Price:", price)  # Debugging statement
            print("Debug - Rating:", rating)  # Debugging statement

            products.append({
                'Name': name.strip(),
                'Price': price.strip(),
                'Rating': rating.strip()
            })
        except Exception as e:
            print("Error:", e)
            continue

    driver.quit()
    return products

def save_to_csv(products, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)

    print(f'Data saved to {filename} successfully.')

if __name__ == '__main__':
    url = 'http://books.toscrape.com/'
    products = scrape_product_data(url)
    save_to_csv(products, 'books_toscrape.csv')
