import docker
import subprocess
import time


def check_image_existence(image_name):
    client = docker.from_env()
    try:
        #tags = client.images.tags(image)
        #latest_tag = sorted(tags)[-1]
        #client.images.pull(f"{image_name}:{latest_tag}")
        client.images.get(image_name)
        return True
    except docker.errors.ImageNotFound:
        return False

def check_container_existence(container_name):
    client = docker.from_env()
    try:
        client.containers.get(container_name)
        return True
    except docker.errors.NotFound:
        return False

def create_container(image_name, container_name):
    client = docker.from_env()
    container = client.containers.run(image_name, detach=True, name=container_name , privileged=True, command="tail -f /dev/null", volumes={"/home/logs/": {"bind": "/home/logs/", "mode": "rw"}})
    return container

def start_or_create_container(image_name, container_name):
    if not check_image_existence(image_name):
        print(f"Image '{image_name}' does not exist. Pulling...")
        subprocess.run(['docker', 'pull', image_name])

    if not check_container_existence(container_name):
        print(f"Container '{container_name}' does not exist. Creating...")
        create_container(image_name, container_name)
    else:
        client = docker.from_env()
        container = client.containers.get(container_name)
        if container.status != "running":
            print(f"Container '{container_name}' exists but is not running. Starting...")
            container.start()

def execute_commands_in_container(container_name, commands):
    client = docker.from_env()
    container = client.containers.get(container_name)
    for cmd in commands:
        exec_command = f"/bin/bash -c '{cmd}'"
        exec_response = container.exec_run(exec_command, stream=True)
        print(f"Output of command '{cmd}':")
        for line in exec_response.output:
            print(line.decode().strip())

def execute_shell_script_in_container(container_name, script_path):
    client = docker.from_env()
    container = client.containers.get(container_name)
    exec_command = f"/bin/bash -c 'cd {script_path} && bash run_avg-latency__SPR_RN50_rev3.1.sh'"
    exec_response = container.exec_run(exec_command, stream=True)
    print(f"Output of shell script '{script_path}/your_script.sh':")
    for line in exec_response.output:
        print(line.decode().strip())

if __name__ == "__main__":
    image_name = "sandeepgunturu/aimlbenchmarks:rev2"
    container_name = "your_container_name"
    script_path = "/home/AI/models/"
    additional_commands = [
        "echo 'Executing additional commands before running the shell script...'",
        "ls -l /",
        "sudo apt update && sudo apt install numactl -y",
        "source /home/AI/anaconda3/bin/activate && conda activate RN50-intel-tf-2.14 && sleep 10 && cd /home/AI/models/ && bash run_avg-latency__SPR_RN50_rev3.1.sh"
        # Add more commands as needed
    ]
    
    start_or_create_container(image_name, container_name)
    execute_commands_in_container(container_name, additional_commands)
    execute_shell_script_in_container(container_name, script_path)

