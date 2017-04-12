##OpenAI gym examples and implementations
#Run basic example from Reinforced learning
#with SpaceInvaders Deterministic environment

import gym
env = gym.make('SpaceInvadersDeterministic-v3')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
