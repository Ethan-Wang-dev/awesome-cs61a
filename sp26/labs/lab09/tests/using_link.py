test = {
  'name': 'using-link',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'c7fdc39a612e9c8887a26a2e08ea34c1',
          'choices': [
            "Link('+', Link('-', Link(2, Link(4, Link(6, Link(8))))))",
            "Link('+', Link(Link(-, Link(2, Link(4))), Link(6, Link(8))))",
            'Link(+, Link(Link(-, Link(2, Link(4))), Link(6, Link(8))))',
            "Link('+', Link(Link('-', Link(2, Link(4))), Link(6, Link(8))))",
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Find the Python expression that returns a `Link` representing the given expression: (+ (- 2 4) 6 8)'
        },
        {
          'answer': 'b440e2425a7fbf959b0a6ec6eb62bd64',
          'choices': [
            '-',
            '+',
            '(',
            '2',
            '6',
            'None of these'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': "What is the operator of the previous part's call expression?"
        },
        {
          'answer': 'f379e7b2c525636836e9d5c05801d4a1',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Link` you constructed in the previous part was bound to the name `p`,
          how would you retrieve the operator?
          """
        },
        {
          'answer': 'fb6d6085526139789c44f24d956e1e0b',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If the `Link` you constructed was bound to the name `p`, 
          how would you retrieve a list containing all of the operands?
          """
        },
        {
          'answer': '6062d3641c25b44c5a0575a7c37ffb2a',
          'choices': [
            'p',
            'p.first',
            'p.rest',
            'p.rest.first',
            'p.first.rest'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How would you retrieve only the first operand?'
        },
        {
          'answer': '2b2fb7e39cdf1487bec74987d5485b40',
          'choices': [
            "'-'",
            "'+'",
            '2',
            '4',
            '-2',
            "Link('-', Link(2, Link(4)))",
            'Link(2, Link(4))'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is the first operand of the call expression (+ (- 2 4) 6 8) prior to evaluation?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
