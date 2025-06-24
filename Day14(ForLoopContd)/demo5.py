# fetch only doses from below list
list1 = ['masala dose','rava dose','pongal','open Dose','idly','khali dose','onion dose']

dose_list = []

for i in list1:
    if 'dose' in i.lower():
        dose_list.append(i)


print(dose_list)

# ['masala dose', 'rava dose', 'open Dose', 'khali dose', 'onion dose']


