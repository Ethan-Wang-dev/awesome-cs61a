test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> formals = Link('a', Link('b', Link('c', nil)))
          >>> vals = Link(1, Link(2, Link(3, nil)))
          >>> frame = global_frame.make_child_frame(formals, vals)
          >>> global_frame.lookup('a') # Type SchemeError if you think this errors
          487e5d855a4749c37e82d995b26091f7
          # locked
          >>> frame.lookup('a')        # Type SchemeError if you think this errors
          e9c72ee24bf5f0040e3f510cd1634fbe
          # locked
          >>> frame.lookup('b')        # Type SchemeError if you think this errors
          725437f086fad00d39b3b3621cfe9fef
          # locked
          >>> frame.lookup('c')        # Type SchemeError if you think this errors
          71373a588b7d2da6b021a6a9cb2a416f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> frame = global_frame.make_child_frame(nil, nil)
          >>> frame.parent is global_frame
          d4dc88cbd250e1e387bfd72d47f43ffd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first = Frame(global_frame)
          >>> second = first.make_child_frame(nil, nil)
          >>> second.parent is first
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # More argument values than formal parameters
          >>> global_frame.make_child_frame(Link('a', nil), Link(1, Link(2, Link(3, nil))))
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # More formal parameters than argument values
          >>> global_frame.make_child_frame(Link('a', Link('b', Link('c', nil))), Link(1, nil))
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Values can be pairs.
          >>> formals = Link('a', Link('b', nil))
          >>> values = Link(Link(1, nil), Link(Link(2, nil), nil))
          >>> frame = global_frame.make_child_frame(formals, values)
          >>> frame.lookup('a')
          Link(1)
          >>> frame.lookup('b')
          Link(2)
          >>> frame2 = frame.make_child_frame(nil, nil) # Bind parents correctly
          >>> frame2.lookup('a')
          Link(1)
          >>> formals # Ensure that formals was not mutated
          Link('a', Link('b'))
          >>> values # Ensure that values was not mutated
          Link(Link(1), Link(Link(2)))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      >>> global_frame = create_global_frame()
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
