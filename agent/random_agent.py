class SmartAgent:
    def select_action(self, state):
        agent_x, agent_y = state["agent_position"]
        deliveries = state["deliveries_left"]

        if not deliveries:
            return 0

        target = deliveries[0]  # pick first delivery

        dx = target[0] - agent_x
        dy = target[1] - agent_y

        if abs(dx) > abs(dy):
            return 1 if dx > 0 else 0
        else:
            return 3 if dy > 0 else 2