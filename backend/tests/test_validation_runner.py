from app.validation.runner import run_validation


def test_validation_datasets_pass():
    results = run_validation()

    failures = [r for r in results if not r["passed"]]
    assert not failures
