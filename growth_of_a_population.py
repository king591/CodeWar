# In a small town the population is p0 = 1000 at the beginning of a year. \
#   The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
#
# At the end of the first year there will be:
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
#
# At the end of the 2nd year there will be:
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants \
#   (** number of inhabitants is an integer **)
#
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
#
# It will need 3 entire years.
# More generally given parameters:
#
# p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)#
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.#
# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)
#
# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10
# Note:
# Don't forget to convert the percent parameter as a percentage in the body of your function: \
#   if the parameter percent is 2 you have to convert it to 0.02.

# regular solution:
#from decimal import *
def nb_year(p0, percent, aug, P):
    years = 0
    print('detailis:{},{},{},{}'.format(p0,percent,aug,P))
    # p0 = Decimal(p0)

    while p0 < P:
        years = years + 1
        # p0 = Decimal(p0 * Decimal(1 + percent / 100) + aug)
        # the population can't be counted in ONE even if the value of population is 0.99999999999. it means 'not ONE completed person'
        p0 = int(p0 * (1 + percent / 100) + aug)
        print(p0, years, P)
        # if p0 > int(p0):
        #     p0 = int(p0) + 1
    return years

L=[1,0,3,0,0,1,0,2]
index(L)
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))
# the problem about 'ONE completed human'
print(nb_year(1000,2.0,50,1214))
