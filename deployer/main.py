import typer
import sys
import json
import os
import subprocess
from pulumi import automation as auto

app = typer.Typer()


@app.command()
def destroy_stack():
    stack = auto.create_or_select_stack(stack_name=stack_name, work_dir=work_dir)
    stack.destroy(on_output=print)
    print("stack destroy complete")
    sys.exit()


@app.command()
def provision_stack():
    stack = auto.create_or_select_stack(stack_name=stack_name, work_dir=work_dir)
    print("successfully initialized stack")

    print("refreshing stack")
    stack.refresh(on_output=print)
    print("refresh complete")

    print("updating stack...")
    up_res = stack.up(on_output=print)
    print(f"update summary: \n{json.dumps(up_res.summary.resource_changes, indent=4)}")


@app.command()
def provision_cluster():
    subprocess.run(["minikube", "start", "--driver=hyperkit"], check=True, capture_output=True)


@app.command()
def destroy_cluster():
    subprocess.run(["minikube", "delete"], check=True, capture_output=True)


if __name__ == "__main__":
    work_dir = os.path.join(os.path.dirname(__file__), "..", "pulumi")
    stack_name = "deployer"
    app()
