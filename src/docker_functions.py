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

def paiv_docker_operations(image_name, container_name, volumes):
    # Initialize the Docker client
    client = docker.from_env()

    # Check if the container already exists
    existing_containers = client.containers.list(all=True, filters={'name': container_name})
    if existing_containers:
        print(f"Container '{container_name}' already exists.")
        return existing_containers[0]

    # Check if the image exists
    try:
        client.images.get(image_name)
    except docker.errors.ImageNotFound:
        print(f"Image '{image_name}' not found. Pulling the image...")
        try:
            client.images.pull(image_name)
            print(f"Image '{image_name}' pulled successfully.")
        except docker.errors.ImageNotFound:
            print(f"Failed to pull image '{image_name}'.")
            return

    # Define the container parameters
    container_params = {
        'image': image_name,
        'name': container_name,
        'volumes': volumes,
        'privileged': True,
        'network_mode': 'host',
        'shm_size': '4g',
        'detach': True,
    }

    # Create the container
    try:
        container = client.containers.run(**container_params)
        print(f"Container '{container_name}' created successfully.")
        return container
    except docker.errors.APIError as e:
        print(f"Failed to create container: {e}")
        return None

# # Example usage
# image_name = 'dcsorepo.jf.intel.com/dlboost/pytorch:2024_ww10'
# container_name = 'pytorch_2024_ww10'
# volumes = {
#     '/home/dataset/pytorch': {'bind': '/home/dataset/pytorch', 'mode': 'rw'},
#     '/home/dl_boost/log/pytorch': {'bind': '/home/dl_boost/log/pytorch', 'mode': 'rw'},
# }

# create_container(image_name, container_name, volumes)


# if __name__ == "__main__":
#     image_name = "sandeepgunturu/aimlbenchmarks:rev2"
#     container_name = "your_container_name"
#     script_path = "/home/AI/models/"
#     additional_commands = [
#         "echo 'Executing additional commands before running the shell script...'",
#         "ls -l /",
#         "sudo apt update && sudo apt install numactl -y",
#         "source /home/AI/anaconda3/bin/activate && conda activate RN50-intel-tf-2.14 && sleep 10 && cd /home/AI/models/ && bash run_avg-latency__SPR_RN50_rev3.1.sh"
#         # Add more commands as needed
#     ]
    
#     start_or_create_container(image_name, container_name)
#     execute_commands_in_container(container_name, additional_commands)
#     execute_shell_script_in_container(container_name, script_path)

