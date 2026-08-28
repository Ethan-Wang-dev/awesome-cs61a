test = {
  'name': 'dog_movies',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from dog_movies;
          Back to the Future Part III|Buford 'Mad Dog' Tannen
          Boyz n the Hood|Mad Dog
          Toy Story|Slinky Dog
          As Good as It Gets|Supporting Dog
          Toy Story 2|Slinky Dog
          Ghost Dog: The Way of the Samurai|Ghost Dog
          The Revenant|Elk Dog
          The Raid: Redemption|Mad Dog
          Everything Everywhere All at Once|Debbie the Dog Mom
          The Mitchells vs. the Machines|Dog Cop
          The Mitchells vs. the Machines|Talking Dog
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
