from Bank import Bank

class main():

    DBC = Bank('DBC', 'santikungo', 'amaderbank@gmail.com')

    DBC.create_account('Jhankar Mahbub', 'USA', 'jhankar@uradhura.com', 1000)
    user1 = DBC.get_user("Jhankar Mahbub")
    user1.deposit(DBC, 5000)
    print('Current Balance' ,user1.check_balance())
    user1.withdraw(DBC, 1000, True)
    print('Current Balance' ,user1.check_balance())


    DBC.create_account('Karina Islam', 'USA', 'karina@.com', 1000)
    user2 = DBC.get_user("Karina Islam")
    user2.deposit(DBC, 10000)
    print('Current Balance' ,user2.check_balance())
    user2.withdraw(DBC, 1000)
    print('Current Balance' ,user2.check_balance())
    user2.balance_transfer(1000, user1)
    print('After transer Balance' ,user2.check_balance())

    print('user1 balance', user1.check_balance())

    user1.show_transaction()
    user2.show_transaction()

    DBC.create_admin('shahadat', 'admin')
    DBC.admin_login('shahadat', 'admin')
    DBC.Local_Admin.total_available_balance(DBC.get_users())
    DBC.Local_Admin.do_loan_request(DBC, 1000, user1)
    DBC.Local_Admin.do_loan_request(DBC, 5000, user2)
    DBC.Local_Admin.total_loan(DBC.get_users())

    DBC.Local_Admin.loan_request_off()

    DBC.Local_Admin.do_loan_request(DBC, 1000, user2)

    DBC.Local_Admin.logout()
    DBC.Local_Admin.total_available_balance(DBC.get_users())


if __name__ == '__main__':
    main()