from unittest import mock

import pytest

from comptia_flash import constants
from comptia_flash.__main__ import main
from comptia_flash.comptia import CompTIAData, get_comptia_data


@pytest.mark.parametrize(
    "test_input",
    [
        constants.APlusOne,
        constants.APlusTwo,
        constants.NetPlus,
        constants.SecPlus,
        constants.PenPlus,
        constants.CysaPlus,
        constants.CaspPlus,
    ],
)
def test_get_comptia_data(test_input):
    output = get_comptia_data(test_input)
    assert len(output) > 0


@pytest.mark.parametrize(
    "test_input, test_expected",
    [
        (["--comptia-test", "a1"], constants.APlusOne),
        (["--comptia-test", "a2"], constants.APlusTwo),
        (["--comptia-test", "net"], constants.NetPlus),
        (["--comptia-test", "sec"], constants.SecPlus),
        (["--comptia-test", "pen"], constants.PenPlus),
        (["--comptia-test", "cysa"], constants.CysaPlus),
        (["--comptia-test", "casp"], constants.CaspPlus),
    ],
)
@mock.patch("comptia_flash.__main__.get_comptia_data")
@mock.patch("builtins.input", lambda *args: "input")
def test_args(mock_get_comptia_data, test_input, test_expected):
    test_data = CompTIAData()
    test_data.acronym = "TTT"
    test_data.value = "time to test"
    mock_get_comptia_data.return_value = [test_data]
    main(test_input)
    mock_get_comptia_data.assert_called_with(test_expected)
