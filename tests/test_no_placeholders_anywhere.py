import unittest
from pathlib import Path

import yaml


class TestNoPlaceholdersAnywhere(unittest.TestCase):
    def test_no_placeholders(self):
        data = yaml.safe_load(Path('model/assumptions.yaml').read_text(encoding='utf-8'))
        placeholders = []

        def walk(value, path):
            if isinstance(value, dict):
                for key, item in value.items():
                    walk(item, path + [str(key)])
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    walk(item, path + [str(index)])
            else:
                if value == 'PLACEHOLDER':
                    placeholders.append('.'.join(path))

        walk(data, [])
        if placeholders:
            self.fail('PLACEHOLDER values found at: ' + ', '.join(placeholders))


if __name__ == '__main__':
    unittest.main()
