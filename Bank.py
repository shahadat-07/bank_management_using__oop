from Users import User

class Bank:
    class Admin:
        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.is_logged_in = False
            self.is_loan_available = True
        
        def login(self, username, password):
            if username == self.username and password == self.password:
                self.is_logged_in = True
                print("Admin Log In Successful")
                return True
            else:
                print("Invalid Credential")
                return False
        
        def logout(self):
            self.is_logged_in = False
            print(f"Admin logged out successfully")

        def loan_request_off(self):
            self.is_loan_available = False

        def loan_request_on(self):
            self.is_loan_available = True
        
        def total_available_balance(self, users):
           if self.is_logged_in == True:
                total_balance = 0
                for user in users:
                    total_balance += user.check_balance()
                print(f'The available balance of the Bank is:  {total_balance}')
           else:
               print("Admin needs to log in")

        def do_loan_request(self, bank, amount, user):
            if self.is_loan_available == True:
                if amount < user.check_balance()*2:
                    print(f'{user.name}, Your request is valid. Request processing...')
                    user.add_loan(amount)
                    user.deposit(bank, amount)
                    bank.total_bank_amount -= amount
                    print(f'Here is your loan {amount}')
                    return True
                else:
                    print('Loan request are not valid as per banks law')
                    return False
            else:
                print("Loan feature is not available now. Contact later")
            
        def total_loan(self, users):
           if self.is_logged_in == True:
                total_loan = 0
                for user in users:
                    total_loan += user.check_loan()
                print(f'Total bank loan is:  {total_loan}')
           else:
               print("Admin needs to log in")

        # -------------------- Admin Features are Done --------------------


    def __init__(self, name, address, email) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.users = {}
        self.Local_Admin = None
        self.total_bank_amount = 0
    
    def create_account(self, name, address, email, amount):
        user = User(name, address, email, amount)
        self.users[name] = user
        print("Account Created Successfully")

    def total_available_balance(self):
        total = 0
        for user in self.users:
            total += user.check_balance()
            return total

    def get_user(self, name):
        if name in self.users:
            return self.users[name]
        else:
            print("User not found!")

    def get_users(self):
        return list(self.users.values())
    

    # ------------------ Admin Facilities --------------------

    def create_admin(self, username, password):
        admin = Bank.Admin(username, password)
        self.Local_Admin = admin
        print("Admin created successfully")

    def admin_login(self, username, password):
        self.Local_Admin.login(username, password)

    def admin_logout(self):
        self.Local_Admin.logout()
