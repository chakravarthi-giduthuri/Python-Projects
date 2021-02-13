import pickle
import os
import pathlib


class Account:
	def __init__(self):
		self.accNo: 0
		self.name:''
		self.deposit:0
		self.type=''

	def createAccount(self):
		self.accNo=int(input('enter the account number: '))
		self.name = input('enter account holder name : ')
		self.type = input('enter the type of the account : ')
		self.deposit =  int(input('enter the initial amount >=5000 for current'))
		print('\n\n\nAccount Created')

	# def showAccount(self):
	# 	print('Account number:',self.accNo)
	# 	print('Account holder name: ',self.name)
	# 	print('Type of Account: ',self.type)
	# 	print('Balance: ',self.deposit)

	# def modifyAccount(self):
	# 	print('Account number : ',self.accNo)
	# 	self.name = input('modify account holder name : ')
	# 	self.type = input('modify the type of the account : ')
	# 	self.deposit =  int(input('modify Balance'))

	# def depositAmount(self,amount):
	# 	self.deposit+=amount

	# def withdrawAmount(self,amount):
	# 	self.deposit-=amount

	# def report(self):
	# 	print(self.accNo,' ',self.name,' ',self.type,' ',self.deposit)

	# def getAccountno(self):
	# 	return self.accNo

	# def getAccountholderName(self):
	# 	return self.name

	# def getAccountType(self):
	# 	return self.type

	# def getDeposit(self):
	# 	return self.deposit


def intro():
	print('**************')
	print('**** BANK MANAGEMENT ****')
	print('**************')

def writeAccount():
	account = Account()
	account.createAccount()
	writeAccountsFile(account)

def displayAll():
	file = pathlib.Path('accounts.data')

	if file.exists():
		infile = open('accounts.data','rb')
		mylist = pickle.load(infile)

		for item in mylist:
			print(item.accNo,' ',item.name,' ',item.type,' ',item.deposit)
		infile.close()
	else:
	  print('no records to display')


def displaySp(num):
	file = pathlib.Path('accounts.data')

	if file.exists():
			infile = open('accounts.data','rb')
			mylist = pickle.load(infile)
			infile.close()
			found = False

			for item in mylist:
				if item.accNo == num:
					print('your account balance is = ',item.deposit)

					found =True
	else:
			print('no record found')

	if not found:
			print('no existing records with this number')


def depostAndwithdraw(num1,num2):
		file = pathlib.Path('accounts.data')

		if file.exists():
			infile = open('accounts.data','rb')
			mylist = pickle.load(infile)
			infile.close()

			os.remove('accounts.data')

			for item in mylist:
				if item.accNo == num1:
					if num2 == 1:
						amount = int(input('enter the amount to deposit : '))
						item.deposit += amount
						print('your account is updated')

					if num2 ==2:
						amount = int(input('enter the amount to withdarw'))
						if amount<=item.deposit:
								item.deposit -= amount
						else:
							print('you cannot withdarw larger ammount')
		else:
		  print('no records to search')

		outfile = open('newaccounts.data','wb')
		pickle.dump(mylist,outfile)
		outfile.close()

		os.rename('newaccounts.data','accounts.data')


def deleteAccount(num):
		file = pathlib.Path('accounts.data')

		if file.exists():
			infile = open('accounts.data','rb')
			oldlist = pickle.load(infile)
			infile.close()

			newlist =[]
			for item in oldlist:
				if item.accNo!= num:
					newlist.apppend(item)
			os.remove('accounts.data')
			outfile = open('newaccounts.data','wb')
			pickle.dump(newlist,outfile)
			outfile.close()
			os.rename('newaccounts.data','accounts.data')


def modifyAccount(num):
		file = pathlib.Path('accounts.data')

		if file.exists():
			infile = open('accounts.data','rb')
			oldlist = pickle.load(infile)
			infile.close()

			os.remove('accounts.data')

			for item in oldlist:
				if item.accNo == num:
					item.name = input('enter the Account holder name: ')
					item.type = input('enter the account type: ')
					item.deposit = int(input('enter the amount: '))

			outfile = open('newaccounts.data','wb')
			pickle.dump(oldlist,outfile)
			outfile.close()
			os.rename('newaccounts.data','accounts.data')


def writeAccountsFile(account):
		file = pathlib.Path('accounts.data')

		if file.exists():
			infile = open('accounts.data','rb')
			oldlist = pickle.load(infile)
			oldlist.append(account)
			infile.close()
			os.remove('accounts.data')

		else:
			oldlist = [account]

		outfile = open('newaccounts.data','wb')
		pickle.dump(oldlist,outfile)
		outfile.close()
		os.rename('newaccounts.data','accounts.data')


ch = ''
num = 0
intro()
while ch!=8:

		print('\tMAIN MENU')
		print('\t1. NEW ACCOUNT')
		print('\t2. DEPOSIT AMOUNT')
		print('\t3. WITHDRAW AMOUNT')
		print('\t4. BALANCE ENQUIRY')
		print('\t5. ALL ACCOUNT HOLDER LIST')
		print('\t6. CLOSE AN ACCOUNT')
		print('\t7. MODIFY AN ACCOUNT')
		print('\t8. EXIT')
		print('\tSelect your option (1-8)')
		ch = input()

		

		if ch =="1":
			writeAccount()
		elif ch =="2":
			num = int(input('\t Enter your account no: '))
			depostAndwithdraw(num,1)
		elif ch =="3":
			num = int(input('\t Enter your account no: '))
			depostAndwithdraw(num,2)
		elif ch =='4':
			num = int(input('\t Enter your account no: '))
			displaySp(num)
		elif ch == '5':
			displayAll()
		elif ch == '6':
			num = int(input('\t Enter your account no: '))
			deleteAccount(num)
		elif ch == '7':
			num = int(input('\t Enter your account no: '))
			modifyAccount(num)
		elif ch == '8':
			print('thanks for using bank MANAGEMENT system')	 
			break  
		else:
			print('invalid choice')

		ch = input('enter your choice: ')


















