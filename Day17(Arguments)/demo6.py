# Keyword Arguments

# **kwargs → Variable-length keyword arguments (Dictionary)
# Using **kwargs (Multiple Keyword Arguments)
# ✅ Allows a function to accept any number of keyword arguments.
# ✅ Collects them into a dictionary.

def profile(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(f'key:{k},value:{v}')


profile(name='Lakshmi',age=30,salary=40000,location='KAR')

# {'name': 'Lakshmi', 'age': 30, 'salary': 40000, 'location': 'KAR'}
# key:name,value:Lakshmi
# key:age,value:30
# key:salary,value:40000
# key:location,value:KAR

print()
def info(*details,**keydetails):
    print(details)
    print(keydetails)


info('Archana',20,'Kerala',Salary=40000,Gender='Female',Id=12345)

# ('Archana', 20, 'Kerala')
# # {'Salary': 40000, 'Gender': 'Female', 'Id': 12345}

