#!/usr/bin/env python3

import pytest
from cvehound.exception import UnsupportedVersion

@pytest.mark.fast
@pytest.mark.notbackported(
    ('cve', 'branch'),
    [
        ('CVE-2019-12455', 'stable/linux-4.19.y'), # Disputed
        ('CVE-2021-4037', 'stable/linux-4.19.y'),
        ('CVE-2022-0998', 'stable/linux-5.15.y'),
        ('CVE-2022-1789', 'stable/linux-4.19.y'),
        ('CVE-2022-1789', 'stable/linux-5.4.y'),
        ('CVE-2022-3061', 'stable/linux-4.19.y'),
        ('CVE-2022-3061', 'stable/linux-5.4.y'),
        ('CVE-2023-4133', 'stable/linux-4.19.y'),
        ('CVE-2023-4133', 'stable/linux-5.4.y'),
        ('CVE-2023-4133', 'stable/linux-5.10.y'),
        ('CVE-2023-4133', 'stable/linux-5.15.y'),
        ('CVE-2023-4133', 'stable/linux-6.1.y'),
        ('CVE-2023-23005', 'stable/linux-6.1.y'),
    ]
)
def test_on_branch(hound, branch, cve):
    try:
        assert not hound.check_cve(cve), cve + ' on ' + branch
    except UnsupportedVersion:
        pytest.skip('Unsupported spatch version')
