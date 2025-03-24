import os
from scripts.docker_handler import DockerHandler

class OctaveRunner:
    SOLUTION_FOLDER = os.path.abspath("solution")
    TEST_CASES_FOLDER = os.path.abspath("test_cases")
    DOCKER_EXEC = ["docker-compose", "exec", "-T", "octave-container"]

    @staticmethod
    def compile_octave(asm_file):
        # No compile needed for @Octave
        pass

    @staticmethod
    def run_octave(m_file, input_file):
        input_path = f"/test_cases/in/{input_file}"
        
        with open(os.path.join(OctaveRunner.TEST_CASES_FOLDER, "in", input_file), "r") as f:
            expected_input = "\n".join([line.strip() for line in f.readlines()])

        command = OctaveRunner.DOCKER_EXEC + ["bash", "-c", f"echo \"{expected_input}\" | octave --no-gui {m_file}"]
        output, _ = DockerHandler.exec_command(command)
        return output
