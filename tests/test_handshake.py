import os
import importlib.util
import unittest

module_path = os.path.join(os.path.dirname(__file__), '..', 'bootloader', 'Codex16_handshake_validation.py')
spec = importlib.util.spec_from_file_location('validator', module_path)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class TestHandshakeValidation(unittest.TestCase):
    def test_verify_handshake_returns_true(self):
        self.assertTrue(validator.verify_handshake())


if __name__ == '__main__':
    unittest.main()
