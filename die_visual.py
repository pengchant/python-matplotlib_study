from die import Die
import pygal

die_1 = Die() 
die_2 = Die(10)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_size + die_2.num_size
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()  
hist.title = "Results of rolling two D6 1000 times."
hist.x_title = "Result"
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual_3.svg')