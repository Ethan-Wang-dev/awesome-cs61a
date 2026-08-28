test = {
  'name': 'Problem 8',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'c1637d7df9f040dc0b1cd3b7d43616a9',
          'choices': [
            'No, I will go do them right now',
            'Yes!'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Did you complete all the unlocking tests for each subpart?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Abstraction tests
          >>> original = ContainerAnt.__init__
          >>> ContainerAnt.__init__ = lambda self, health: print("init") #If this errors, you are not calling the parent constructor correctly.
          >>> protector = ProtectorAnt()
          init
          >>> ContainerAnt.__init__ = original
          >>> protector = ProtectorAnt()
          >>> hasattr(protector, 'ant_contained')
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> protector = ProtectorAnt()
          >>> protector.action(gamestate) # Action without contained ant should not error
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing protector performs thrower's action
          >>> protector = ProtectorAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place protector before thrower
          >>> gamestate.places["tunnel_0_0"].add_insect(protector)
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee)
          >>> protector.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing protector performs thrower's action
          >>> protector = ProtectorAnt()
          >>> thrower = ThrowerAnt()
          >>> bee = Bee(2)
          >>> # Place thrower before protector
          >>> gamestate.places["tunnel_0_0"].add_insect(thrower)
          >>> gamestate.places["tunnel_0_0"].add_insect(protector)
          >>> gamestate.places["tunnel_0_3"].add_insect(bee)
          >>> protector.action(gamestate)
          >>> bee.health
          1
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing removing a protector doesn't remove contained ant
          >>> place = gamestate.places['tunnel_0_0']
          >>> protector = ProtectorAnt()
          >>> test_ant = Ant(1)
          >>> # add protector first
          >>> place.add_insect(protector)
          >>> place.add_insect(test_ant)
          >>> gamestate.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          >>> protector.place is None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing removing a protector doesn't remove contained ant
          >>> place = gamestate.places['tunnel_0_0']
          >>> protector = ProtectorAnt()
          >>> test_ant = Ant(1)
          >>> # add ant first
          >>> place.add_insect(test_ant)
          >>> place.add_insect(protector)
          >>> gamestate.remove_ant('tunnel_0_0')
          >>> place.ant is test_ant
          True
          >>> protector.place is None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing protectored ant keeps instance attributes
          >>> test_ant = Ant()
          >>> def new_action(gamestate):
          ...     test_ant.health += 9000
          >>> test_ant.action = new_action
          >>> place = gamestate.places['tunnel_0_0']
          >>> protector = ProtectorAnt()
          >>> place.add_insect(test_ant)
          >>> place.add_insect(protector)
          >>> place.ant.action(gamestate)
          >>> place.ant.ant_contained.health
          9001
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing single ProtectorAnt cannot hold two other ants
          >>> protector = ProtectorAnt()
          >>> first_ant = ThrowerAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(protector)
          >>> place.add_insect(first_ant)
          >>> second_ant = ThrowerAnt()
          >>> place.add_insect(second_ant)
          Traceback (most recent call last):
          ...
          AssertionError: Too many ants in tunnel_0_0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ProtectorAnt cannot hold another ProtectorAnt
          >>> protector1 = ProtectorAnt()
          >>> protector2 = ProtectorAnt()
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(protector1)
          >>> place.add_insect(protector2)
          Traceback (most recent call last):
          ...
          AssertionError: Too many ants in tunnel_0_0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # Testing ProtectorAnt takes all the damage
          >>> thrower = ThrowerAnt()
          >>> protector = ProtectorAnt()
          >>> bee = Bee(1)
          >>> place = gamestate.places['tunnel_0_0']
          >>> place.add_insect(thrower)
          >>> place.add_insect(protector)
          >>> place.add_insect(bee)
          >>> protector.health
          2
          >>> bee.action(gamestate)
          >>> (protector.health, thrower.health)
          (1, 1)
          >>> bee.action(gamestate)
          >>> (protector.health, thrower.health)
          (0, 1)
          >>> protector.place is None
          True
          >>> place.ant is thrower
          True
          >>> bee.action(gamestate)
          >>> thrower.health
          0
          >>> place.ant is None
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> # test proper call to death callback
          >>> original_zero_health_callback = Insect.zero_health_callback
          >>> Insect.zero_health_callback = lambda x: print("insect died")
          >>> place = gamestate.places["tunnel_0_0"]
          >>> bee = Bee(3)
          >>> protector = ProtectorAnt()
          >>> ant = ThrowerAnt()
          >>> place.add_insect(bee)
          >>> place.add_insect(ant)
          >>> place.add_insect(protector)
          >>> bee.action(gamestate)
          >>> bee.action(gamestate)
          insect died
          >>> bee.action(gamestate) # if you fail this test you probably didn't correctly call Ant.reduce_health or Insect.reduce_health
          insect died
          >>> Insect.zero_health_callback = original_zero_health_callback
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> beehive, layout = Hive(AssaultPlan()), dry_layout
      >>> gamestate = GameState(beehive, ant_types(), layout, (1, 9))
      >>> #
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> from ants import *
          >>> ProtectorAnt.implemented
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
