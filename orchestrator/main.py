import argparse, os
from agents.planner.planner import analyze_repo
from agents.executor.executor import run_terraform
from agents.monitor.observer import check_health


def main(repo_path):
    print(" Step 1: Planning")
    plan = analyze_repo(repo_path, "Auto generated plan")
    print(plan)

    print("\n Step 2: Executing (Terraform)")
    run_terraform()

    print("\n Step 3: Observing")
    status = check_health()
    print("Service health:", status)

    #  Save to artifacts/report.md
    os.makedirs("artifacts", exist_ok=True)
    with open("artifacts/report.md", "w") as f:
        f.write(f"# Observer Report\n\nStatus: {status}\n")

    print(f"Report saved at artifacts/report.md")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    main(args.repo)
