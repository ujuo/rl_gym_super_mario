import gym
import gym_pull
import super_mario_bros

from wrappers import ProcessFrame84,MarioActionSpaceWrapper
#gym_pull.pull('github.com/ppaquette/gym-super-mario') 
env = gym.make('ppaquette/meta-SuperMarioBros-v0')
print(env.observation_space,env.action_space)
env = MarioActionSpaceWrapper(env)
print(env.observation_space,env.action_space)
env = ProcessFrame84(env)
print(env.observation_space,env.action_space)

env.reset()