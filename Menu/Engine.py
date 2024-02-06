import Menu.Menu as Menu
import Controller.Engine as Engine


def start():
    while True:
        Menu.draw_menu()
        user_input = input()
        if user_input == '1':
            Engine.show('all')
        elif user_input == '2':
            Engine.show('ID')
        elif user_input == '3':
            Engine.show('date')
        elif user_input == '4':
            Engine.show('all')
            Engine.change_note()
        elif user_input == '5':
            Engine.add_note()
        elif user_input == '6':
            Engine.show('all')
            Engine.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break
