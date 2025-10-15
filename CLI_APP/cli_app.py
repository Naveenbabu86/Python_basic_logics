import argparse

def read_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def write_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))

parser = argparse.ArgumentParser(description="Simple Todo CLI Application")
subparsers = parser.add_subparsers(dest="command", help="Available commands")

# Add command
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task", help="Task description")

# List command
list_parser = subparsers.add_parser("list", help="List all tasks")

# Remove command
remove_parser = subparsers.add_parser("remove", help="Remove a task by its index")
remove_parser.add_argument("index", type=int, help="Task index to remove")

args = parser.parse_args()

if args.command == "add":
    tasks = read_tasks()
    tasks.append(args.task)
    write_tasks(tasks)
    print(f"✅ Task added: {args.task}")

elif args.command == "list":
    tasks = read_tasks()
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("📝 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

elif args.command == "remove":
    tasks = read_tasks()
    if 0 < args.index <= len(tasks):
        removed = tasks.pop(args.index - 1)
        write_tasks(tasks)
        print(f"🗑️ Task removed: {removed}")
    else:
        print("❌ Invalid index.")
else:
    parser.print_help()
