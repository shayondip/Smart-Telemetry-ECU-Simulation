from ecu.engine import Engine


def test_engine_start():
    engine = Engine()
    engine.start()

    assert engine.running is True
    assert engine.rpm == 800


def test_engine_stop():
    engine = Engine()
    engine.start()
    engine.stop()

    assert engine.running is False
    assert engine.rpm == 0