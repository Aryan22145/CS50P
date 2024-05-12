from Twttr import shortern


def test_twttr():
    assert shortern("aeiouAEIOU") == ''
    assert shortern("Mr. Jock, TV quiz PhD., bags few lynx") == 'Mr. Jck, TV qz PhD., bgs fw lynx'
    assert shortern("1234567890") == "1234567890"
