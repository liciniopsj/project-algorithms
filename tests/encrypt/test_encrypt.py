from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("secret", 3) == "ces_ter"
    assert encrypt_message("secret", 4) == "te_rces"
    assert encrypt_message("secret message", 9) == "em terces_egass"
    assert encrypt_message("", 3) == ""

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("secret", "invalid_key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)
