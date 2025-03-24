import unittest
import os
from scripts.docker_handler import DockerHandler
from scripts.octave_runner import OctaveRunner

class TestOctavePrograms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        DockerHandler.start_container()

    @classmethod
    def tearDownClass(cls):
        DockerHandler.stop_container()

    def test_1(self):
        octave_file = "run_my_sum.m"
        input_file = "input4.txt"
        output_file = "output4.txt"

        OctaveRunner.compile_octave(octave_file)
        output = OctaveRunner.run_octave(octave_file, input_file)

        output_path = os.path.join(OctaveRunner.TEST_CASES_FOLDER, "out", output_file)
        with open(output_path, "r") as f:
            expected_output = [line.strip() for line in f.readlines()]

        self.assertEqual(output, expected_output, f"Unexpected output for {octave_file}")


if __name__ == "__main__":
    unittest.main()
