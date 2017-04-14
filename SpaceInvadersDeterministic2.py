

import gym
env = gym.make('SpaceInvadersDeterministic-v3')
for i_episode in range(120):
    observation = env.reset()
    for t in range(10000):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
            
#Box and Discrete are the most normal environments 
print(env.action_space)
print(env.observation_space)
