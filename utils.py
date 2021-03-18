def create_machine_state(n=100):
    return [{'n_pulls_0': 0, 
             'n_success_0': 0, 
             'not_pull_since_last_0': 0, 
             'not_pull_since_last_1': 0,
             'n_pulls_1': 0, 
             'n_success_1': 0, 
             'my_continue': 0, 
             'op_continue': 0, 
             'self_ucb': 0, 
             'op_ucb': 0,
             'payout': None}
              for ii in range(n)]
