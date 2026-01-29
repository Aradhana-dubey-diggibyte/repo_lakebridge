from lakebridge_recon_dab import compute


def test_compute():
    assert compute(["a", "bc", "abc"]) == "abc"
