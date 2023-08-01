# Genetic-Algorithm
Suppose, you have a run-predictor for cricket matches and the predictor can predict the target run for batting innings. Now you need to find out the match-winning combination of batsmen for your favorite team given the average runs of different batsmen. You need to find out a combination of batsmen where the total of average runs equals exactly the runs predicted as the target score by the predictor. 
The input contains the number of batsmen available, the target run predicted by the predictor, and the names and average runs of the respective batsman. 
Assume, the predictor predicted 300 runs as the target and there are 7 batsmen in your favorite team with their corresponding average scores, you need to find out the binary combination (1 denoting batsman selected, 0 denotes batsman not selected) of those 7 batsmen in order to find the winning combination.

Your task is to use a genetic algorithm to solve this Run-Chase problem.

Task Breakdown:

a)Model the selected batsman array in a way suitable for the problem.
b)Write a fitness function. Hint: It is the sum of the total runs of the selected batsmen.
c)Write the crossover function.
d)Write the mutation function.
e)Create a population of randomly generated selected-batsman-array.
