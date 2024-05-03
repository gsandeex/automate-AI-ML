
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






def main(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions):
    if model=="RN50-intel" and env_type=='src':
        default_steps=1000
        wamp_up=100
        resnet=resnet_50_Intel_src(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions)
        resnet.run_benchmark()
        print(" Run completed successfully")

    if model=="RN50-amd" and env_type=='src':
        default_steps=1000
        wamp_up=100
        resnet=resnet_50_stock_tf_zendnn_src(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions)
        resnet.run_benchmark()
        print(" Run completed successfully")

    





if __name__ == "__main__" :

    model = input(" enter the model name: ")
    env_type = input("which environment u want to run ? : ")
    avilable_envs=input(" these are the avialble envs.. choose one : ")
    batch_size=input(" enter the BS : ")
    cpi=input( "enter the cpi : ")
    precisions=input(" enter the precisions u want to run : ")
    steps=int(input("enter the steps : "))
    warmup_steps=int(input(" enter the warmup_steps : "))
    main(model,env_type,avilable_envs,batch_size,cpi,steps,warmup_steps,precisions) 












