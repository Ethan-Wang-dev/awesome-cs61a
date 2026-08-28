test = {
  'name': 'Question 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> boar_brawl(21, 46)
          e9a3dddaa9988fe42dd39d1e2cb3390f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(52, 79)
          c93f67db6585f1aa98e0123a91161c40
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(0, 0)
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(0, 5)
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(5, 0)
          c93f67db6585f1aa98e0123a91161c40
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(2, 5)
          3086e969d799e68cd8468df232597f2c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(7, 2)
          383b6800a83090c27da97b04ffebb176
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(6, 10)
          15
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(16, 27)
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(39, 71)
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(72, 29)
          c4933a0dd093653b499b3bff4a4c8ec8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(82, 115) # don't assume scores are below 100
          3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(99, 121) # don't assume scores are below 100
          21
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(109, 99) # don't assume scores are below 100
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> a = boar_brawl(42, 61)
          >>> a # check that the value is being returned, not printed
          12
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> boar_brawl(727, 939)
          12
          >>> # ban str and indexing (lists)
          >>> test.check('hog.py', 'boar_brawl', ['Slice', 'List', 'ListComp', 'Index', 'Subscript', 'For'])
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      >>> import tests.construct_check as test
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
