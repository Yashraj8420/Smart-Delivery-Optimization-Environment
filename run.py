import os
print(os.getcwd())

from env.delivery_env import DeliveryEnv

print(DeliveryEnv)
print(DeliveryEnv.__module__)
    
from env.delivery_env import DeliveryEnv
from agent.random_agent import SmartAgent

env = DeliveryEnv(grid_size=5, num_deliveries=3)
agent = SmartAgent()

state = env.reset()

total_reward = 0 

for step in range(50):
    action = agent.select_action(state)
    state, reward, done = env.step(action)

    total_reward += reward

    print(f"Step: {step}")
    env.render()

    if done:
        print("All deliveries completed!")
        break

print("Total Reward:", total_reward)
print(dir(env))