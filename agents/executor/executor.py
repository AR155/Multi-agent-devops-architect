import subprocess


def run_terraform():
    subprocess.run(["terraform", "init"], cwd="infra/terraform")
    subprocess.run(["terraform", "apply", "-auto-approve"], cwd="infra/terraform")


if __name__ == "__main__":
    run_terraform()
