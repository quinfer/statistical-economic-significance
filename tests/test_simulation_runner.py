import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from simulations.run_labs import build_results, check_reference, write_results


class SimulationReportTests(unittest.TestCase):
    def test_reference_reproduction_and_stale_views(self):
        result = build_results(('power',), 40, 7)
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            write_results(result, output)
            with contextlib.redirect_stdout(io.StringIO()):
                check_reference(output/'reference.json')
            (output/'summary.md').write_text('stale view\n')
            with self.assertRaisesRegex(AssertionError, 'stale'):
                check_reference(output/'reference.json')

    def test_changed_numbers_cannot_be_laundered_by_rebuilding_views(self):
        result = build_results(('power',), 40, 7)
        result['labs'][0]['scenarios'][0]['metrics']['zero_rejection']['estimate'] = .9
        with tempfile.TemporaryDirectory() as folder:
            write_results(result, folder)
            with self.assertRaises(AssertionError):
                check_reference(Path(folder)/'reference.json')

    def test_design_inputs_and_portable_manifest(self):
        for labs in ((), ('unknown',), ('power', 'power')):
            with self.assertRaises(ValueError):
                build_results(labs, 40, 7)
        result = build_results(('power',), 40, 7)
        self.assertEqual(result['seed'], 7)
        self.assertEqual(result['replications_per_scenario'], 40)
        self.assertTrue(all(not Path(p).is_absolute() for p in result['source_sha256']))
        self.assertTrue(all(len(h) == 64 for h in result['source_sha256'].values()))
        json.dumps(result, allow_nan=False)
