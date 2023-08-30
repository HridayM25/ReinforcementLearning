Related to Chapter 10 of the Textbook, have implemented Episodic Semi Gradient SARSA for which is an On Policy Control Method.

I have used the Discrete Mountain Car environment which is a part of OpenAI's gym. 

I have made the features as a concatenation of the observation vector given by gym along with the action value to be taken. 

For example if I want to represent taking an action to the left at observation values ([-0.4, 0.4]), the feature vector is ([-0.4, 0.4, 0]).

The step-size (alpha) and discount factor (gamma) values are mentioned in the notebook.

I have randomly initialized the weights and followed the algorithm. 

I have shown the weights at the end of 100 runs.

I have also plotted the graph of steps/episode.
