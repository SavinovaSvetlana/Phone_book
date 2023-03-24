import phone_book

pb = phone_book.PhoneBook('2\phone.txt')

while True:
    print(pb.main_menu())
    choice = int(input('Выберете пункт меню: '))
    match choice:
        case 1:
            print(pb)

        case 2:
            name = input('Ведите имя: ')
            phone = input('Ведите номер телефона: ')
            comment = input('Ведите комментарий: ')
            pb.new_contact(name, phone, comment)
        case 3:
            word = input('Введите поисковый запрос: ')
            print(pb.search(word))
        case 4:
            print(pb)
            index = int(
                input('Ведите индекс контакта, который будем изменять'))
            name = input(
                'Ведите имя (или Enter, чтобы оставить без изменений): ')
            phone = input(
                'Ведите номер телефона (или Enter, чтобы оставить без изменений): ')
            comment = input(
                'Ведите комментарий (или Enter, чтобы оставить без изменений): ')
            pb.change(index - 1, name, phone, comment)
        case 5:
            print(pb)
            index = int(
                input('Ведите индекс контакта, который хотите удалить'))
            pb.delete(index - 1)
        case 6:
            pb.save()
        case 7:
            break
