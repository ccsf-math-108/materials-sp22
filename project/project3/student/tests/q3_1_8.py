test = {   'name': 'q3_1_8',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> genre_and_distances.labels == ('Genre', 'Distance')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> genre_and_distances.num_rows == train_movies.num_rows\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> genre_and_distances.group('Genre').column(1).item(0) == 113\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.allclose(genre_and_distances.column('Distance'), sorted(fast_distances(test_my_features.row(0), train_my_features)))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
