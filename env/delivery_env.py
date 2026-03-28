import random

class DeliveryEnv:
    def __init__(self, grid_size=5, num_deliveries=3):
        self.grid_size = grid_size
        self.num_deliveries = num_deliveries
        self.reset()

    def reset(self):
        # Agent starts at random position
        self.agent_pos = [random.randint(0, self.grid_size-1),
                          random.randint(0, self.grid_size-1)]

        # Random delivery locations
        self.deliveries = []
        for _ in range(self.num_deliveries):
            self.deliveries.append([
                random.randint(0, self.grid_size-1),
                random.randint(0, self.grid_size-1)
            ])

        self.done = False
        return self.state()

    def state(self):
        return {
            "agent_position": self.agent_pos,
            "deliveries_left": self.deliveries
        }

    def step(self, action):
        if self.done:
            return self.state(), 0, True

        reward = -1  # step penalty

        # Actions: 0=up, 1=down, 2=left, 3=right
        if action == 0 and self.agent_pos[0] > 0:
            self.agent_pos[0] -= 1
        elif action == 1 and self.agent_pos[0] < self.grid_size - 1:
            self.agent_pos[0] += 1
        elif action == 2 and self.agent_pos[1] > 0:
            self.agent_pos[1] -= 1
        elif action == 3 and self.agent_pos[1] < self.grid_size - 1:
            self.agent_pos[1] += 1
        else:
            reward -= 5  # invalid move penalty

        # Check if delivery completed
        if self.agent_pos in self.deliveries:
            self.deliveries.remove(self.agent_pos)
            reward += 10

        # Check if all deliveries done
        if len(self.deliveries) == 0:
            self.done = True

        return self.state(), reward, self.done
    

    def render(self):   # ✅ MUST BE HERE
        grid = [["." for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        for d in self.deliveries:
            grid[d[0]][d[1]] = "D"

        x, y = self.agent_pos
        grid[x][y] = "A"

        for row in grid:
            print(" ".join(row))
        print("\n")