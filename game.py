from DB import todo_list

def main() -> None:
    the_list = todo_list
    flag = True
    while flag:
        user_choice = get_user_choice()
        match user_choice:
            case '1':
                new_task = input('enter new task: ')
                add_task(the_list,new_task)
                print('the list: ',the_list)
            case '2':
                show_all_tasks(the_list)
            case '3':
                if len(the_list) == 0 :
                    print('list is empty')
                    continue
                index = input('enter task num to delete: ')
                delete_task(the_list,index)
                
            case '4':
                if len(the_list) == 0 :
                    print('list is empty')
                    continue
                index = input('enter task num to edit: ')
                new_task = input('enter new task: ')
                edit_task(the_list,index, new_task)
            case '5':
                print('exit')
                flag = False
            case _:
                print('an expected choice')

    


def get_user_choice() -> str:
    while True: 
        user_choice =  input("""
            1. Adding a task. 
            2. Show all tasks. 
            3. Deleting a task. 
            4. Editing a task. 
            5. Exit. 
            """)
        if len(user_choice) == 1:
            return user_choice



def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    
    
def show_all_tasks(tasks: list) -> None:
    if  len(tasks):
        print({'list':tasks})
    else: print('list is empty')


def delete_task(tasks: list, index: int) -> bool:
    index = int(index) -1
    task = tasks.pop(index)
    print(f'you deleted {task}')
    return True
        
def edit_task(tasks: list, index: int, new_task: str) -> bool:
    index = int(index) -1
    if len(tasks) < index:
        print('en volid index')
        False
        
    else: tasks[index] = new_task
    
    