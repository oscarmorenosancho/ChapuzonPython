# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omoreno- <omoreno-@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 16:31:38 by omoreno-          #+#    #+#              #
#    Updated: 2023/03/17 10:56:24 by omoreno-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self): self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return   True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if # it can be appended to the attribute accounts
        if not isinstance(new_account, Account):
            return False
        acc_lst = [acc for acc in self.accounts if acc.name == new_account.name]     
        if acc_lst:
            return False 
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """
        if not isinstance(origin, str):
            return False
        if not isinstance(dest, str):
            return False
        if not isinstance(amount, int) and not isinstance(amount, float):
            return False
        if amount <= 0.0:
            return False
        origin_acc_lst = [acc for acc in self.accounts if acc.name == origin]
        if (origin == dest):
            return len(origin_acc_lst) > 0
        dest_acc_lst = [acc for acc in self.accounts if acc.name == dest]
        if (len(origin_acc_lst)==0 or len(dest_acc_lst)==0):
            return False
        origin_acc = origin_acc_lst[0]
        dest_acc = dest_acc_lst[0]
        if not isinstance(origin_acc, Account):
            return False
        if self.check_account_corrupt(origin_acc):
            return False     
        if not isinstance(dest_acc, Account):
            return False
        if self.check_account_corrupt(dest_acc):
            return False
        if origin_acc.value < amount:
            return False
        origin_acc.value -= amount
        dest_acc.value += amount
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        acc_lst = [acc for acc in self.accounts if acc.name == name]
        if not acc_lst:
            return False
        acc = acc_lst[0]
        if not isinstance(acc, Account):
            return False
        if not self.check_account_corrupt(acc):
            return True
        account_attribs = dir(acc)
        b_atrs = list(filter(lambda x: x.startswith('b'), account_attribs))
        if b_atrs and len(b_atrs) > 0:
            for atr in b_atrs:
                del acc[atr]
        account_attribs = dir(acc)
        zip_atrs = list(filter(lambda x: x.startswith('zip'), account_attribs))
        if not zip_atrs:
            acc.zip = 'unknown'
        account_attribs = dir(acc)
        addr_atrs = list(filter(lambda x: x.startswith('addr'), account_attribs))
        if not addr_atrs:
            acc.addr = 'unknown'
        if not hasattr(acc, 'id'):
            acc.id = acc.ID_COUNT
            Account.ID_COUNT += 1
        if not hasattr(acc, 'value'):
            acc.id = 0.0
        if not isinstance(acc.id, int):
            acc.id = acc.ID_COUNT
            Account.ID_COUNT += 1
        if not isinstance(acc.value, int) and not isinstance(acc.value, float):
            acc.value = 0.0
        account_attribs = dir(acc)
        if len(account_attribs) % 2 == 0:
            if (hasattr(acc, 'unpair')):
                del acc.unpair
            else:
                acc.unpair = ''
        return not self.check_account_corrupt(acc)

    def check_account_corrupt(self, account) -> int:
        account_attribs = dir(account)
        # tiene un número par de atributos,
        if len(account_attribs) % 2 == 0:
            return True
        # tiene un atributo que empieza por b,
        if list(filter(lambda x: x.startswith('b'), account_attribs)):
            return True
        # no tiene ningún atributo que empieza por zip o addr,
        if not list(filter(lambda x: x.startswith('zip'), account_attribs)):
            return True
        if not list(filter(lambda x: x.startswith('addr'), account_attribs)):
            return True
        # no tiene atributos name, id o value,
        if not hasattr(account, 'name'):
            return True
        if not hasattr(account, 'id'):
            return True
        if not hasattr(account, 'value'):
            return True
        # name no es un string,
        if not isinstance(account.name, str):
            return True
        # idnoesunint,
        if not isinstance(account.id, int):
            return True
        # value no es un int o un float.
        if not isinstance(account.value, int) and not isinstance(account.value, float):
            return True
        return False