import os
import subprocess
import sys

# --- CONFIGURATION ---
# Change this to your GitHub Repository URL
REPO_URL = "https://github.com/Pranavrai207/client-pitches.git" 
GITHUB_USERNAME = "Pranavrai207"
REPO_NAME = "client-pitches"

def run_git(commands):
    """Executes a list of git commands."""
    for cmd in commands:
        try:
            print(f"Running: {cmd}")
            subprocess.run(cmd, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing {cmd}: {e}")
            return False
    return True

def deploy(client_folder):
    """Adds, commits, and pushes a specific client folder."""
    # Add project root to sys.path
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    if root_dir not in sys.path:
        sys.path.append(root_dir)
    clients_path = os.path.join(root_dir, "Client_Websites", "clients")
    if not os.path.exists(os.path.join(clients_path, client_folder)):
        print(f"Error: Folder '{client_folder}' not found in {clients_path}.")
        return

    # git commands should run from the root of the repo
    # 1. Check if remote is set
    result = subprocess.run("git remote", capture_output=True, text=True, shell=True)
    if "origin" not in result.stdout:
        if "REPLACE_WITH" in REPO_URL:
            print("\n!!! ACTION REQUIRED !!!")
            print("Please edit deploy.py and set your REPO_URL first.")
            return
        subprocess.run(f"git remote add origin {REPO_URL}", shell=True)

    # 2. Git Workflow
    msg = f"Add pitch for {client_folder}"
    path_to_client = os.path.join("clients", client_folder)
    commands = [
        f"git add {path_to_client}",
        f'git commit -m "{msg}"',
        "git push -u origin main"
    ]
    
    if run_git(commands):
        live_url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/clients/{client_folder}/"
        print("\n" + "="*50)
        print("🚀 DEPLOYMENT SUCCESSFUL!")
        print(f"Client: {client_folder}")
        print(f"Live URL: {live_url}")
        print("="*50)
    else:
        print("\n❌ Deployment Failed. Check your internet connection or GitHub permissions.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python deploy.py [folder_name]")
        print("Example: python deploy.py reflections_cafe")
    else:
        deploy(sys.argv[1])
