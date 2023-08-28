#!/usr/bin/env python3
"""dictionary in google search"""
import xlsxwriter
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    """ Main function of this file """
    # Create Workbook and worksheet
    workbook = xlsxwriter.Workbook('dictionary_explain.csv')
    worksheet = workbook.add_worksheet()

    # Set column width
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 300)

    #Create heading format bold
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'WORD', bold)
    worksheet.write('B1', 'EXPLANATION', bold)

    site = "https://google.com/search?q="
    with open('dictionary.txt', 'r', encoding="utf-8") as keywords:
        i=2
        for search in keywords:
            search_site = site+search
            browser = webdriver.Firefox()
            browser.get(search_site)
            CELL_A = 'A'+str(i)
            CELL_B = 'B'+str(i)
            try:
                element = browser.find_element(By.CSS_SELECTOR, ".O5uR6d")

            except selenium.common.exceptions.NoSuchElementException:
                browser.close()
                continue

            print(f"{search}Explaination: {element.text}")
            worksheet.write(CELL_A, search.strip(), bold)
            worksheet.write(CELL_B, element.text)
            browser.close()
            i += 1

            with open('new_dictionary.txt', 'a', encoding="utf-8") as file:
                file.write(f"{search}")
        print("*** All Keywords are searched ***")
        workbook.close()

if __name__ == "__main__":
    main()
