test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sus_strategy(31, 21, threshold=10, num_rolls=2)
          62a329e8634e8fe7dd0b7f2080aba699
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(30, 41, threshold=10, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(53, 60, threshold=14, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(53, 60, threshold=15, num_rolls=2)
          62a329e8634e8fe7dd0b7f2080aba699
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(23, 54, threshold=4, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(14, 21, threshold=8, num_rolls=2)
          62a329e8634e8fe7dd0b7f2080aba699
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> sus_strategy(14, 21, threshold=12, num_rolls=5)
          e18fd36a3682a2e4f9f9c5eb315ddb8a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> s = 0
          >>> while s < 100:
          ...     if sus_update(0, 20, s) - 20 >= 10:
          ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert sus_strategy(20, s, threshold=10, num_rolls=3) == 3
          ...     s += 1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
