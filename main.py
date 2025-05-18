from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB Connection
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

# Database and Collection
db = client.todo_db
task_collection = db.tasks

# -------------------- CRUD FUNCTIONS --------------------

# Create
def create_task(description):
    task = {
        'task': description,
        'status': 'Not Yet Started'
    }
    result = task_collection.insert_one(task)
    print(f"✅ Task Created with ID: {result.inserted_id}")

# Read / View All
def view_tasks():
    tasks = task_collection.find()
    print("\n📋 All Tasks:")
    for task in tasks:
        print(f"- {task.get('task')} | Status: {task.get('status')} | ID: {task.get('_id')}")

# Update Description
def update_task(task_id, new_description):
    result = task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"task": new_description}}
    )
    if result.modified_count:
        print("✏️ Task description updated successfully.")
    else:
        print("⚠️ Task not found.")

# Update Status: In Progress
def mark_in_progress(task_id):
    result = task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": "In Progress"}}
    )
    if result.modified_count:
        print("🔄 Task marked as 'In Progress'.")
    else:
        print("⚠️ Task not found or already in progress.")

# Update Status: Complete
def mark_complete(task_id):
    result = task_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"status": "Complete"}}
    )
    if result.modified_count:
        print("✅ Task marked as 'Complete'.")
    else:
        print("⚠️ Task not found or already complete.")

# Delete Task
def delete_task(task_id):
    result = task_collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        print("🗑️ Task deleted successfully.")
    else:
        print("⚠️ Task not found.")

# -------------------- MENU LOOP --------------------

def menu():
    while True:
        print("\n====== TO-DO CLI App ======")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task Description")
        print("4. Mark Task as In Progress")
        print("5. Mark Task as Complete")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        try:
            if choice == '1':
                description = input("Enter your task: ")
                create_task(description)

            elif choice == '2':
                view_tasks()

            elif choice == '3':
                task_id = input("Enter Task ID to update: ")
                new_description = input("Enter new task description: ")
                update_task(task_id, new_description)

            elif choice == '4':
                task_id = input("Enter Task ID to mark as 'In Progress': ")
                mark_in_progress(task_id)

            elif choice == '5':
                task_id = input("Enter Task ID to mark as 'Complete': ")
                mark_complete(task_id)

            elif choice == '6':
                task_id = input("Enter Task ID to delete: ")
                delete_task(task_id)

            elif choice == '7':
                print("👋 Goodbye!")
                break

            else:
                print("❌ Invalid option. Please try again.")

        except Exception as e:
            print(f"❗Error: {e}")

# -------------------- RUN --------------------
if __name__ == "__main__":
    menu()
