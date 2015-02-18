
def main():
    user_input = raw_input() 
    try:
        n = int(user_input)
    except:
        print "Please input a valid integer"
        return
    for i in range(n):
        num = i + 1
        if num % 5 == 0 and num % 3 == 0: 
            print 'FizzBuzz'
        elif num % 5 == 0: 
            print 'Buzz'
        elif num % 3 == 0: 
            print 'Fizz'
        else: 
            print num


if __name__ == '__main__':
    main()

