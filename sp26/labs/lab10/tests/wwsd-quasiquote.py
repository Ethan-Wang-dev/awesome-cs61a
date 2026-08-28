test = {
  'name': 'wwsd-quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          9361113117cbf04a77ec19756fb23ed5
          # locked
          scm> (define x 2)
          adfa7f54c8ad7613f4804096e85be4da
          # locked
          scm> `(1 x 3)
          9361113117cbf04a77ec19756fb23ed5
          # locked
          scm> `(1 ,x 3)
          5aa726f3ee5e32f3b1aaf920885bb5df
          # locked
          scm> `(1 x ,3)
          9361113117cbf04a77ec19756fb23ed5
          # locked
          scm> `(1 (,x) 3)
          4bcb7537b268198696b1f28355a012a6
          # locked
          scm> `(1 ,(+ x 2) 3)
          25ce38d7ddca5d758275c538ca626873
          # locked
          scm> (define y 3)
          612417f3d036b486fb3efc75ae7d405e
          # locked
          scm> `(x ,(* y x) y)
          f2e02f7744981f74c682a76f30d8e3d2
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          5cfeefea45ed5af3861adddcf1e8d238
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
