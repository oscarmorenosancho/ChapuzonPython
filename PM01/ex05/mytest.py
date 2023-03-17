from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    ac1 = Account(
        'Smith Jane',
        zip='911-745',
        addr = 'towers',
        unpair = '',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    ac2 = Account(
        'Smith Joe',
        zip='911-745',
        addr = 'towers',
        unpair = '',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )
    print (ac1.__dict__)
    print (bank.check_account_corrupt(ac1))