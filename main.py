class Kelly:
    def __init__(self, bankroll=0, position_A=None, position_B=None):
        self.bankroll = bankroll
        self.pos_A = position_A
        self.pos_B = position_B

    def calc_odds(self):
        self.odds_A = (1 - self.pos_A) / self.pos_A
        self.odds_B = (1 - self.pos_B) / self.pos_B

    def calc_edge(self, my_prob_A, my_prob_B):
        self.edge_A = my_prob_A - self.pos_A
        self.edge_B = my_prob_B - self.pos_B

    def calc_total_edge(self):
        self.total_edge = self.edge_A + self.edge_B

    def calc_allocation(self):
        self.allocation_A = self.edge_A / self.total_edge
        self.allocation_B = self.edge_B / self.total_edge

    def calc_bet(self):
        self.bet_A = self.allocation_A * self.total_edge
        self.bet_B = self.allocation_B * self.total_edge
