def squsum(*param):
    sum=0
    for i in param:
        sum+=i*i
    print(sum)
squsum(1,2,3,4)

def city_temp(**param):
    print(param)
city_temp(bj='32c',xm='23c',sh='31c')

def city_temp(**param):
        print(param)
        for c,t in param.items():
            print (c,':',t)
#city_temp(bj='32c',xm='23c',sh='31c')
a={'bj':'21','sh':'25'}
city_temp(**a)