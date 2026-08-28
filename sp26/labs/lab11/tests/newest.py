test = {
  'name': 'newest',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from newest;
          KPop Demon Hunters|2025
          F1: The Movie|2025
          Weapons|2025
          How to Train Your Dragon|2025
          One Battle After Another|2025
          Sinners|2025
          Furiosa: A Mad Max Saga|2024
          Wicked|2024
          I'm Still Here|2024
          Dune: Part Two|2024
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
