# Python Programming
def out_square(a, b):
    sq1=a**2
    sq2=b**2

    def in_add(a, b):
        return a + b
    
    print("square of", a,"is", sq1)
    print("square of", b,"is", sq2)
    print("addition of", a,"and", b,"is",in_add(a, b))  

out_square(5, 10)
