def test_fuzz_does_not_crash(client):
    response = client.post(
        "/ai/analyze",
        json={"events": [{}]}  # malformed on purpose
    )
    assert response.status_code in (200, 422)
