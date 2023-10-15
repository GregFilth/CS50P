from project import get_command, get_name, get_number, Fridge
from unittest import mock
from termcolor import colored
import pytest


@mock.patch("builtins.print")
def test_getname(mock_print):
    with mock.patch("builtins.input", return_value="honey chicken"):
        assert get_name("", test_running=True) == "honey chicken".upper()

    with mock.patch("builtins.input", return_value="1"):
        get_name("", test_running=True)
        mock_print.assert_called_with(colored("You can only input letters.", "red"))

    with mock.patch("builtins.input", return_value="a1"):
        get_name("", test_running=True)
        mock_print.assert_called_with(colored("You can only input letters.", "red"))

    with mock.patch("builtins.input", return_value="a-"):
        get_name("", test_running=True)
        mock_print.assert_called_with(colored("You can only input letters.", "red"))

    with mock.patch("builtins.input", return_value=""):
        get_name("", test_running=True)
        mock_print.assert_called_with(colored("Please enter a valid name.", "red"))


@mock.patch("builtins.print")
def test_getnumber(mock_print):
    with mock.patch("builtins.input", return_value="1"):
        assert get_number("") == "1"

    with mock.patch("builtins.input", return_value="-1"):
        assert get_number("") == "-1"

    with mock.patch("builtins.input", return_value="+1"):
        assert get_number("") == "+1"

    with mock.patch("builtins.input", return_value="0"):
        assert get_number("") == "0"

    with mock.patch("builtins.input", return_value="1.5"):
        assert get_number("") == "1.5"

    with mock.patch("builtins.input", return_value="-1.5"):
        assert get_number("") == "-1.5"

    with mock.patch("builtins.input", return_value="a"):
        get_number("", test_running=True)
        mock_print.assert_called_with(colored("You can only input numbers.", "red"))

    with mock.patch("builtins.input", return_value="1a"):
        get_number("", test_running=True)
        mock_print.assert_called_with(colored("You can only input numbers.", "red"))

    with mock.patch("builtins.input", return_value="1-"):
        get_number("", test_running=True)
        mock_print.assert_called_with(colored("You can only input numbers.", "red"))

    with mock.patch("builtins.input", return_value=""):
        get_number("", test_running=True)
        mock_print.assert_called_with(colored("Please enter a valid number.", "red"))


@mock.patch("builtins.print")
def test_getcommand(mock_print):
    fridge = Fridge()
    with mock.patch("builtins.input", return_value="C"):
        fridge.choose_recipe = mock.MagicMock()
        get_command(fridge, test_running=True)
        assert fridge.choose_recipe.called

    with mock.patch("builtins.input", return_value="A"):
        fridge.add_recipe = mock.MagicMock()
        get_command(fridge, test_running=True)
        assert fridge.add_recipe.called

    with mock.patch("builtins.input", return_value="D"):
        fridge.delete_recipe = mock.MagicMock()
        get_command(fridge, test_running=True)
        assert fridge.delete_recipe.called

    with mock.patch("builtins.input", return_value="U"):
        fridge.update_inventory = mock.MagicMock()
        get_command(fridge, test_running=True)
        assert fridge.update_inventory.called

    with mock.patch("builtins.input", return_value="R"):
        fridge.request_suggestion = mock.MagicMock()
        get_command(fridge, test_running=True)
        assert fridge.request_suggestion.called

    with mock.patch("builtins.input", return_value="E"):
        with pytest.raises(SystemExit):
            get_command(fridge, test_running=True)

    with mock.patch("builtins.input", return_value="L"):
        fridge.choose_recipe = mock.MagicMock()
        get_command(fridge, test_running=True)
        mock_print.assert_called_with(colored("Invalid input", "red"))
