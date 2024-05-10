
### import needed functions..

from source_models import * 

# you take input through python 

# model 

# mode src / paiv 

# available_envmnts 

# batch size 

# cpi 

# steps  

# warmup_steps 

# log_name == add a run id 






def main(model,bkm_type,machine_type,env,input5_value,batch_size,cpi,precision_list,steps,warmup_steps,log_file,ip_token,op_token):

    if bkm_type=='paiv':
        paiv_docker=pytorch_paiv_docker(model,env,batch_size,cpi,steps,warmup_steps,precision_list,log_file,ip_token,op_token)
        paiv_docker.run_benchmarks()

    if model=="ResNet50-v1-5" and bkm_type=='src' and machine_type=='Intel':
        default_steps=1000
        wamp_up=100
        resnet=resnet_50_Intel_src(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions)
        resnet.run_benchmarks()

    if model=="ResNet50-v1-5" and bkm_type=='src' and machine_type=='amd':
        default_steps=1000
        wamp_up=100
        resnet=resnet_50_stock_tf_zendnn_src(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions)
        resnet.run_benchmarks()

    





if __name__ == "__main__" :

    import sys
    arguments = sys.argv[1:]

    # Print the arguments
    model = sys.argv[1]
    bkm_type = sys.argv[2]
    machine_type = sys.argv[3]
    env=sys.argv[4]
    input5_value =sys.argv[5]
    batch_size = sys.argv[6]
    cpi = sys.argv[7]
    precision_list=sys.argv[8]
    steps=sys.argv[9]
    warmup_steps=sys.argv[10]
    log_file=sys.argv[11]
    ip_token=sys.argv[12]
    op_token=sys.argv[13]
    print('coming here : ')

    model = input(" enter the model name: ")
    env_type = input("which environment u want to run ? : ")
    avilable_envs=input(" these are the avialble envs.. choose one : ")
    batch_size=input(" enter the BS : ")
    cpi=input( "enter the cpi : ")
    precisions=input(" enter the precisions u want to run : ")
    steps=int(input("enter the steps : "))
    warmup_steps=int(input(" enter the warmup_steps : "))
    #main(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions)
    main(model,bkm_type,machine_type,env,input5_value,batch_size,cpi,precision_list,steps,warmup_steps,log_file,ip_token,op_token)












