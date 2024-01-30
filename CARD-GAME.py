import random

output_dict={}

fees=int(input("entry fees:-"))

players=int(input("how many players:- "))


total_amount=fees*players
print("total amount in your match:-->",total_amount,"--start your game--")

company_amount=0
for i in range(0,players):
    output_dict[str(i)]=[]
    for j in range(0,2):
        random_number=random.randint(2,10)
        if random_number not in output_dict[str(i)]:
            output_dict[str(i)].append(random_number)
        else:
            random_2=random.randint(2,10)
            output_dict[str(i)].append(random_2)
    print(output_dict)
    choice=input("1.play 2.pass  :-->")
    if choice=="1":
        betting_amount=int(input("|enter your bet amount inbetween 0 to "+str(total_amount))) 
        print(betting_amount)
        first_number=output_dict[str(i)][0]
        second_number=output_dict[str(i)][1]
        card=random.randint(2,10)
        print("your card number:",card)
        if card<first_number and card>second_number:
            calculation=20/total_amount
            company_amount+=int(calculation*100)
            winning_amount=total_amount-company_amount
            print("you are winner AND your winning amount is :-",winning_amount)
        else:
            total_amount+=betting_amount
            print("better luck next time,your number is",card)
    
print("company profit:",company_amount)

