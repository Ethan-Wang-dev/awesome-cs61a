test = {
  'name': 'leads',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from leads;
          Brad Pitt|12
          Tom Cruise|12
          Robert De Niro|12
          Johnny Depp|12
          Leonardo DiCaprio|13
          Tom Hanks|18
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read imdb1000.sql
      sqlite> .read lab11.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
