cars_ = ["BMW", "MB", "LADA", "KIA", "HONDA"]
T = 'я езжу на автомобиле марки '
cars_count = 0
for i in range(len(cars_)):
    print(T + cars_[i])
    cars_count += 10
    pass
print('вот', cars_count)