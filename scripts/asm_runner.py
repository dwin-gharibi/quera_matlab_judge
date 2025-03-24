import os
from scripts.docker_handler import DockerHandler

class AssemblyRunner:
    SOLUTION_FOLDER = os.path.abspath("solution")
    TEST_CASES_FOLDER = os.path.abspath("test_cases")
    DOCKER_EXEC = ["docker-compose", "exec", "-T", "asm-container"]

    @staticmethod
    def compile_asm(asm_file):
        program_name = asm_file.split('.')[0]
        DockerHandler.exec_command(AssemblyRunner.DOCKER_EXEC + ["nasm", "-f", "elf", "-d", "ELF_TYPE", "asm_io.asm"])
        DockerHandler.exec_command(AssemblyRunner.DOCKER_EXEC + ["nasm", "-f", "elf", asm_file])
        DockerHandler.exec_command(AssemblyRunner.DOCKER_EXEC + ["gcc", "-m32", "-c", "driver.c"])
        DockerHandler.exec_command(AssemblyRunner.DOCKER_EXEC + ["gcc", "-m32", "driver.o", f"{program_name}.o", "asm_io.o"])

    @staticmethod
    def run_asm(asm_file, input_file):
        input_path = f"/test_cases/in/{input_file}"
        with open(os.path.join(AssemblyRunner.TEST_CASES_FOLDER, "in", input_file), "r") as f:
            expected_input = "\n".join([line.strip() for line in f.readlines()])

        command = AssemblyRunner.DOCKER_EXEC + ["bash", "-c", f"echo \"{expected_input}\" | ./a.out"]
        output, _ = DockerHandler.exec_command(command)
        return output
