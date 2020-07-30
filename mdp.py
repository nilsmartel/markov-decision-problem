import math

gamma = 0.8

class MagicTrainProblem(object):
    def __init__(self, N, goal, goal_reward):
        self.goal_reward = goal_reward
        self.goal = goal
        self.N = N

    def get_states(self):
        return range(0, self.N-1)

    def get_actions(self, state):
        if state == self.goal:
            return []
        # list of action
        actions = []
        if state+1 < self.N:
            actions.append('walk')
        if state*2 < self.N:
            actions.append('train')
        return actions

    def is_goal(self, state):
        return self.goal == state

    def get_reward_prob_folow(self, state, action):
        # [] (Reward, probability, follow State)
        list = []
        if action == 'walk':
            if self.N+1 == self.goal:
                list.append((self.goal_reward, 1.0, self.N+1))
            else:
                list.append((-1, 1.0, self.N+1))
        if action == 'train':
            if self.N*2 == self.goal:
                list.append((self.goal_reward, 0.5, self.N*2))
            else:
                list.append((-1, 0.5, self.N*2))
            list.append((-1, 0.5, self.N))
        return list

def v(problem, state, iter):
    # I don't know, where to match this!
    if state == 0:
        return 0
    value = -math.inf
    for action in problem.get_actions(state):
        value = max(value, q(problem, state, action, iter-1))

    return value


def q(problem, state, action, iter):
    if iter == 0:
        return 0
    sum = 0
    for (r, p, s_next) in problem.get_reward_prob_folow(state, action):
        sum += p*(r + gamma* v(problem, s_next, iter))

    return sum



ITERATIONS = 100

# optimal policy
def opt_policy(problem):
    p={}
    for state in problem.get_states():
        action = None
        value = -math.inf
        for action in problem.get_actions(state):
            q_a = q(problem, state, action, ITERATIONS)
            if q_a > value:
                value = q_a
                action = action

        p[state] = action

    return p

problem = MagicTrainProblem(200, 180, 0)

policy = opt_policy(problem)

print(policy)

