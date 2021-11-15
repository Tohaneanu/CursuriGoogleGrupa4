from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os

browser = webdriver.Chrome(ChromeDriverManager().install())

header = []
browser.get('https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-ianuarie-ora-13-00/')
for i in range(1, 6):
    header_text = browser.find_element(By.XPATH, f'//*[@id="post-24911"]/div/div/table[1]/tbody/tr[1]/td[{i}]').text
    header.append(header.replace("ț",
                                 "t").replace(
        "ș", "s").replace("ă", "a").replace("î", "i").replace("â", "a"))
dictionar = {i: [] for i in header}


def has_numbers(string: str) -> bool:
    """
    :param string:
    :return: true if string don t have digits in all characters, else false
    """
    return not any(char.isdigit() for char in string)


def string_check(lista: list) -> list:
    """""
    :param lista: list of data take from table
    :return: concatenate successive strings which were separated by parsing through space and return the new list
    """
    for j in range(len(lista)):
        if j + 1 >= len(lista):
            break
        if has_numbers(lista[j]) and has_numbers(lista[j + 1]):
            j = 1
            while True:
                if j + j < len(lista) and has_numbers(lista[j + j]):
                    j = 1
                    lista[j] = lista[j] + " " + lista[j + j]
                    # print(lista[i])
                    lista.pop(j + j)
                else:
                    break
    return lista


def calculate_dict():
    for day in range(1, 7):
        try:
            browser.get(
                f'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/')

            table = browser.find_element(By.CLASS_NAME, 'entry-content').find_elements_by_tag_name("tr")
            table_rows = table[0:44]
            table_text = " "
            for element in table_rows:
                table_text = table_text + " " + element.text

            # print(table_text)
            head_max = table_text.find("Alba")
            table_text = table_text.replace("ț", "t").replace("ș", "s").replace("ă", "a").replace("î", "i").replace("â",
                                                                                                                    "a")
            garbage = table_text[0:head_max - 3]
            print(f"Garbage: {garbage}")
            # print(table_text)
            table_text = table_text.replace(garbage, "")
            table_text = table_text.replace("\n", " ").replace(",", ".")
            print(table_text)
            dataset = table_text.split(" ")

            dataset = string_check(dataset)
            print(dataset)
            if len(dataset) != 215:
                continue
            for j in range(0, len(header)):
                for index in range(int(j), len(dataset), len(header)):
                    # print(i, j)
                    dictionar[header[int(j)]].append(dataset[index])
            # print(dictionar)
            time.sleep(5)

        except NoSuchElementException:
            print("Not found data!")


calculate_dict()
print(dictionar)
for e in header:
    print(len(dictionar[e]))
if os.path.exists("covid.csv"):
    os.remove("covid.csv")
df = pd.DataFrame(dictionar)
df.to_csv("covid.csv", header=header, index=False)

time.sleep(10)
browser.close()
