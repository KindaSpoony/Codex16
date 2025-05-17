import importlib.util
import os
import unittest

class TestHandshakeValidator(unittest.TestCase):
    def test_verify_handshake(self):
        module_path = os.path.join(os.path.dirname(__file__), '..', 'bootloader', 'Codex16_handshake_validation.py')
        spec = importlib.util.spec_from_file_location('handshake', module_path)
        handshake = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(handshake)
        self.assertTrue(handshake.verify_handshake())

if __name__ == '__main__':
    unittest.main()
