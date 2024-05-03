import subprocess
import time

def open_tmux_session(command):
    # Start a detached tmux session and execute the command
    subprocess.run(["tmux", "new-session", "-d", "-s", "my_session"])
    subprocess.run(["tmux", "send-keys", "-t", "my_session", command, "Enter"])

def stop_tmux_session():
    # Send Ctrl+C to the tmux session
    subprocess.run(["tmux", "send-keys", "-t", "my_session", "C-c"])

def main():
    # Command to execute in the tmux session
    command = "echo 'Its working ' " #cd /path/to/monitoring_script && ./monitoring_script.sh"

    open_tmux_session(command)
    time.sleep(60)

    # Stop the tmux session
    stop_tmux_session()

if __name__ == "__main__":
    main()
