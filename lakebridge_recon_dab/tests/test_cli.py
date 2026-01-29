import subprocess


def test_main():
    assert subprocess.check_output(["lakebridge-recon-dab", "foo", "foobar"], text=True) == "foobar\n"
