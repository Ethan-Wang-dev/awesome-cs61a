test = {
  'name': 'Question 10',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=7, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=15, num_rolls=7)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 51, threshold=16, num_rolls=7)
          bd13fb79db576dcc5054025fb0039643
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(44, 53, threshold=3, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(44, 53, threshold=4, num_rolls=2)
          62a329e8634e8fe7dd0b7f2080aba699
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 31, threshold=9, num_rolls=5)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 31, threshold=10, num_rolls=5)
          e18fd36a3682a2e4f9f9c5eb315ddb8a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 52, threshold=15, num_rolls=2)
          a66dc92bea7ccf4e90441e4a7fe5fcd8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_strategy(40, 52, threshold=16, num_rolls=2)
          62a329e8634e8fe7dd0b7f2080aba699
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
          ...     if boar_brawl(90, s) >= 10:
          ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 0
          ...     else:
          ...         assert boar_strategy(90, s, threshold=10, num_rolls=3) == 3
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
