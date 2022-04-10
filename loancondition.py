monthly_income=int(input("請輸入月薪:"))
saving_account=int(input("請輸入存款:"))
if saving_account>80000 and monthly_income>30000: 
	print('approved')
else: 
	print('disapproved')
