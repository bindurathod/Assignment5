def max_of_one( x, y ):
    if x > y:
        return x
    return y
def max_of_two( x, y ):
    return max_of_one( x, max_of_one( x, y ) )
print(max_of_two(3, 6 ))
