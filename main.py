# monety_znalezoine = 20
# monety_magiczne = 70
# monety_ukradzione = 3
# monety = 20
#
#
# for tydzien in range (1,53):
#     monety = monety + monety_magiczne - monety_ukradzione
#     print('tydzien %s' % tydzien)
#     print('monety %s' % monety)


# l = '1,2,3,4,5,6,7,8,9,'
# for l in letters:
#     print(l)
countdown = 10

while countdown > 0:
    print ('CountDown = ', countdown)
    countdown = countdown - 1

print("LAUNCH!")

#----------------------------------------------------------
# for x in range (2,16,2):
#     print(x)
# print("You are 14!")

sandwitch = ["salad","papryka","tomato","ogurek","banan"]
number = 1
for x in sandwitch:
    print("%s,%s" % (number, x))
    number = number+1

#-----------------------------------------------------------

weight = 50
for i in range (1,16):
    weight = weight + 1
    moonweight = weight * 0.165
    print(moonweight)