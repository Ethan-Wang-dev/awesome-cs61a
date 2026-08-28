test = {
  'name': 'Understanding Eval/Apply',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '9bef332e7a4ee9e0a88f50e7c8102859',
          'choices': [
            'Call expressions and special forms',
            'Only call expressions',
            'Only special forms',
            'All expressions are represented as Links'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What types of expressions are represented as Links?'
        },
        {
          'answer': '78281c8aa60cfeb28cc419e45eded414',
          'choices': [
            'env.find(name)',
            'scheme_symbolp(expr)',
            'env.lookup(expr)',
            'scheme_forms.SPECIAL_FORMS[first](rest, env)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What expression in the body of scheme_eval finds the value of a name?'
        },
        {
          'answer': '8e2984abf58403830db140aa255877e8',
          'choices': [
            r"""
            Check if the first element in the list is a symbol and that the
            symbol is in the dictionary SPECIAL_FORMS
            """,
            'Check if the first element in the list is a symbol',
            'Check if the expression is in the dictionary SPECIAL_FORMS'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'How do we know if a given combination is a special form?'
        },
        {
          'answer': '760951e4c03e3f903a39510d6f9260cd',
          'choices': [
            'I only',
            'II only',
            'III only',
            'I and II',
            'I and III',
            'II and III',
            'I, II and III'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          What is the difference between applying builtins and applying user-defined procedures?
          (Choose all that apply)
          
          I.   User-defined procedures open a new frame; builtins do not
          II.  Builtins simply execute a predefined Python function; user-defined
               procedures must evaluate additional expressions in the body
          III. Builtins have a fixed number of arguments; user-defined procedures do not
          
          ---
          """
        },
        {
          'answer': '4b42cf68a456920260c67272f303ed1e',
          'choices': [
            'SchemeError("malformed list: (1)")',
            'SchemeError("1 is not callable")',
            'AssertionError',
            'SchemeError("unknown identifier: 1")'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What exception should be raised for the expression (1)?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
