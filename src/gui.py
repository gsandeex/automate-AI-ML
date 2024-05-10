###################################

import tkinter as tk
from tkinter import ttk
import subprocess
import os
import paramiko
import threading

def run_gui():

    def update_dropdown4(event):
        option1 = dropdown1.get()
        option2 = dropdown2.get()
        option3 = dropdown3.get()
        print(option1)
        print(option2)
        print(option3)
        #if option1 == 'GPTJ' or option1 == 'Llama-7b' or option1 == 'Llama-13b':

        ######## if env id PAIV ##########
        if option1 == "DLRM-V2" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "ResNet50-v1-5" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "BERT-LARGE" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "Distilbert" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "GPT-J-6B" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "LLaMA-2-7B" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd") or \
            option1 == "LLaMA-2-13B" and option2 == "paiv" and (option3 == "Intel" or option3 == "amd"):
            options = ["ww10", "ww16"]

        ######### if env is SOURCE #########
        elif option1 == "ResNet50-v1-5" and option2 == "src" and option3 == "Intel":
            options = ["Intel TF 2.13", "Intel TF 2.14"]
        elif option1 == "ResNet50-v1-5" and option2 == "src" and option3 == "amd":
            options = ["zendnn 4.1 TF 2.12", "stock TF 2.13","stock tf 2.14"]

        elif option1 == "BERT-LARGE" and option2 == "src" and option3 == "Intel":
            options = ["need to add bert"]
        elif option1 == "BERT-LARGE" and option2 == "src" and option3 == "amd":
            options = ["need to add bert"]
        
        elif option1 == "DLRM-V2" and option2 == "src" and option3 == "Intel":
            options = ["need to add dlrm"]
        elif option1 == "DLRM-V2" and option2 == "src" and option3 == "amd":
            options = ["need to add dlrm"]
        
        elif option1 == "Distilbert" and option2 == "src" and option3 == "Intel":
            options = ["need to add Distilbert"]
        elif option1 == "Distilbert" and option2 == "src" and option3 == "amd":
            options = ["need to add Distilbert"]

        else:
            options = []  # Clear options if no valid selection
        dropdown4.config(values=options)

    def watch_logs(channel, log_file):
        # Continuously read and print the live logs
        while True:
            data = channel.recv(1024).decode('utf-8')
            if data:
                print(data, end='', flush=True)
                # console_output.insert(tk.END, data)
                # console_output.see(tk.END)
                log_file.write(data)
                log_file.flush()

    def execute_command():
        # # Create a new window for displaying the console output
        # output_window = tk.Toplevel(app)
        # output_window.title("Console Output")
        
        # # Create a Text widget to display the console output
        # console_output = tk.Text(output_window, height=40, width=100)
        # console_output.pack(padx=10, pady=10)

        # Create an SSH client instance
        # ssh_client = paramiko.SSHClient()
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        model = dropdown1.get()
        bkm_type = dropdown2.get()
        machine_type = dropdown3.get()
        env = dropdown4.get()
        input5_value = dropdown5.get()
        batch_size   = batch_size_entry.get()
        cpi = cpi_entry.get()
        precision_list=precision_entry.get()
        steps=steps_entry.get()
        warmup_steps=wm_up_entry.get()
        log_file=logfile_name_entry.get()
        ip_token=ip_token_entry.get()
        op_token=op_token_entry.get()
        arguments=[model,bkm_type,machine_type,env,input5_value,batch_size,cpi,precision_list,steps,warmup_steps,log_file, \
                   ip_token,op_token]

        try:

            run_log=f'{machine_ip_entry.get()}-{model}-{bkm_type}-{env}.log'
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the remote server
            hostname=machine_ip_entry.get()
            username='root'
            password='Intel!'
            log_file_path=f"C:\\Users\\GSANDEEX\\Downloads\\{machine_ip_entry.get()}-{model}-{bkm_type}-{env}.log"
            #command='nvidia-smi dmon'
            command = f'python3 harness_main.py {" ".join(arguments)}'
            ssh_client.connect(hostname,username=username, password=password)

            # Open a SSH session and execute the command
            _, stdout, stderr = ssh_client.exec_command(command, get_pty=True)

            # Open a log file for writing
            with open(log_file_path, 'a') as log_file:
                # Start a thread to watch live logs
                log_watcher_thread = threading.Thread(target=watch_logs, args=(stdout.channel, log_file))
                log_watcher_thread.daemon = True
                log_watcher_thread.start()

                # Wait for the command to complete
                stdout.channel.recv_exit_status()

        finally:
            # Close the SSH client connection
            ssh_client.close()

    # Create the main application window
    app = tk.Tk()
    app.title("ML Model Trigger")

    # Create dropdown menus for input values
    tk.Label(app, text="Models:").pack()
    dropdown1 = ttk.Combobox(app, values=["ResNet50-v1-5", "BERT-LARGE","Distilbert", "DLRM-V2","GPT-J-6B","llama-7b","LLaMA-2-13B"],state="readonly")
    dropdown1.pack()

    tk.Label(app, text="Type of BKM:").pack()
    dropdown2 = ttk.Combobox(app,state="readonly", values=["src", "paiv", "Option C"])
    dropdown2.pack()

    #dropdown1.bind("<<ComboboxSelected>>", update_dropdown2)
    #dropdown1.bind("<<ComboboxSelected>>", lambda event: update_dropdown2())

    tk.Label(app, text="Machine Type:").pack()
    dropdown3 = ttk.Combobox(app, state="readonly",values=["Intel", "amd", "others"])
    dropdown3.pack()

    tk.Label(app, text="env").pack()
    dropdown4 = ttk.Combobox(app,state="readonly")
    dropdown4.pack()
    # machine_ip_label = tk.Label(app, text=" Machine IP :")
    # machine_ip_label.pack(padx=10, pady=5)
    # machine_ip_entry = tk.Entry(app)
    # machine_ip_entry.pack(padx=10, pady=5)

    dropdown1.bind("<<ComboboxSelected>>", update_dropdown4)
    dropdown2.bind("<<ComboboxSelected>>", update_dropdown4)
    dropdown3.bind("<<ComboboxSelected>>", update_dropdown4)

    ######## just as a spare #########
    tk.Label(app, text="Input 5:").pack()
    dropdown5 = ttk.Combobox(app, values=["Item Alpha", "Item Beta", "Item Gamma"])
    dropdown5.pack()

    ## machine ip ##
    machine_ip_label = tk.Label(app, text=" Machine IP :")
    machine_ip_label.pack(padx=10, pady=5)
    machine_ip_entry = tk.Entry(app)
    machine_ip_entry.pack(padx=10, pady=5)

    ## batch szie ##
    batch_size_label = tk.Label(app, text="Batch size ex : '1 2 3 4' :")
    batch_size_label.pack(padx=10, pady=5)
    batch_size_entry = tk.Entry(app)
    batch_size_entry.pack(padx=10, pady=5)

    ## cpi ##

    cpi_label = tk.Label(app, text="cpi ex : '1 2 3 4' :")
    cpi_label.pack(padx=10, pady=5)
    cpi_entry = tk.Entry(app)
    cpi_entry.pack(padx=10, pady=5)

    ## precision ##

    precision_label = tk.Label(app, text="precisions ex : 'int8 bfloat16 float32' :")
    precision_label.pack(padx=10, pady=5)
    precision_entry = tk.Entry(app)
    precision_entry.pack(padx=10, pady=5)

    ## steps ##
    steps_label = tk.Label(app, text="Steps ex : 100 ")
    steps_label.pack(padx=10, pady=5)
    steps_entry = tk.Entry(app)
    steps_entry.pack(padx=10, pady=5)

    ## warmup steps ##
    wm_up_label = tk.Label(app, text=" warmup steps ex : 10 ")
    wm_up_label.pack(padx=10, pady=5)
    wm_up_entry = tk.Entry(app)
    wm_up_entry.pack(padx=10, pady=5)

    ## log name ##
    logfile_name_label = tk.Label(app, text=" results log name ex : sweep.csv ")
    logfile_name_label.pack(padx=10, pady=5)
    logfile_name_entry = tk.Entry(app)
    logfile_name_entry.pack(padx=10, pady=5)

    ## input token ##
    ip_token_label = tk.Label(app, text="NOTE : enter here only for LLM's")
    ip_token_label.pack(padx=10, pady=5)
    ip_token_entry = tk.Entry(app)
    ip_token_entry.pack(padx=10, pady=5)

    ## op token ##
    op_token_label = tk.Label(app, text="NOTE : enter here only for LLM's ")
    op_token_label.pack(padx=10, pady=5)
    op_token_entry = tk.Entry(app)
    op_token_entry.pack(padx=10, pady=5)

    ######################## CONSOLE WIDGETS ###########################

    # process_button = tk.Button(app, text="Process", command=process_inputs)
    # process_button.pack(pady=10)

    # Create a button to trigger the ML model
    # run_model_button = tk.Button(app, text="Run Model", command=run_ml_model_2)
    # run_model_button.pack(pady=5)

    # button = tk.Button(app, text="Run ML Model", command=run_ml_model)
    # button.pack()

    button = tk.Button(app, text="Run Remote Script", command=execute_command)
    button.pack()
    # Create a Text widget to display the console output
    console_output = tk.Text(app, height=20, width=80)
    console_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    #console_output.pack()

    # Run the application
    app.mainloop()

run_gui()