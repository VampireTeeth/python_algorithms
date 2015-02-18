
def fib(init, k):
    if len(init) > k: return
    print ' '.join([str(i) for i in init])
    fib([1] + [init[i-1] + init[i] for i in range(len(init)) if i > 0 and i < len(init)] + [1], k)

def main():
    user_input = raw_input()
    try:
        k = int(user_input)
    except:
        print 'Invalid user input'
        return
    if k < 2 or k > 10:
        print 'K needs to be between 2 and 10'
        return
    fib([1], k)


if __name__ == '__main__':
    main()

