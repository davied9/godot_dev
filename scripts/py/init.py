
import os, sys, platform, subprocess

def check_python_version():
    if platform.python_version() < '3.5':
        print('[ERROR] support python version greater than 3.5')
        exit(1)
    if platform.system() != 'Windows':
        print('[ERROR] support Windows only')
        exit(1)

check_python_version()

def check_working_dir():
    # should run init.py from godot_dev root directory
    godot_dev_root = os.path.abspath(os.path.join(__file__, '..', '..', '..')).replace('g:', 'G:')
    if godot_dev_root != os.getcwd():
        print("[ERROR] please call init.py from godot_dev root : calling from {0}".format(os.getcwd()))
        exit(1)

def run_command(command, work_stage):
    print("start {} ...".format(work_stage))
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stdout:
        print(stdout.decode())
    if stderr:
        print(stderr.decode())
        print("{} failed, abort".format(work_stage))
        return False
    return True

def create_virtual_environment():
    if not os.path.exists(".venv"):
        if not run_command("virtualenv --no-download .venv", "creating virutal environment"):
            return
    if not run_command(os.path.join(os.getcwd(), "scripts", "bat", "setup_venv.bat"), "initializing virutal environment"):
        return
        
def clone_godot_repository():
    if not os.path.exists("godot"):
        if not run_command("git clone -q https://github.com/godotengine/godot.git --branch master --single-branch godot", "cloning godot repository"):
            return

if "__main__" == __name__:
    check_working_dir()
    create_virtual_environment()
    clone_godot_repository()
