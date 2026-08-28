test = {
  'name': 'long_movies',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select decade, count from long_movies;
          1930s|1
          1950s|2
          1960s|2
          1970s|3
          1980s|2
          1990s|7
          2000s|4
          2010s|3
          2020s|4
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
