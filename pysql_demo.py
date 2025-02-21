import sys
import pysql_impl_service_class as psc

class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def match_user_choice(self, choice, service):
        match choice:
            case '1' : 
                service.oprs.create_table()
            case '2' : 
                service.oprs.insert_row()
            case '3' :
                service.oprs.delete_row()
            case '4' :
                service.oprs.update_row()
            case '5' :
                service.oprs.display_table()
            case '6' :
                service.oprs.delete_table()
            case '7' :
                service.oprs.search()
            case '8' :
                self.end_of_program()
            case _ :
                self.invalid_choice()

    def run_menu(self):
        service = psc.Table_service()
        while True:
            print("\n----- MENU -----")
            print("1. Create Table")
            print("2. Insert Row")
            print("3. Delete Row")
            print("4. Update Row")
            print("5. Display Table")
            print("6. Delete Table")
            print("7. Search")
            print("8. Exit")
            
            choice = (input("\nEnter choice: "))
            self.match_user_choice(choice, service)

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()