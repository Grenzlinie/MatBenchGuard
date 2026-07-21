import math, json, csv

class Compute:
    def __init__(self):
        # Parameters matching the paper's channel simulation example
        self.K = 4.0
        self.gamma = 8.0
        self.alpha = 5.0   # base α₄ used for drag and active free velocity
        self.r_core = 0.2
        self.r_max = 1.0   # used for drag and active free
        self.d = 2.0       # channel width
        self.zeta = 1.0    # activity coefficient

    def drag_coefficient(self, k, alpha):
        """
        Compute D₁ (k=+0.5) or D₁′ (k=−0.5) from Eq. (33)/(35).
        Uses the small‑g expansion (γ₁/α₄ ≪ 1).
        """
        gamma = self.gamma
        rmax = self.r_max
        rcore = self.r_core
        log_ratio = math.log(rmax / rcore)
        # first term
        term1 = (math.pi * gamma / 4.0) * log_ratio
        # correction factor
        factor = (math.pi * math.pow(gamma, 1.5)) / (math.pow(2, 3.5) * math.sqrt(alpha))
        if abs(k - 0.5) < 1e-9:      # +1/2
            bracket = log_ratio**2 + log_ratio - 2.5
        elif abs(k + 0.5) < 1e-9:    # −1/2
            bracket = log_ratio**2 - 7*log_ratio + 5.5
        else:
            raise ValueError(f"Unsupported defect charge {k}")
        return term1 - factor * bracket

    def write_analytic_drag(self):
        D1 = self.drag_coefficient(0.5, self.alpha)
        D1_prime = self.drag_coefficient(-0.5, self.alpha)
        result = {"D1": D1, "D1_prime": D1_prime}
        with open("/app/outputs/analytic_drag_coefficients.json", "w") as f:
            json.dump(result, f, indent=2)

    def write_channel_velocities(self):
        # α₄ values to scan (same as used in check)
        alpha_list = [1.0, 2.0, 5.0, 10.0]
        K = self.K
        d = self.d
        # In the channel, the system‑size cutoff is half the width
        rmax_ch = d / 2.0
        # Temporarily override r_max for the drag calculation
        saved_rmax = self.r_max
        self.r_max = rmax_ch
        with open("/app/outputs/channel_velocities.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["alpha4", "u_plus_half", "u_minus_half"])
            for alpha in alpha_list:
                D1 = self.drag_coefficient(0.5, alpha)
                D1_prime = self.drag_coefficient(-0.5, alpha)
                # Force balance: elastic force f = π²K/(2d) balances drag D*u.
                u_plus = (math.pi**2 * K) / (2.0 * d * D1)
                u_minus = (math.pi**2 * K) / (2.0 * d * D1_prime)
                writer.writerow([alpha, u_plus, u_minus])
        self.r_max = saved_rmax

    def write_active_free_velocity(self):
        # Active driving coefficient D₅ from Eq. (64)
        D5 = (math.pi * self.zeta * math.sqrt(self.gamma) * self.r_max) / (3.0 * math.sqrt(2.0 * self.alpha))
        D1 = self.drag_coefficient(0.5, self.alpha)
        # Free motion speed (magnitude of −D₅/D₁)
        u_free = abs(-D5 / D1)   # negative sign returns direction; speed is positive
        result = {"u_free": u_free}
        with open("/app/outputs/active_free_velocity.json", "w") as f:
            json.dump(result, f, indent=2)
