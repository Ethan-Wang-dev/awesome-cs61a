test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> global_frame = create_global_frame()
          >>> global_frame.define("x", 3)
          >>> global_frame.parent is None
          d4dc88cbd250e1e387bfd72d47f43ffd
          # locked
          >>> global_frame.lookup("x")
          71373a588b7d2da6b021a6a9cb2a416f
          # locked
          >>> global_frame.define("x", 2)
          >>> global_frame.lookup("x")
          725437f086fad00d39b3b3621cfe9fef
          # locked
          >>> global_frame.lookup("foo")
          487e5d855a4749c37e82d995b26091f7
          # locked
          # choice: None
          # choice: SchemeError
          # choice: 3
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> second_frame.parent == first_frame
          d4dc88cbd250e1e387bfd72d47f43ffd
          # locked
          >>> second_frame.define("y", False)
          >>> second_frame.lookup("x")
          71373a588b7d2da6b021a6a9cb2a416f
          # locked
          >>> second_frame.lookup("y")
          eb46eb687223c688890be91ff6e2b9b4
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 3)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(third_frame)
          >>> fourth_frame.lookup("x")
          3
          >>> second_frame.define("y", 1)
          >>> fourth_frame.lookup("y")
          1
          >>> first_frame.define("y", 0)
          >>> fourth_frame.lookup("y")
          1
          >>> fourth_frame.define("y", 2)
          >>> fourth_frame.lookup("y")
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> first_frame = create_global_frame()
          >>> first_frame.define("x", 1)
          >>> second_frame = Frame(first_frame)
          >>> third_frame = Frame(second_frame)
          >>> fourth_frame = Frame(first_frame)
          >>> fifth_frame = Frame(fourth_frame)
          >>> fifth_frame.lookup("x")
          1
          >>> third_frame.lookup("x")
          1
          >>> second_frame.define("x", 2)
          >>> third_frame.lookup("x")
          2
          >>> fifth_frame.lookup("x")
          1
          >>> fifth_frame.define("x", 5)
          >>> fifth_frame.lookup("x")
          5
          >>> fourth_frame.lookup("x")
          1
          >>> first_frame.define("x", 4)
          >>> fourth_frame.lookup("x")
          4
          >>> third_frame.lookup("x")
          2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> +
          #[+]
          scm> display
          #[display]
          scm> hello
          SchemeError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
