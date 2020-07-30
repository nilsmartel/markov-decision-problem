# Markov Decision Problem (MDP)

Implementation of simple MDPs for reasearch in basic AI problems.

### What is an MDP?
A Markov Decision Problem is a search problem, where the outcome of an action is non deterministic.
There 2 differences in the forumulation of the problem:
- rather than assigning a `successor(s, a)` state, we define a set of `transitions(s, a, s')` probabilities, to get from `s` to `s'` using action `a`.
- rather than using a `cost(s, a)` function, we're dealing with a (possibly negative) `reward(s, a, s')`

There is another key difference:
In a search problem, one looks for a path to take from some start state to some goal state.
In an MDP one looks for a policy `π(s) -> a`, which maps every possible state to an action. Why is that useful? Now, in a traditional search problem one would never derive from ones path. In an MDP one might find himself in any possible state.

### How are MDPs useful?
Whenever the outcome of an action is unknown.
For example:
- One can not know exactly what the whether os going to look like next year. Non the less farmers have to plan how much they plan and how much they might yield.might no
