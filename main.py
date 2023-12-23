import tkinter as tk
import time

# In this function, we created entry window process
# Entry window gets information for disks value
def create_get_disk_window():

    # First Window Implemantation
    window_input = tk.Tk()
    window_input.title('Tower of Hanoi')
    window_input.geometry('800x600')
    window_input.resizable(False, False)

    # Load an image process
    image = '/Users/genius/Desktop/AlgorithmAnalysis_COMP303_Project_TowerOfHanoi_Group18/mainImage.png'
    img = tk.PhotoImage(file=image)
    if image:
        image_label = tk.Label(window_input, image=img)
        image_label.image = img
        image_label.pack(pady=5)
    else:
        'Image Not Found' # if image will not find, the console gives error message...

    # Create and configure Widgets
    entry = tk.Entry(window_input, font=('Arial', 12))
    entry.pack(pady=10, padx=20, ipady=5, fill=tk.X)
    button = tk.Button(window_input, text='Enter a disk value',
                                 command=get_num_disks_recursive, font=('Arial', 12), fg='blue')
    button.pack(pady=10, ipady=5, ipadx=10, fill=tk.X)

    error_label = tk.Label(window_input, text="", fg="red", font=('Arial', 15))
    error_label.pack(pady=10)
    exit_button = tk.Button(window_input, text='Exit', command=window_input.destroy, font=('Arial', 12), fg='red')
    exit_button.pack(pady=10, ipady=5, ipadx=10, fill=tk.X)

    return window_input, entry, error_label

# This function gets num of disks with recursively...
# We have try and except operation in this function number must be greater than 1.
def get_num_disks_recursive():
    global disk_number, tower_source_rod, tower_auxiliary_rod, tower_destination_rod, move_count, label_round, canvas_main, window_main, entry

    try:
        disk_number = int(entry.get())
        if disk_number < 1:
            raise ValueError("Number must be 1 or greater.")
        init_towers()
        create_main_window()
    except ValueError as e:
        print(f"Invalid input: {e}")
        error_label.config(text=f"Invalid input: {e}", fg="red")

# This function gets num of disks with iteratively...
# We have try and except operation in this function number must be greater than 1.
def get_num_disks_iterative():
    global disk_number, tower_source_rod, tower_auxiliary_rod, tower_destination_rod, move_count, label_round, canvas_main, window_main, entry

    try:
        disk_number = int(entry.get())
        if disk_number < 1:
            raise ValueError("Number must be 1 or greater.")
        init_towers()
        create_main_window()
    except ValueError as e:
        print(f"Invalid input: {e}")
        error_label.config(text=f"Invalid input: {e}", fg="red")

# This window creates secon window as a main window.
def create_main_window():
    global canvas_main, window_main, label_round, move_count, entry, window_input

    window_main = tk.Tk()
    window_main.geometry('1920x1080')
    window_main.title('Tower of Hanoi')

    label_title = tk.Label(window_main, text='Tower of Hanoi', font=('Times New Roman', 34, 'bold'), fg='black')
    label_title.pack(pady=2, side=tk.TOP, anchor=tk.N)

    label_round = tk.Label(window_main, text=f'Total Rounds: {move_count} for {disk_number} disks',
                           font=('Times New Roman', 26), fg='black')
    label_round.pack(side=tk.TOP, anchor=tk.N)

    restart = tk.Button(window_main, text='Restart', command=window_main.destroy)
    restart.place(x=1900, y=50, anchor=tk.NE)

    # If user click exit buttom, all program will close
    # In this function. if user directly click exit button in the second window, program automatically will close.
    # If user will run the algorithms(can be both iterative or recursive) then user must click exit buttom if user wish enclosed the gui...
    def Close():
        global window_main, window_input # calling first and second window...

        if window_main:
            if window_main.winfo_exists():
                window_main.destroy()
            window_main = None

        if window_input:
            if window_input.winfo_exists():
                window_input.destroy()
            window_input = None

        print("Program Closed")

    exit_button = tk.Button(window_main, text="Exit", command=Close)
    exit_button.place(x=1900, y=10, anchor=tk.NE)

    canvas_main = tk.Canvas(window_main, width=1920, height=1080)

    # Create and implemented the rods and platforms here.
    platform = canvas_main.create_rectangle(0, 725, 1920, 1080, fill='grey')
    source_rod = canvas_main.create_rectangle(250, 850, 275, 50, fill='red')
    canvas_main.create_text(250, 900, text='Source Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
    destination_rod = canvas_main.create_rectangle(950, 850, 975, 50, fill='red')
    canvas_main.create_text(950, 900, text='Auxiliary Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
    auxiliary_rod = canvas_main.create_rectangle(1645, 850, 1670, 50, fill='red')
    canvas_main.create_text(1645, 900, text='Destination Rod', font=('Times New Roman', 34), anchor=tk.CENTER)

    create_disk(canvas_main, 250, 800, tower_source_rod, disk_number)
    create_disk(canvas_main, 950, 800, tower_auxiliary_rod, disk_number)
    create_disk(canvas_main, 1645, 800, tower_destination_rod, disk_number)

    button_simulate_recursive = tk.Button(window_main, text='Simulate Recursive', command=simulate_recursive)
    button_simulate_recursive.place(x=20, y=10, anchor=tk.NW)

    button_simulate_iterative = tk.Button(window_main, text='Simulate Iterative', command=simulate_iterative)
    button_simulate_iterative.place(x=20, y=50, anchor=tk.NW)

    canvas_main.pack()

# In this function creates disk with help of sorting algorithm.
def create_disk(canvas, x, y, rod, total_disks):
    width = 25
    height = 60
    multiplier = 3
    disk_colors = ['red', 'firebrick', 'gold', 'dark orange', 'lime green', 'dark green', 'steel blue', 'dim gray', 'cyan', 'magenta', 'pink'] # fixed disk color
    selection_sort(rod, reverse=True)

    for index, size in enumerate(rod):
        disk_width = size * 20 * multiplier
        disk_x = x - (disk_width // 2) + (width // 2)
        disk_y = y - (index * height)
        color = disk_colors[size % len(disk_colors)]
        canvas.create_rectangle(disk_x, disk_y, disk_x + disk_width, disk_y + height, fill=color)

        label_x = disk_x + (disk_width // 2)
        label_y = disk_y + (height // 2)
        canvas.create_text(label_x, label_y, text=str(size), font=('Arial', 14), fill='white')

# We created and implement selection sort algorithm.
# In this function helps the create_disk function for sorting
def selection_sort(array, reverse=False):
    value = len(array)
    for index in range(value):
        if reverse:
            min_index = max(range(index, value), key=lambda x: array[x])
        else:
            min_index = min(range(index, value), key=lambda x: array[x])
        array[index], array[min_index] = array[min_index], array[index]

# In this function, the tower for the tower of hanoi algorithm is initialized.
# Arrays were created according to the rods and added to source rod info by disk num from user
def init_towers():
    global tower_source_rod, tower_auxiliary_rod, tower_destination_rod
    tower_source_rod = list(reversed(range(1, disk_number + 1)))
    tower_auxiliary_rod = []
    tower_destination_rod = []

# This function define to simulate Tower of Hanoi algorithm recursively.
def simulate_recursive():
    global disk_number, tower_source_rod, tower_auxiliary_rod, tower_destination_rod, move_count, label_round, canvas_main, window_main, entry

    init_towers() # call and initialize towers
    create_main_window() # call and initialize main window

    # if condition for checking valid number or invalid number
    if not entry.get().isdigit():
        error_label.config(text="Invalid input. Please enter a valid number.", fg="red")
    else:
        disk_number = int(entry.get())
        if disk_number < 1:
            error_label.config(text="Number must be 1 or greater.", fg="red")
        else:
            error_label.config(text="")
            simulate_recursive_hanoi()

# This function simulate Tower of Hanoi recursively and record the time for runtime calculation
def simulate_recursive_hanoi():
    global move_count
    move_count = 0
    start_time = time.time() # Runtime starting

    if disk_number > 0:
        hanoi_recursive(disk_number, tower_source_rod, tower_destination_rod, tower_auxiliary_rod)

    end_time = time.time() # Runtime ended

    run_time = end_time - start_time
    print(f"Recursive Total Rounds: {move_count} for {disk_number} disks")
    print(f"Recursive Total Runtime: {run_time} seconds")

# This function include nested function for update, delete, draw operations according to recursive algorithm
def hanoi_recursive(n, start_rod, end_rod, middle_rod):
    global move_count, canvas_main, label_round

    def update_canvas_recursive():
        canvas_main.delete("all") # all elements deleted

        platform = canvas_main.create_rectangle(0, 725, 1920, 1080, fill='grey')
        source_rod = canvas_main.create_rectangle(250, 850, 275, 50, fill='red')
        canvas_main.create_text(250, 900, text='Source Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
        destination_rod = canvas_main.create_rectangle(950, 850, 975, 50, fill='red')
        canvas_main.create_text(950, 900, text='Auxiliary Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
        auxiliary_rod = canvas_main.create_rectangle(1645, 850, 1670, 50, fill='red')
        canvas_main.create_text(1645, 900, text='Destination Rod', font=('Times New Roman', 34), anchor=tk.CENTER)

        create_disk(canvas_main, 250, 800, tower_source_rod, len(tower_source_rod))
        create_disk(canvas_main, 950, 800, tower_auxiliary_rod, len(tower_auxiliary_rod))
        create_disk(canvas_main, 1645, 800, tower_destination_rod, len(tower_destination_rod))

        label_round.config(text=f'Total Rounds: {move_count} for {disk_number} disks')
        canvas_main.update()

    # Perform starting point for this algorithm recursion
    if n > 0:
        hanoi_recursive(n - 1, start_rod, middle_rod, end_rod)

        if start_rod:
            end_rod.append(start_rod.pop())
            move_count += 1

        update_canvas_recursive()
        window_main.update_idletasks()
        window_main.update()
        time.sleep(0.1) # delay function for visualization

        hanoi_recursive(n - 1, middle_rod, end_rod, start_rod) # move the n-1 disks

# This function define to simulate Tower of Hanoi algorithm iteratively.
# All operations are the same as in the simulate_recursive function
def simulate_iterative():
    global disk_number, tower_source_rod, tower_auxiliary_rod, tower_destination_rod, move_count, label_round, canvas_main, window_main, entry

    init_towers()
    create_main_window()

    if not entry.get().isdigit():
        error_label.config(text="Invalid input. Please enter a valid number.", fg="red")
    else:
        disk_number = int(entry.get())
        if disk_number < 1:
            error_label.config(text="Number must be 1 or greater.", fg="red")
        else:
            error_label.config(text="")
            simulate_iterative_hanoi()

# This function simulate Tower of Hanoi iteratively and record the time for runtime calculation
# All operations are the same as in the simulate_recursive_hanoi function
def simulate_iterative_hanoi():

    global move_count
    move_count = [0]

    start_time = time.time()
    hanoi_iterative_gui(disk_number, tower_source_rod, tower_destination_rod, tower_auxiliary_rod, move_count, label_round)
    end_time = time.time()

    run_time = end_time - start_time
    print(f"Iterative Total Rounds: {move_count[0]} for {disk_number} disks")
    print(f"Iterative Total Runtime: {run_time} seconds")

'''
Main operations are here for implementing and creating iterative function.
The iterative algorithm function will be different recursive algorithm.
The recursive algorithm just run with calling function and some conditions but in the iterative 
function we have to create stack and check stack states in every step.
We have to do pop and push operations. Here iterative function for our iterative algorithm...
'''
def hanoi_iterative_gui(n, start_rod, end_rod, middle_rod, move_count, label_round):
    stack = [(n, start_rod, end_rod, middle_rod)]

    # In this function cheks stack şs empty or not if we have one disk, we can move and update canvas
    # othwerwise pop current state and push state for moving n-1 disks operations are made from the stack in here
    def update_operations_for_interface():
        if stack:
            nonlocal move_count
            n, start, end, middle = stack[-1]

            if n == 1:
                move_count[0] += 1
                end.append(start.pop())
                update_canvas_iterative()
                stack.pop()
            else:
                stack.pop()
                stack.append((n - 1, middle, end, start))
                stack.append((1, start, end, middle))
                stack.append((n - 1, start, middle, end))
                update_canvas_iterative()

    # In this function, updates operations according to canvas during all iterative steps
    def update_canvas_iterative():

        canvas_main.delete("all") # deleting elements

        platform = canvas_main.create_rectangle(0, 725, 1920, 1080, fill='grey')
        source_rod = canvas_main.create_rectangle(250, 850, 275, 50, fill='red')
        canvas_main.create_text(250, 900, text='Source Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
        destination_rod = canvas_main.create_rectangle(950, 850, 975, 50, fill='red')
        canvas_main.create_text(950, 900, text='Auxiliary Rod', font=('Times New Roman', 34), anchor=tk.CENTER)
        auxiliary_rod = canvas_main.create_rectangle(1645, 850, 1670, 50, fill='red')
        canvas_main.create_text(1645, 900, text='Destination Rod', font=('Times New Roman', 34), anchor=tk.CENTER)

        create_disk(canvas_main, 250, 800, tower_source_rod, len(tower_source_rod))
        create_disk(canvas_main, 950, 800, tower_auxiliary_rod, len(tower_auxiliary_rod))
        create_disk(canvas_main, 1645, 800, tower_destination_rod, len(tower_destination_rod))

        label_round.config(text=f'Total Rounds: {move_count[0]} for {disk_number} disks')
        canvas_main.update()
        
    # Update and perform iterative function until the stack will be empty...
    while stack:
        update_operations_for_interface()

if __name__ == "__main__":
    disk_number, tower_source_rod, tower_auxiliary_rod, tower_destination_rod, move_count, label_round, canvas_main = 0, [], [], [], 0, None, None
    window_input, entry, error_label = create_get_disk_window()
    window_input.mainloop()