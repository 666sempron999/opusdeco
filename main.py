# coding: utf-8

import pandas as pd
import time
from selenium import webdriver
import random


def create_product_list(pageAddress):
    """
    """
    # перейти на страницу
    browser = webdriver.Firefox()
    # browser = webdriver.Firefox()
    # browser = webdriver.PhantomJS()
    browser.get(pageAddress)
    print("Страница загрузилась. Ожидание 5 сек.")
    # time.sleep(5)

    # подготовить данные
    page = browser.find_element_by_id("content")
    table = page.find_elements_by_class_name("bx_catalog_item")

    textTable = list()
    for i in range(0, len(table)):
        textTable.append(table[i].text)

    # закрыть браузер
    browser.close()

    # вернуть или сохранить данные
    return textTable


def parse_data(rawHTML):
    """
    """
    tocsvData = list()
    for i in range(0, len(rawHTML)):
        
        inside = rawHTML[i].split("\n")
        
        s="".join(i for i in inside[1] if i.isdigit())
        
        inside[1] = s
        tocsvData.append(inside)

    return tocsvData


def save_product_in_csv(prodictList, fileName):
    """
    """
    df = pd.DataFrame(prodictList, columns=["Артикул", "Цена"])
    df.to_csv("{}.csv".format(fileName), index=False)
    print("Сохранено {} записей".format(len(prodictList)))


def main():

    url = input("Введите адресс страницы, с которой будут \
        собираться данные - ")

    pageData = create_product_list(url)
    tocsvData = parse_data(pageData)
    save_product_in_csv(tocsvData, "opusdeco")


if __name__ == '__main__':
    main()
