test = {   'name': 'q1_12',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> # Check your column labels and spelling\n>>> pop_by_decade.labels == ('decade', 'population')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> # The first year of the 1960's is 1960.\n>>> pop_by_decade.column(0).item(0) == 1960\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> pop_by_decade.num_rows == 6\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> pop_by_decade.column(0).item(0) == 1960\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> pop_by_decade.column(0).item(5) == 2010\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> pop_by_decade.column(1).item(1) == 3211487418\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> pop_by_decade.column(1).item(5) == 6040810517\nTrue', 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}