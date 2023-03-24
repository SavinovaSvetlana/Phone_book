import text_fields


def main_menu() -> int:
    print(text_fields.main_menu)
    lenght_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        chois = input('Выберите пунк меню:')
        if chois.isdigit() and 0 < int(chois) <= lenght_menu:
            return int(chois)
        else:
            print(f'Введите число от 1 до {lenght_menu}')


def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}.{contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        return True


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Ведите телефон: ')
    comment = input('Ведите коментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def input_index(message: str):
    return int(input(message))


def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений: ')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index - 1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index - 1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index - 1].get('comment')}


def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))
