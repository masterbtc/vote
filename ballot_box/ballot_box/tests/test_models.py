import unittest

from ballot_box.data.models import Contest, Contestant, Decision, Opinion



class TestOpinion(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        d = {u'name': u'NEEL KASHKARI',
                u'description': u'Party Preference: Republican\nBusinessman'}
        c = Contestant(d)
        self.object = Opinion(c, 1, authoritative=True)

    def test_opinion_to_json(self):
        print(self.object.to_json())
        self.object.to_json()

class TestContestant(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        d = {u'name': u'NEEL KASHKARI',
                u'description': u'Party Preference: Republican\nBusinessman'}

        self.empty = Contestant()
        self.object = Contestant(d)

    def test_contestant_empty(self):
        print(self.empty.name)
        self.assertEquals(self.empty.name, '')

    def test_contestant_name(self):
        print(self.object.name)
        self.assertEquals(self.object.name, 'NEEL KASHKARI')

    def test_contestant_to_json(self):
        print(self.object.to_json())
        self.object.to_json()


class TestContest(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        d = {
            u'contestants':
                [{u'name': u'NEEL KASHKARI', u'description': u'Party Preference: Republican\nBusinessman'},
                 {u'name': u'EDMUND G. "JERRY" BROWN',
                  u'description': u'Party Preference: Democratic\nGovernor of California'}],
            u'description': u'',
            u'tags':
                [[u'contest type', u'VOTER-NOMINATED'],
                 [u'name', u'Governor'],
                 [u'opinion type', u'vote one'],
                 [u'region', u'STATE']]}

        self.empty = Contest('ID_empty')
        self.object = Contest('ID', d)

    def test_contest_empty(self):
        self.assertEquals(self.empty.name, '')

    def test_contest_name(self):
        print(self.empty.name)
        self.assertEquals(self.object.name, 'Governor')

    def test_contest_tag(self):
        value = self.object.tag('region')
        print(value)
        self.assertEquals(value, 'STATE')

    def test_contest_contestant(self):
        print(self.object.contestants)
        self.assertIsNotNone(self.object.contestants)
        self.assertEquals(self.object.contestants[0].name, 'NEEL KASHKARI')
        self.assertEquals(self.object.contestants[1].index, 1)

    def test_contest_to_json(self):
        print(self.object.to_json())
        self.object.to_json()

    def test_contest_search(self):
        self.assertTrue(self.object.search('NEEL'))
        self.assertTrue(self.object.search('republican'))
        self.assertTrue(self.object.search('STATE'))
        self.assertTrue(self.object.search('vot'))
        self.assertTrue(self.object.search('Governor'))
        self.assertFalse(self.object.search('Governor1'))


class TestDecision(unittest.TestCase):
    def setUp(self):
        """Call before every test case."""
        c = {
            u'contestants':
                [{u'name': u'NEEL KASHKARI', u'description': u'Party Preference: Republican\nBusinessman'},
                 {u'name': u'EDMUND G. "JERRY" BROWN',
                  u'description': u'Party Preference: Democratic\nGovernor of California'}],
            u'description': u'',
            u'tags':
                [[u'contest type', u'VOTER-NOMINATED'],
                 [u'name', u'Governor'],
                 [u'opinion type', u'vote one'],
                 [u'region', u'STATE']]}

        contest = Contest('0433bd4c47055eea322517df70a95e275422ac57b0466538b8944ee23b2ffafd', c)

        d = {
               "decision_id": "b5f77b0fcd4443bd74be46b79b1f1dc646f7db15a107f1c68a89e3dc68249717",
               "contest_id": "0433bd4c47055eea322517df70a95e275422ac57b0466538b8944ee23b2ffafd",
               "ballot_id": "b7cd4d83a3f000cf5187513f9053eadec89f6c5c7ceac1214a24a6e84175f2d6",
               "write_in_names": [],
               "voter_opinions": [[0, 1]],
               "voter_id": "XTSMcFMA3yGyUaQbRmVaY4tdsZvbEaL7jd7",
               "timestamp": "2015-01-01T08:00:00",
               "authoritative": True,
               "latest": True
            }
        self.object = Decision(contest, d)
        pass

    def test_decision_to_json(self):
        print(self.object.to_json())
        self.object.to_json()


if __name__ == "__main__":
    unittest.main()