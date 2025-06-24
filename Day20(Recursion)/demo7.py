class Car:
    car_Name = "BMW"
    car_Color = "White"
    car_Price = 2000000
    car_Type = "Petrol"


obj_car = Car()
print(obj_car.car_Name)
print(obj_car.car_Color)
print(obj_car.car_Price)
print(obj_car.car_Type)

# Update values
obj_car.car_Color = "Black"
obj_car.car_Type = "Diesel"

print()
# Print after update
print(obj_car.car_Name)
print(obj_car.car_Color)
print(obj_car.car_Price)
print(obj_car.car_Type)

# print()
# print('Created a new object obj_car1')
# # Create one more object of car
# obj_car1 = Car()
# print(obj_car1.car_Name)
# print(obj_car1.car_Color)
# print(obj_car1.car_Price)
# print(obj_car1.car_Type)

print()
# delete values - we need to directly delete from class
# obj_car.car_Price accesses it, but doesn’t own it.
# del obj_car.car_Price looks for car_Price on the instance, doesn't find it, and throws error AttributeError: 'Car' object has no attribute 'car_Price', hence:
# Direct delete from class attribute
del Car.car_Price

print(obj_car.car_Name)
print(obj_car.car_Color)
print(obj_car.car_Price)
print(obj_car.car_Type)




