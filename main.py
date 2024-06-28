def main():

    N = int(input('Enter the number N: '))
    result = []

    for i in range(N+1):
        new_num = 2**i
        result.append(new_num)
        
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
