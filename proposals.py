REQUIRED_FIELDS = ['id', 'format', 'service_type', 'provider_id']


def is_proposal_valid(proposal):
    for required_field in REQUIRED_FIELDS:
        if required_field not in proposal:
            return False

    return True
