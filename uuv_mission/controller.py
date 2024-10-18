class PDController:
    def __init__(self, KP: float, KD: float):
        self.KP = KP  # Proportional gain
        self.KD = KD  # Derivative gain
        self.prev_error = 0  # Store previous error to compute derivative term

    def compute_control(self, error: float) -> float:
        # PD control law: u[t] = KP * e[t] + KD * (e[t] - e[t-1])
        derivative = error - self.prev_error
        control_action = self.KP * error + self.KD * derivative
        self.prev_error = error  # Update previous error for the next time step
        return control_action
