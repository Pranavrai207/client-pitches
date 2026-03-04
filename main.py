import argparse
import sys
import os
import subprocess

def run_script(script_path, script_args=None):
    """Executes a python script with optional arguments."""
    cmd = [sys.executable, script_path]
    if script_args:
        cmd.extend(script_args)
    
    print(f"\n🚀 Running: {os.path.basename(script_path)}")
    print("-" * 40)
    
    try:
        result = subprocess.run(cmd, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {os.path.basename(script_path)}: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Lead Gen System Orchestrator (10/10 Hybrid Structure)")
    parser.add_argument("command", choices=["scrape", "filter", "pitch", "report", "deploy", "optimize", "all"], 
                        help="Command to execute")
    parser.add_argument("--query", "-q", help="Search query (e.g. 'cafes in Delhi')")
    parser.add_argument("--max", "-m", help="Maximum results to collect")
    parser.add_argument("--client", "-c", help="Client name/folder for pitch, deploy, or optimize")
    parser.add_argument("--dir", "-d", help="Custom directory for optimize_assets")

    args, unknown = parser.parse_known_args()
    
    scripts_dir = "scripts"
    
    # --- Workflow Orchestration ---
    
    if args.command == "all":
        print("🌟 Executing Full Automation Pipeline...")
        if not run_script(os.path.join(scripts_dir, "scraping", "scraper.py")): sys.exit(1)
        if not run_script(os.path.join(scripts_dir, "processing", "filter_leads.py")): sys.exit(1)
        print("✅ Pipeline Complete. Check data/ directory for results.")
        return

    if args.command == "scrape":
        scrape_args = []
        if args.query: scrape_args.extend(["--query", args.query])
        if args.max: scrape_args.extend(["--max", args.max])
        run_script(os.path.join(scripts_dir, "scraping", "scraper.py"), scrape_args)

    elif args.command == "filter":
        run_script(os.path.join(scripts_dir, "processing", "filter_leads.py"))

    elif args.command == "pitch":
        if not args.client:
            print("❌ Error: --client [name] is required for pitch generation.")
            sys.exit(1)
        run_script(os.path.join(scripts_dir, "generation", "generate_pitch.py"), [args.client])

    elif args.command == "report":
        run_script(os.path.join(scripts_dir, "generation", "generate_report.py"))

    elif args.command == "optimize":
        target = args.dir or (f"clients/{args.client}/assets/images" if args.client else None)
        if not target:
            print("❌ Error: --client [name] or --dir [path] is required for optimization.")
            sys.exit(1)
        run_script(os.path.join(scripts_dir, "generation", "optimize_assets.py"), [target])

    elif args.command == "deploy":
        if not args.client:
            print("❌ Error: --client [folder_name] is required for deployment.")
            sys.exit(1)
        run_script(os.path.join(scripts_dir, "deployment", "deploy.py"), [args.client])

if __name__ == "__main__":
    main()
