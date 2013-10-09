text_file = open('C:\cygwin\home\Karshin\survey_multiple_choice.csv', "r")
lines = filter(None, (line.rstrip() for line in text_file))
print len(lines)

import csv
import collections

unix = collections.Counter() #defines count as unix
with open('survey_multiple_choice.csv','r') as f: #reads file
		for row in csv.reader(f, delimiter = ','):
			unix[row[2]] += 1 #counts responses in column 3
print unix.most_common() #prints frequency of each response

database = collections.Counter()
with open('survey_multiple_choice.csv','r') as f:
	for row in csv.reader(f, delimiter = ','):
		database[row[3]] +=1
print database.most_common()

programming = collections.Counter()
with open('survey_multiple_choice.csv','r') as f:
	for row in csv.reader(f, delimiter = ','):
		programming[row[4]] +=1
print programming.most_common()
print(" ")
print(" ")

print("Most frequent response")
print unix.most_common(1)
print database.most_common(1)
print programming.most_common(1)

print("The lowest discipline is databases. The highest discipline is working in a command-line terminal.")

import numpy as np
import matplotlib.pyplot as plt

n = 5
ind = np.arange(5)
width = 0.35

fig = plt.figure()
ax = fig.add_subplot(111)

unix = (5,6,21,18,2)
rects1 = ax.bar(ind, unix, width, color = 'b')
database = (17,17,10,8,0)
rects2 = ax.bar(ind+width, database, width, color = 'r')
programming = (6,21,17,8,0)
rects3 = ax.bar(ind+width*2, programming, width, color = 'g')

ax.set_ylabel('Students')
ax.set_title('Skill Level of Students in PDS')
ax.set_xticks(ind+width)
ax.set_xticklabels(('One', 'Two', 'Three', 'Four', 'Five'))
ax.legend( (rects1[0], rects2[0], rects3[0]), ('Unix', 'Databases', 'Programming') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.show()
