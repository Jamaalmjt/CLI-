import click


@click.group
def mycommands():
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"hello {name}!")

PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial",
}


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.KEYS()), default="m")
@click.argumet("todofile", type=click.Path(exists=False), required=0)
@click.option("-n", "--name", prompt="Enter the todo name", help="the name of the todo item")
@click.option("-d", "--desc", prompt="Describe the tod", help="The description of the todo it")
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filaname, "a+")as f:
        f.write(f"{name}:{description} [Priority:{PRIORITIES[priority]}")

@click.command()
@click.argumet("idx", type=int, required=1)
def delete_todo(idx):
    with open("mytodos.txt","r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f: 
        f.write("\n".join(todo_list))
        f.write('\n')



@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
        if priority is None:
            for idx, todo in enumerate(todo_list):
                print(f"({idx}) - {todo}")
        else:
            for idx, todo in enumerate(todo_list):
                if f"[Priority: {PRIORITIES[priority]}]" in todo:
                    print(f"({idx}) - {todo}")


mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__ == "__main__":
    mycommand()