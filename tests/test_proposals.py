from unittest import TestCase

from proposals import is_proposal_valid


class TestApi(TestCase):
    def test_is_proposal_valid(self):
        full_proposal = {
            'id': '1',
            'format': 'service-proposal/v1',
            'service_type': 'openvpn',
            'provider_id': '123',
        }

        self.assertTrue(is_proposal_valid(full_proposal))

        self.assertFalse(is_proposal_valid(self.excluded_key(full_proposal, 'id')))
        self.assertFalse(is_proposal_valid(self.excluded_key(full_proposal, 'format')))
        self.assertFalse(is_proposal_valid(self.excluded_key(full_proposal, 'service_type')))
        self.assertFalse(is_proposal_valid(self.excluded_key(full_proposal, 'provider_id')))

    def excluded_key(self, dictionary, key):
        c = dictionary.copy()
        c.pop(key)
        return c

