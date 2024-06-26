from docker_functions import * 


## common variabe

#image_name = "sandeepgunturu/aimlbenchmarks:rev2"
image_name='dcsorepo.jf.intel.com/dlboost/pytorch:2024_ww10'

# container_name = "your_container_name"
# import random
# random_number = random.randint(10000, 99999)


class pytorch_paiv_docker():
    def __init__(self,model,env,batch_size,cpi,steps,warmup_steps,precisions,log_file,ip_token,op_token):
        self.model_name=model

        self.batch_size=batch_size
        self.cpi=cpi
        self.steps=steps
        self.warmup_steps=warmup_steps
        self.precisions=precisions
        self.env=env
        self.log_name=log_file
        
        self.framework='pytorch'
        self.mode='latency' # latency / throughput / accuracy
        self.topology=model
        self.function='inference'

        if model == 'DLRM-V2':
            self.weight_sharing=True
        else :
            self.weight_sharing=False
        if model == 'ResNet50-v1-5':
            self.data_type='dummy'
        else :
            self.data_type='real'
        if model == 'GPT-J-6B' or model == 'LLaMA-2-7B' or model == 'LLaMA-2-13B':
            self.ip_token=ip_token
            self.op_token=op_token

        if self.env=='ww10':
            self.image_name='dcsorepo.jf.intel.com/dlboost/pytorch:2024_ww10'
            self.container_name='pytorch_2024_ww10'
            self.commands = [
                f'docker exec -it pytorch_2024_ww10 /bin/bash -c "python /home/workspace/benchmark/main.py \
                    --framework {self.framework} --mode {self.mode} --topology {self.model_name} --function {self.function} \
                    --precision amx_int8 --weight_sharing {self.weight_sharing} --batch_size {self.batch_size} --data_type {self.data_type}" '
            ]
        if self.env=='ww16':
            self.image_name='dcsorepo.jf.intel.com/dlboost/pytorch:2024_ww16'
            self.container_name='pytorch_2024_ww16'
            self.commands = [
                f'docker exec -it pytorch_2024_ww16 /bin/bash -c "python /home/workspace/benchmark/main.py \
                    --framework {self.framework} --mode {self.mode} --topology {self.model_name} --function {self.function} \
                    --precision amx_int8 --weight_sharing {self.weight_sharing} --batch_size {self.batch_size} --data_type {self.data_type}" '
            ]

        self.volumes = {
            '/home/dataset/pytorch': {'bind': '/home/dataset/pytorch', 'mode': 'rw'},
            '/home/dl_boost/log/pytorch': {'bind': '/home/dl_boost/log/pytorch', 'mode': 'rw'},
        }
            

    def run_benchmarks(self):
        paiv_docker_operations(self.image_name,self.container_name,self.volumes)
        #run_benchmark(self)


class resnet_50_Intel_src():
    def_steps=1000
    def_wm_steps=100
    def_script_path = "/home/AI/models/"
    #random_number = random.randint(10000, 99999)
    def __init__(self, model, env_type, available_envs, batch_size, cpi, steps, warmup_steps,precisions):
        self.model = model
        self.env_type = env_type
        self.available_envs = available_envs
        self.batch_size = batch_size
        self.cpi = cpi
        self.steps = steps
        self.warmup_steps = warmup_steps
        self.precisions=precisions
        self.container_name=f"your_container_name" #{self.model}-{self.env_type}"
        #condition for default steps

        self.commands = [
            "echo 'Executing additional commands before running the shell script...'",
            "sudo apt update && sudo apt install numactl -y",
            f"source /home/AI/anaconda3/bin/activate && \
            conda activate RN50-intel-tf-2.14 && \
            sleep 10 && cd /home/AI/models/ && \
            export VAR1={self.batch_size} && export VAR2={self.cpi} && export VAR3={self.steps} && export VAR4={self.warmup_steps} && \
            bash run_avg-latency__SPR_RN50_rev3.1.sh "
            # Add more commands as needed
        ]
    def run_benchmarks(self):
        run_benchmark(self)


class resnet_50_stock_tf_zendnn_src():
    def_steps=1000
    def_wm_steps=100
    def_script_path = "/home/AI/models/"
    #random_number = random.randint(10000, 99999)
    def __init__(self, model, env_type, available_envs, batch_size, cpi, steps, warmup_steps,precisions):
        self.model = model
        self.env_type = env_type
        self.available_envs = available_envs
        self.batch_size = batch_size
        self.cpi = cpi
        self.steps = steps
        self.warmup_steps = warmup_steps
        self.precisions=precisions
        self.container_name=f"your_container_name" #f"{self.model}-{self.env_type}"
        #condition for default steps

        self.commands = [
            "echo 'Executing additional commands before running the shell script...'",
            "sudo apt update && sudo apt install numactl -y",
            f"source /home/AI/anaconda3/bin/activate && \
            conda activate zendnn4.1-RN50-stocktf-2.12-py-3.10 && \
            sleep 10 && cd /home/AI/TF_v2.12_ZenDNN_v4.1_Python_v3.10/ && source scripts/TF_ZenDNN_setup_release.sh && source scripts/zendnn_TF_env_setup.sh && \
            cd /home/AI/models/ && \
            export VAR1={self.precisions} && export VAR2={self.batch_size} && export VAR3={self.cpi} && export VAR4={self.steps} && export VAR5={self.warmup_steps} && \
            bash run_OPTS-OFF-zendnn_AT_RN50_REV1.sh "
            # Add more commands as needed
        ]
    def run_benchmarks(self):
        run_benchmark(self)

def run_benchmark(self):

    start_or_create_container(image_name, self.container_name)

    execute_commands_in_container(self.container_name, self.commands)



        
