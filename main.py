from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def search_wikipedia(query):
    search_box = browser.find_element(By.NAME, 'search')
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

def scroll_paragraphs():
    paragraphs = browser.find_elements(By.CSS_SELECTOR, 'p')
    index = 0
    while index < len(paragraphs):
        print(paragraphs[index].text)
        index += 1
        if index < len(paragraphs):
            user_input = input("Нажмите Enter, чтобы увидеть больше параграфов, или введите 'назад', чтобы вернуться: ")
            if user_input.lower() == 'назад':
                break

def follow_link():
    links = browser.find_elements(By.CSS_SELECTOR, 'a')
    for index, link in enumerate(links):
        print(f"{index}: {link.text}")
    try:
        link_choice = int(input("Выберите номер ссылки, чтобы перейти по ней, или введите '-1', чтобы вернуться: "))
        if link_choice != -1 and 0 <= link_choice < len(links):
            links[link_choice].click()
            time.sleep(3)
    except ValueError:
        print("Пожалуйста, введите корректный номер.")

def return_to_initial_query(initial_url):
    browser.get(initial_url)
    time.sleep(3)

def main():
    global browser
    browser = webdriver.Chrome()
    browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
    time.sleep(5)

    query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(query)

    initial_url = browser.current_url  # Сохраняем URL первоначального запроса

    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть параграфы текущей статьи")
        print("2. Перейти на интересующую вас страницу")
        print("3. Вернуться к первоначальному запросу")
        print("4. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == '1':
            scroll_paragraphs()
        elif choice == '2':
            follow_link()
        elif choice == '3':
            return_to_initial_query(initial_url)
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

    browser.quit()

if __name__ == "__main__":
    main()