def calc_all(*args, operation="sum"):
    """
    Вычисляет сумму или произведение всех переданных чисел.
    
    Параметры:
    *args - произвольное количество чисел
    operation - "sum" для суммы, "mul" для произведения
    
    Возвращает:
    Результат вычисления или None, если чисел нет
    """
    if not args: 
        return None
    
    if operation == "sum":
        result = 0
        for num in args:
            result += num
        return result
    elif operation == "mul":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return None  

if __name__ == "__main__":
    print(calc_all(1, 2, 3, operation="sum"))  
    print(calc_all(2, 3, 4, operation="mul"))  
    print(calc_all(5, operation="sum"))        
    print(calc_all())                          
    print(calc_all(10, 20, operation="sum"))  
