test = {
  'name': 'Problem 15',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define dict '((a 1) (b 10) (c 7)))
          dict
          scm> (get dict 'a)
          1
          scm> (get dict 'b)
          10
          scm> (get dict 'c)
          7
          scm> (get dict 'd)
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define schememon '((squirrel 0) (fibo 1) (oski 2)))
          schememon
          scm> (define with-tree (set (set schememon 'tree 3) 'fibo 4))
          with-tree
          scm> with-tree
          ((squirrel 0) (fibo 4) (oski 2) (tree 3))
          scm> schememon
          ((squirrel 0) (fibo 1) (oski 2))
          scm> (get with-tree 'tree)
          3
          scm> (get schememon 'tree)
          #f
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'questions)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
