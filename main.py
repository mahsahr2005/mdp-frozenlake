from source import FrozenLake
import numpy as np
from enum import Enum as tmp
# Create an environment
max_iter_number = 100

class Actions(tmp):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
env = FrozenLake(render_mode="human", map_name="8x8")
observation, info = env.reset(seed=30)

def stateValue():
    Environment = np.zeros(env.nS)
    policy = np.zeros(env.nS, dtype=int)
    Environment[63] = 10
    g = 0.8
    for __ in  range(0,1000):
        newEnvironment = np.copy(Environment)
        for State in range(0,env.nS):
            actionValues = []
            for tmp1 in range (0,env.nA):
                qValue = 0
                for tmp2 in range (0,env.nA):
                    [_ , nextPosition , Hole , Done] = env.P[State][tmp2][0]
                    nextState = 8*nextPosition[0] + nextPosition[1]
                    if tmp1== tmp2 : Probability=1/2
                    else: Probability=1/4
                    score =-1
                    if nextState== 63: score=10
                    if Done and Hole== -1: score=-10
                    qValue+= Probability* (score+ g*Environment[nextState])
                actionValues.append(qValue)
            
            newEnvironment[State]= max(actionValues)
            policy[State] =np.argmax(actionValues)
        Environment= newEnvironment
    return Environment,policy

if __name__ == "__main__":
    V, policy = stateValue()
    current_state = env.s
    tScore = 0
    for __ in range(max_iter_number):
        action = policy[env.s]
        # Perform the action and receive feedback from the environment
        next_state, reward, done, truncated , info = env.step(action)
        tScore -=1
        if next_state[0]*8 + next_state[1] == 63 :
            print(f"total score: {tScore + 100}")
            env.close()
            break
        if done or truncated:
            tScore = 0
            observation, info = env.reset()
    env.close()
