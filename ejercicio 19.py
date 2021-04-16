s = int(input("escribe la cantidad de segundos: "))

h = s // (60 * 60)
s = s % (60*60)
m = s // 60
s = s % 60

print("{} : {} : {}".format(h,m,s))