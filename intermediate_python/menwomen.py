from matplotlib import pyplot

data = open("life_expectancies_usa.txt", "r").readlines()

dates = []
male_life = []
female_life = []

for line in data:
	date, male_l, female_l = line.split(",")
	dates.append(date)
	male_life.append(male_l)
	female_life.append(female_l)


pyplot.plot(dates,male_life,"bo-",label="Men")
pyplot.plot(dates,female_life,"mo-",lable="Women")

pyplot.legend(loc="upper left")
pyplot.title("Avg Life Expect")
pyplot.yaxis("age")
pyplot.xais("years")

pyplot.show()
