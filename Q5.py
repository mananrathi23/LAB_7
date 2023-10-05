n =str(input())
count_small =  0
count_digits=0
count_capital = 0 
count_special = 0
index =0
for i in n :
    if i.isupper():
        count_capital+=1
    elif i.islower():
        count_small+=1
    elif i.isdigit():
        count_digits+=1
    else:
        count_special+=1
print(count_small)
print(count_digits)
print(count_capital)
print(count_special)