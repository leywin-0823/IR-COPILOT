from app.attack.rules import map_attack_techniques

def test_bruteforce_mapping():
    events = [
        {"event_id": "1", "action": "failed_login"},
        {"event_id": "2", "action": "failed_login"},
        {"event_id": "3", "action": "failed_login"},
    ]

    hits = map_attack_techniques(events)

    assert len(hits) == 1
    assert hits[0].technique_id == "T1110"
    assert hits[0].source == "rule"
    assert hits[0].confidence >= 0.8
