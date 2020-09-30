def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2!=0 or heads==0 or heads>legs:
        print(error_msg)
    else:
        rabbit_count=int((legs-(2*heads))/2)
        chicken_count=int(heads-rabbit_count)
        print(chicken_count,rabbit_count)
solve(35,94)