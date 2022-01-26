
while True:
    try:
        age = int(input('what is your age: '))
        print(age)
        raise Exception('fk u')
    except ValueError:
        print('please enter a number Bitch')
        continue
    except ZeroDivisionError:
        print('No 0 allowed bitch')
        break
    else:
        break
    finally:
        print('Thank you... Bitch')

# def sum(n1,n2):
#     try:
#         return n1+n2
#     except (TypeError, ZeroDivisionError )as err:
#         print(f'only numbers: {err}')

# print(sum(1,'j'))