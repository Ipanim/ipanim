# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:06:25 2023

@author: Anim Isaac
"""


cars={'ferrari': 767886555,
'Birkin': 9086432,
'buggatti': 6875422,
' toyota prado': 12345678,
'Hyundai': 12345678,
'mitsubishi': 876542345678,
'tesla': 9876545,
'pontiac': 2345676,
'bmw': 23444540,
'opel': 34578234,
'picanto': 986449,
'matiz': 527863800,
'acura': 235789840,
'ford': 235789741,
'accord': 2478852,
'chevrolet': 247699743,
'subaru': 23468864,
'audi': 43578850,
'culvert': 7843578640,
'gmc': 68055788,
        'porsche': 7656780,
        'jaguar': 689000,
        'bentley': 56758000,
        'renault': 345678600,
        'suzuki':67685500,
        'lexus': 365657000,
        'land rover': 23457800,
        'range rover': 3467460000,
        'dodge': 23468680000,
        'ram': 3579332563,
        'range rover':3466553999}

prompt = input('Which type of car do you want to buy ? ')
if prompt in cars:
        print('Yes, we do have ' + prompt.upper() + ' available.')
        price = cars[prompt]
        print(prompt.upper() + ' the price of the car goes for rupees' + str(price))

else:
        print("We dont have that type of car,sorry" + prompt + ' inaccesssible. These are the cars we have here in our custody:')
        a = cars.keys()
        print(a)
        
        #https://github.com/Ipanim/Ipanim