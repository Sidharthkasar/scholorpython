#payment.py

while True:
    print('1.payment failed')
    print('2.profile and privacy')
    print('3.money transfer')
    print('4.exit')
    user_inp=int(input('enter your choice'))
    if user_inp==1:
        print('welcome to payment faild')
    elif user_inp==2:
        print('welcome to profile and privacy')
    elif user_inp==3:
        print('welcome money trasfer')
    else:
        print('exit')
        break 