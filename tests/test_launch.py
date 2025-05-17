import os
import importlib.util
import unittest

module_path = os.path.join(os.path.dirname(__file__), '..', 'bootloader', 'Codex16_launch.py')
spec = importlib.util.spec_from_file_location('launch', module_path)
launch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launch)

expand_doctrine = launch.expand_doctrine
MAX_CHAIN_LENGTH = launch.MAX_CHAIN_LENGTH


class TestExpandDoctrine(unittest.TestCase):

    def test_non_string_input_raises(self):
        with self.assertRaises(TypeError):
            expand_doctrine([1, 2, 3])

    def test_chain_length_respects_limits(self):
        cases = [
            ("5", 2),  # small iteration count
            ("25", 2),  # exceeds limit; should cap at 20 and chain truncated
        ]
        for env_value, seed_count in cases:
            with self.subTest(env_value=env_value):
                seeds = [f"seed{i}" for i in range(seed_count)]
                os.environ["RI_ITERATIONS"] = env_value
                result = expand_doctrine(seeds)
                iterations = max(1, min(int(env_value), 20))
                expected_length = min(MAX_CHAIN_LENGTH, seed_count + iterations)
                self.assertEqual(len(result), expected_length)


if __name__ == '__main__':
    unittest.main()
