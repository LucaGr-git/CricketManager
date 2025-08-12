import glob, os, tkinter.messagebox
from tkinter import *
from tkinter import _setit

if True:
    total = open('files/Total_Season.txt', 'r')
    lines = total.readlines()
    total.close()
    try:
        lines[10]

    except IndexError:
        add_player = Tk()
        # window title
        add_player.title('')
        # window size
        add_player.geometry('1152x648')
        add_player.resizable(False, False)
        add_player.config(bg='#fcc777')

        # variables
        first_player_name = StringVar()
        last_player_name = StringVar()


        def Add(first_name, last_name):
            player = first_name + ' ' + last_name

            total = open('files/Total_Season.txt', 'r')
            try:
                for line in total:
                    total_line_info = line.strip().split(",")

                    if player == total_line_info[0]:
                        total.close()
                        first_player_name.set('')
                        last_player_name.set('')
                        tkinter.messagebox.askretrycancel('Player already exists',
                                                          'Please retry and input a player that does not already exist')
                        return
            except IndexError:
                pass

            total.close()
            if ',' in player:
                tkinter.messagebox.askretrycancel('Error', 'Please retry, you cannot use "," in the players name')

            else:
                total = open('files/Total_Season.txt', 'a')
                total.write(str(player) + ',0,0\n')
                total.close()

                try:
                    total = open('files/Total_Season.txt', 'r')
                    lines = total.readlines()
                    total.close()
                    lines[10] = lines[10]
                    tkinter.messagebox.showinfo('Completed',
                                                'You now have 11 players in your season, if you want to add more go to the lookup page')
                    add_player.destroy()
                    return


                except IndexError:
                    first_player_name.set('')
                    last_player_name.set('')

                    return


        # Labels
        Label(add_player, text='Add Players', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()
        Label(add_player, text='Add players so you have at least 11', bg='#fcc777',
              font=('Franklin Gothic Book', 12, 'bold')).pack()

        Label(add_player, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()
        Label(add_player, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()

        # Widgets
        # Title Label
        Label(add_player, text='Player Name', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()

        # Entry Box
        Label(add_player, text='First Name', bg='#fcc777', font=('Franklin Gothic Book', 10, 'bold')).pack()
        Entry(add_player, textvariable=first_player_name, bg='#FC9979',
              font=('Franklin Gothic Book', 25, 'bold')).pack()

        Label(add_player, text='Second Name', bg='#fcc777', font=('Franklin Gothic Book', 10, 'bold')).pack()
        Entry(add_player, textvariable=last_player_name, bg='#FC9979', font=('Franklin Gothic Book', 25, 'bold')).pack()

        # Create player button
        Button(add_player, text='Add Player', font=('Franklin Gothic Book', 12, 'bold'),
               command=lambda: Add(first_player_name.get(), last_player_name.get())).pack()

        add_player.mainloop()

total.close()
del lines


def Edit(gamefile_path):
    edit = Tk()
    # window title
    edit.title('Edit a Game')
    # window size
    edit.geometry('1152x648')
    edit.resizable(False, False)
    edit.config(bg='#fcc777')

    # variables
    window_target = StringVar()
    wickets = IntVar()
    runs = IntVar()
    player_choice = StringVar()

    def Menu_Toggle(menu_choice):
        # reads the wickets and runs of the selected player and changes the IntVar's to display the correct values
        file = open(gamefile_path, 'r')
        for line in file:
            total_line_info = line.strip().split(",")
            if total_line_info[0] == menu_choice:
                runs.set(total_line_info[1])
                wickets.set(total_line_info[2])

                return

    # creates a list of the players in the gamefile
    file = open(gamefile_path, 'r')
    players = []

    for line in file:
        total_line_info = line.strip().split(",")
        players.append(total_line_info[0])

    # checks if whether there are 11 or 12 players and makes seperate optionmenu's accordingly
    try:
        players[11] = players[11]
        playermenu = OptionMenu(edit, player_choice, players[0], players[1], players[2], players[3], players[4],
                                players[5], players[6], players[7], players[8], players[9], players[10], players[11],
                                command=lambda x: Menu_Toggle(player_choice.get()))
        playermenu.place(x=900, y=100)
        player_choice.set(players[0])
        file.close()
        Menu_Toggle(player_choice.get())

    except IndexError:
        playermenu = OptionMenu(edit, player_choice, players[0], players[1], players[2], players[3], players[4],
                                players[5], players[6], players[7], players[8], players[9], players[10],
                                command=lambda x: Menu_Toggle(player_choice.get()))
        playermenu.place(x=950, y=100)
        player_choice.set(players[0])
        file.close()
        Menu_Toggle(player_choice.get())

    def Run_Wicket(current_runs_wickets, num, menu_choice, run_mode):
        # check what mode it is in (run/wickets) and checks if they are trying to go under 0
        if run_mode:
            if runs.get() <= 0 and num == -1:
                return

            runs.set(current_runs_wickets + num)
        else:
            if wickets.get() <= 0 and num == -1:
                return

            wickets.set(current_runs_wickets + num)

        for i in range(1, 3):
            # changes the total and gamefile text values so that the runs are added by 1
            line_number = -1

            if i == 1:
                file = open(gamefile_path, 'r')
            else:
                file = open('files/Total_Season.txt', 'r')

            for line in file:

                total_line_info = line.strip().split(",")
                line_number += 1
                if total_line_info[0] == menu_choice:

                    if i == 1:
                        write = open(gamefile_path, 'r')
                    else:
                        write = open('files/Total_Season.txt', 'r')

                    list_of_lines = write.readlines()

                    if run_mode:
                        new_runs_wickets = int(total_line_info[1]) + num
                        list_of_lines[line_number] = total_line_info[0] + ',' + str(new_runs_wickets) + ',' + \
                                                     total_line_info[2] + '\n'
                    else:
                        new_runs_wickets = int(total_line_info[2]) + num
                        list_of_lines[line_number] = total_line_info[0] + ',' + total_line_info[1] + ',' + str(
                            new_runs_wickets) + '\n'

                    if i == 1:
                        write = open(gamefile_path, 'w')

                    else:
                        write = open('files/Total_Season.txt', 'w')

                    write.writelines(list_of_lines)
                    write.close()

    # backarrow button
    photo = PhotoImage(file="images/backarrow.png")
    But = Button(edit, width=25, height=25, image=photo, compound=CENTER, command=lambda: Window_Change('Game Mode'))
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-2)

    # end editing button
    Button(edit, text='Finish Editing Game', command=lambda: Window_Change('Game Mode'), width=20, height=8).place(
        x=900, y=450)

    # labels
    Label(edit, text='Runs', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).place(x=175, y=1)
    Label(edit, text='Wickets', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold'), fg='white').place(x=600, y=1)

    # label that gets the gamefile path and removes the files/ at the start and the .txt at the end
    Label(edit, text=(gamefile_path[6:])[:-4], bg='#fcc777', font=('Franklin Gothic Book', 18, 'bold')).place(x=900,
                                                                                                              y=1)

    # Buttons
    # up arrow button
    photo1 = PhotoImage(file="images/up_arrow.png")
    But = Button(edit, width=64, height=16, image=photo1, compound=CENTER, command=lambda: Run_Wicket(runs.get(), 1, player_choice.get(), True))
    But.place(x=175, y=75)
    But.config(relief='flat', bd=-2)

    # down arrow button
    photo2 = PhotoImage(file="images/down_arrow.png")
    But = Button(edit, width=64, height=16, image=photo2, compound=CENTER, command=lambda: Run_Wicket(runs.get(), -1, player_choice.get(), True))
    But.place(x=175, y=450)
    But.config(relief='flat', bd=-2)

    # up arrow button
    photo3 = PhotoImage(file="images/up_arrow.png")
    But = Button(edit, width=64, height=16, image=photo3, compound=CENTER, command=lambda: Run_Wicket(wickets.get(), 1, player_choice.get(), False))
    But.place(x=600, y=75)
    But.config(relief='flat', bd=-2)

    photo4 = PhotoImage(file="images/down_arrow.png")
    But = Button(edit, width=64, height=16, image=photo4, compound=CENTER, command=lambda: Run_Wicket(wickets.get(), -1, player_choice.get(), False))
    But.place(x=600, y=450)
    But.config(relief='flat', bd=-2)



    # displays
    Label(edit, textvariable=runs, bg='#fcc777', font=('Franklin Gothic Book', 185, 'bold')).place(x=135, y=120)

    Label(edit, textvariable=wickets, bg='#fcc777', fg='white', font=('Franklin Gothic Book', 185, 'bold')).place(x=560,
                                                                                                                  y=120)

    def Window_Change(target):
        window_target.set(target)
        edit.destroy()

    edit.mainloop()

    if window_target.get() == 'Game Mode':
        return Game_Mode()


def Login():
    # defines tkinter variable
    login = Tk()
    # window title
    login.title('Login')
    # background
    login.config(bg='purple')
    # window size
    login.resizable(False, False)
    login.geometry('650x400')
    # Entry box variable for username
    username = StringVar()
    # Entry box variable for password
    password = StringVar()
    # password true variable
    correct = BooleanVar()
    correct.set(False)
    # user choice variable
    user_choice = StringVar()

    def Stats_Load(mode):
        # checks current mode and changes a variable based on it
        if mode == 'Runs':
            mode = 1
        elif mode == 'Wickets':
            mode = 2

        # clears output boxes
        NameBox.delete(0, 'end')
        ValueBox.delete(0, 'end')

        # dictionary for players as keys and stats as values
        stats = {}

        total = open('files/Total_Season.txt', 'r')
        for line in total:
            lineInfo = line.strip().split(",")
            # appends the name as keys and uses mode to sort the value placed in the dictionary
            stats[lineInfo[0]] = lineInfo[mode]
        total.close()

        # makes an ordered list (High-Low) of player's stats
        top_players = (sorted(stats.keys(), key=lambda x: stats[x], reverse=True))

        # output the top 10 players and stats
        for i in range(0, 10):
            NameBox.insert(i, (' ' + str(i + 1) + '. ' + top_players[i]))
            ValueBox.insert(i, (' ' + stats[top_players[i]]))

    def Submit(password_input, username_input):
        file = open('passwords.txt', 'r')
        for line in file:
            lineInfo = line.strip().split(",")
            if username_input == lineInfo[0] and password_input == lineInfo[1]:
                file.close()
                correct.set(True)
                login.destroy()
                return

        file.close()
        password.set('')
        tkinter.messagebox.askretrycancel('Incorrect', 'That username or password is incorrect')

    def Enter(*args):
        if str(login.focus_get()) == '.!entry':
            password_entry.focus_set()
        else:
            Submit(password.get(), username.get())

    # backarrow button
    photo = PhotoImage(file="images/logo.png")
    But = Button(login, width=325, height=200, image=photo, compound=CENTER, bg='purple')
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-2)

    # Username Label and Entry
    Label(login, text='Username: ', bg='white', fg='purple').place(x=20, y=230)
    username_entry = Entry(login, textvariable=username, bg='silver')
    username_entry.place(x=20, y=250)

    # Password Label and Entry
    Label(login, text='Password:  ', bg='white', fg='purple').place(x=20, y=270)
    password_entry = Entry(login, textvariable=password, bg='silver', show='*')
    password_entry.place(x=20, y=290)

    # Button for submitting
    Button(login, text='   Submit   ', bg='spring green', fg='purple',
           command=lambda: Submit(password.get(), username.get())).place(x=20, y=310)

    # ListBoxes
    NameBox = Listbox(login, height=20, width=25, font=('arial', 10, 'bold'))
    NameBox.place(x=325, y=35)
    NameBox.config(relief='flat', bd=-2)

    ValueBox = Listbox(login, height=20, width=15, font=('arial', 10, 'bold'))
    ValueBox.place(x=498, y=35)
    ValueBox.config(relief='flat', bd=-2)

    # optionmenu
    OptionMenu(login, user_choice, 'Runs', 'Wickets', command=lambda x: Stats_Load(user_choice.get())).place(x=498, y=1)
    user_choice.set('Runs')

    # Label
    Label(login, text='Leaderboard', font=('arial', 16, 'bold'), bg='purple', fg='white').place(x=325, y=1)

    # spacing labels
    #Label(login, text='      ', bg='purple').grid(row=0, column=0)
    #Label(login, text='      ', bg='purple').grid(row=100, column=100)

    login.bind('<Return>', Enter)

    Stats_Load(user_choice.get())

    login.mainloop()

    if correct.get():
        return Game_Mode()


def Lookup():
    lookup = Tk()
    # window title
    lookup.title('Edit a Game')
    # window size
    lookup.geometry('1152x648')
    lookup.resizable(False, False)
    lookup.config(bg='#c972f1')
    # variables
    window_target = StringVar()

    def Delete_Player():
        # checking if he correct listbox is in focus
        if str(lookup.focus_get()) == '.!frame.!listbox':
            pass

        else:
            tkinter.messagebox.askretrycancel('No Player Selected', 'Please select a player to delete')
            return

        # checking if the user has at least 12 players to delete a player
        total = open('files/Total_Season.txt', 'r')
        try:
            line_list = total.readlines()
            line_list[11] = line_list[11]
            total.close()

        except IndexError:
            total.close()
            tkinter.messagebox.askretrycancel('Not enough players',
                                              'You must have at least 12 players to delete a player')
            return

        # gets cwd (current working directory)
        owd = os.getcwd()

        # changes cwd to "files/"
        os.chdir('files/')

        # for loop for all files in the files/ directory
        for file in glob.glob("*.txt"):
            # if the file is not the total file
            if file != "Total_Season.txt":
                file = open(str(file), 'r')
                for line in file:
                    total_line_info = line.strip().split(",")
                    # if the selected player is in a gamefile
                    if total_line_info[0] == NameBox.get(NameBox.curselection())[1:]:
                        file.close()
                        os.chdir(owd)
                        tkinter.messagebox.askretrycancel('Player in a game',
                                                          'A player cannot be deleted if the player is in a gamefile')
                        return

        # reverts to original cwd
        os.chdir(owd)
        selected_player = NameBox.get(NameBox.curselection())[1:]

        delete = Toplevel()
        delete.config(bg='#c972f1')
        delete.grab_set()

        # variables
        window_targ = StringVar()

        # label
        Label(delete, text='Are you sure you want to delete "' + NameBox.get(NameBox.curselection())[1:] + '"',
              font=('Franklin Gothic Book', 13, 'bold'), bg='#c972f1').pack()

        # buttons
        Button(delete, text='Yes', command=lambda: Yes(), width=10).pack()

        Button(delete, text='No', command=lambda: No(), width=10).pack()

        def No():
            delete.destroy()

        def Yes():
            file = open('files/Total_Season.txt', 'r')
            # variable for keeping track of line in txt file
            line_num = -1

            for line in file:
                total_line_info = line.strip().split(",")
                line_num += 1
                # if the name in the line matches the selected Name
                if total_line_info[0] == selected_player:
                    # deletes the line that the player that was selected is on
                    write = open('files/Total_Season.txt', 'r')
                    line_list = write.readlines()
                    del line_list[line_num]
                    write = open('files/Total_Season.txt', 'w')
                    write.writelines(line_list)
                    write.close()

            # closes file/window and refreshes players
            file.close()
            delete.destroy()
            return Total_Stats_Load()

    def Total_Stats_Load():
        # resets the Listboxes with the new player information
        total = open('files/Total_Season.txt', 'r')
        outputline = -1
        NameBox.delete('0', 'end')
        RunsBox.delete('0', 'end')
        WicketsBox.delete('0', 'end')
        for line in total:
            total_line_info = line.strip().split(",")

            outputline += 1

            NameBox.insert(outputline, (' ' + total_line_info[0]))
            RunsBox.insert(outputline, (' ' + total_line_info[1]))
            WicketsBox.insert(outputline, (' ' + total_line_info[2]))

    def Add_Player():
        # toplevel that gives the user a menu to add a player into their roster
        add = Toplevel()
        add.geometry('200x130')
        add.config(bg='#c972f1')
        add.grab_set()

        # variables
        first_player_name = StringVar()
        last_player_name = StringVar()

        def Cancel():
            add.destroy()
            return Total_Stats_Load()

        def Submit(first_name, last_name):
            player = first_name + ' ' + last_name

            total = open('files/Total_Season.txt', 'r')
            try:
                for line in total:
                    total_line_info = line.strip().split(",")

                    if player == total_line_info[0]:
                        total.close()
                        first_player_name.set('')
                        last_player_name.set('')
                        tkinter.messagebox.askretrycancel('Player already exists',
                                                          'Please retry and input a player that does not already exist')
                        return

            except IndexError:
                pass

            total.close()

            if ',' in player:
                tkinter.messagebox.askretrycancel('Error', 'Please retry, you cannot use "," in the players name')
            else:

                total = open('files/Total_Season.txt', 'a')
                total.write(str(player) + ',0,0\n')
                total.close()
                first_player_name.set('')
                last_player_name.set('')

                return Cancel()

        # First name Label and Entry
        Label(add, text='First name:', bg='#c972f1').pack()
        Entry(add, textvariable=first_player_name).pack()

        # Second name Label and Entry

        Entry(add, textvariable=last_player_name).pack()

        # buttons
        Button(add, text='Add Player',
               command=lambda: Submit(first_player_name.get(), last_player_name.get())).pack()

        Button(add, text='Cancel',
               command=lambda: Cancel()).pack()

    # scrollbar
    frame = Frame(lookup, bg='#c972f1')
    scrollbar = Scrollbar(frame, orient=VERTICAL)

    # back arrow button
    photo = PhotoImage(file="images/backarrow.png")
    But = Button(lookup, width=25, height=25, image=photo, compound=CENTER, command=lambda: Window_Change('Game Mode'))
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-2)

    # labels
    Label(lookup, text='     Total Season Stats', bg='#c972f1', font=('Franklin Gothic Book', 25, 'bold')).place(x=30,
                                                                                                                 y=1)

    Label(lookup, text='Names', bg='#c972f1', font=('Franklin Gothic Book', 11, 'bold')).place(x=5, y=42)
    Label(lookup, text='Runs', bg='#c972f1', font=('Franklin Gothic Book', 11, 'bold')).place(x=350, y=42)
    Label(lookup, text='Wickets', bg='#c972f1', font=('Franklin Gothic Book', 11, 'bold')).place(x=600, y=42)

    # output box
    NameBox = Listbox(frame, height=33, width=50, font=('arial', 10, 'bold'), yscrollcommand=scrollbar.set)
    NameBox.place(x=2, y=70)
    NameBox.config(relief='flat', bd=-2)

    RunsBox = Listbox(frame, height=33, width=36, font=('arial', 10, 'bold'), yscrollcommand=scrollbar.set)
    RunsBox.place(x=350, y=70)
    RunsBox.config(relief='flat', bd=-2)

    WicketsBox = Listbox(frame, height=33, width=50, font=('arial', 10, 'bold'), yscrollcommand=scrollbar.set)
    WicketsBox.place(x=600, y=70)
    WicketsBox.config(relief='flat', bd=-2)

    # Button
    Button(lookup, text='Add a Player', height=2, command=lambda: Add_Player()).place(x=955, y=540)
    Button(lookup, text='Delete Selected Player', height=2, command=lambda: Delete_Player()).place(x=955, y=500)

    # configure scrollbar and scrolling function
    def scroll(*args):
        NameBox.yview(*args)
        RunsBox.yview(*args)
        WicketsBox.yview(*args)

    scrollbar.config(command=scroll)
    scrollbar.pack(side=RIGHT, fill=Y)
    frame.pack(expand=1, fill=BOTH)

    def Window_Change(target):
        window_target.set(target)
        lookup.destroy()

    # loads stats from text file on window startup
    Total_Stats_Load()

    lookup.mainloop()

    if window_target.get() == 'Game Mode':
        return Game_Mode()


def Choose(gamefile_path):
    choose = Tk()
    # window title
    choose.title('Choose the players')
    # window size
    choose.resizable(False, False)
    choose.config(bg='#fdce50')
    # variables
    Name_Choice = StringVar()
    window_target = StringVar()

    players_list = []

    # title label
    Label(choose, text='Choose the players for your game', font=('Franklin Gothic Book', 15, 'bold'),
          bg='#fdce50').pack()

    # makes an optionmenu that has in it every name in the total roster
    total_players = []
    total = open('files/Total_Season.txt', 'r')
    for line in total:
        total_line_info = line.strip().split(",")
        total_players.append(total_line_info[0])
    total.close()

    Names = OptionMenu(choose, Name_Choice, *total_players)
    Name_Choice.set(total_players[0])
    Names.pack()

    # buttons
    Button(choose, text='Add Player to game', command=lambda: Add_Player(Name_Choice.get())).pack()

    def End_Choosing():
        window_target.set('Edit')
        choose.destroy()

    def Add_Player(choice):
        # adds their choice to a list
        players_list.append(choice)

        # reset's choice and deletes all options in the optionmenu
        Name_Choice.set('')
        Names['menu'].delete(0, 'end')

        # removes the current choice from the total players list
        total_players.remove(choice)

        # inserts new options into the optionmenu
        for select in total_players:
            Names['menu'].add_command(label=select, command=_setit(Name_Choice, select))

        # writes the users choice into the gamefile
        file = open(gamefile_path, 'a')
        file.write(choice + ',0,0\n')
        file.close()

        # has different paths on whether there are less than 11, 11 or 12 players
        try:
            players_list[11] = players_list[11]
            return End_Choosing()

        except IndexError:
            pass

        try:
            players_list[10] = players_list[10]
            try:
                total = open('files/Total_Season.txt', 'r')
                total_line = total.readlines()
                total.close()

                total_line[10] = total_line[10]
                del total_line

                Button(choose, text='End Player Choosing', command=lambda: End_Choosing()).pack()
                Name_Choice.set(total_players[0])
                tkinter.messagebox.showinfo('You can finish now',
                                            'You have 11 players on your team now, you can finish selecting players now by pressing "End Player Choosing" or add 1 last player')
                return

            except IndexError:
                return End_Choosing()

        except IndexError:
            pass

        # sets users choice to the first one
        Name_Choice.set(total_players[0])

    choose.mainloop()

    if window_target.get() == 'Edit':
        return Edit(gamefile_path)

    # if the user closes window midway through selection the file will be deleted
    else:
        os.remove(gamefile_path)


def Create():
    create = Tk()
    # window title
    create.title('Create New Game')
    # window size
    create.geometry('1152x648')
    create.resizable(False, False)
    create.config(bg='#fcc777')
    # variables
    window_target = StringVar()
    Text_File_Name = StringVar()

    def New_Game(gamefile_path):
        try:
            file = open(gamefile_path, 'r')
            tkinter.messagebox.askretrycancel('File already exists',
                                              'Please retry and input a game file that does not already exist')
            file.close()
            Text_File_Name.set('')

        except FileNotFoundError:
            file = open(gamefile_path, 'w')
            file.close()

            return Window_Change('Choose')

    # FILLERS
    Label(create, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()
    Label(create, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()
    Label(create, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()
    Label(create, text='', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()

    # Widgets
    # Title Label
    Label(create, text='Game Name', bg='#fcc777', font=('Franklin Gothic Book', 25, 'bold')).pack()

    # Entry Box
    entry = Entry(create, text=Text_File_Name, bg='#FC9979', font=('Franklin Gothic Book', 25, 'bold'))
    entry.pack()

    # Create Game button
    Button(create, text='Create Game', font=('Franklin Gothic Book', 12, 'bold'),
           command=lambda: New_Game('files/' + Text_File_Name.get() + '.txt')).pack()

    # back arrow button
    photo = PhotoImage(file="images/backarrow.png")
    But = Button(create, width=25, height=25, image=photo, compound=CENTER, command=lambda: Window_Change('Game Mode'))
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-2)

    def Window_Change(target):
        window_target.set(target)
        create.destroy()

    def Enter(*args):
        return New_Game('files/' + Text_File_Name.get() + '.txt')

    entry.bind('<Return>', Enter)

    create.mainloop()

    if window_target.get() == 'Game Mode':
        return Game_Mode()
    if window_target.get() == 'Choose':
        return Choose('files/' + Text_File_Name.get() + '.txt')


def Load():
    load = Tk()
    # window title
    load.title('Edit a Game')
    # window size
    load.geometry('1152x648')
    load.resizable(False, False)
    load.config(bg='#9796C2')

    # variables
    window_target = StringVar()
    gamefile_path = StringVar()

    def Load_Game():
        # checks if the listbox is in focus and if it is it opens the edit window with the correct gamefile that is in focus
        if str(load.focus_get()) == '.!listbox':
            gamefile_path.set('files/' + (FileBox.get(FileBox.curselection())[1:]) + '.txt')
            window_target.set('Edit')
            load.destroy()

        else:
            tkinter.messagebox.askretrycancel('No Game Selected', 'Please select a game to load')

    def Delete_Game():
        # checks if the listbox is in focus and if it is it opens the delete window
        if str(load.focus_get()) == '.!listbox':
            delete = Toplevel(load)
            # window title
            delete.title('')
            # window size
            delete.resizable(False, False)
            delete.config(bg='#9796C2')
            # variables
            file_path = 'files/' + (FileBox.get(FileBox.curselection())[1:]) + '.txt'

            # Label
            Label(delete, text='Are you sure you want to delete "' + FileBox.get(FileBox.curselection())[1:] + '"',
                  font=('Franklin Gothic Book', 13, 'bold'), bg='#9796C2').pack()

            # buttons
            Button(delete, text='Yes', command=lambda: Yes(), width=10).pack()

            Button(delete, text='No', command=lambda: No(), width=10).pack()

            def Yes():
                # deletes game and removes all of the scores from game from the total folder
                file = open(file_path, 'r')

                # checks the file about to be deleted line by line
                for file_line in file:
                    file_line_info = file_line.strip().split(",")
                    # keeps track of what line the matching name is on
                    line = -1
                    # every line that is checked on the file about to be deleted goes through every line in the total file
                    total = open('files/Total_Season.txt', 'r')
                    for total_line in total:
                        line += 1
                        total_line_info = total_line.strip().split(",")

                        # if the two lines(total and about to be deleted) are the same the if statement goes through
                        if file_line_info[0] == total_line_info[0]:
                            # calculates the stats of the player in the total file subtracted by the same player in the game file
                            result = total_line_info[0] + ',' + str(int(total_line_info[1]) - int(file_line_info[1])) + ',' + str(int(total_line_info[2]) - int(file_line_info[2])) + '\n'

                            # opens the total file and reads its line into a list file then changs the line that the matching player name is on to be the new result
                            write = open('files/Total_Season.txt', 'r')
                            line_list = write.readlines()
                            line_list[line] = result

                            # writes changes and closes file
                            write = open('files/Total_Season.txt', 'w')
                            write.writelines(line_list)
                            write.close()

                # closes files opens
                file.close()
                total.close()
                # deletes the file that has just been sutracted from total
                os.remove(file_path)
                # destroys toplevel window
                delete.destroy()
                Refresh()

            def No():
                delete.destroy()


        else:
            tkinter.messagebox.askretrycancel('No Game Selected', 'Please select a game to delete')

    # scrollbar
    scrollbar = Scrollbar(load, orient=VERTICAL)

    # Labels
    Label(load, text='Load a Game or Delete it', font=('Franklin Gothic Book', 25, 'bold'), bg='#9796C2').place(x=35,
                                                                                                                y=20)

    # Listbox
    FileBox = Listbox(load, height=19, width=75, font=('arial', 18, 'bold'), yscrollcommand=scrollbar.set)
    FileBox.place(x=12, y=70)
    FileBox.config(relief='flat', bd=-2)

    # buttons
    Button(load, text='Load selected Game', command=lambda: Load_Game()).place(x=1000, y=500)

    Button(load, text='Delete selected Game', command=lambda: Delete_Game()).place(x=1000, y=450)

    # backarrow button
    photo = PhotoImage(file="images/backarrow.png")
    But = Button(load, width=25, height=25, image=photo, compound=CENTER, command=lambda: Window_Change('Game Mode'))
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-2)

    # configure scrollbar and scrolling function
    def scroll(*args):
        FileBox.yview(*args)

    scrollbar.config(command=scroll)
    scrollbar.pack(side=RIGHT, fill=Y)

    def Window_Change(target):
        window_target.set(target)
        load.destroy()

    def Refresh():
        # gets cwd
        owd = os.getcwd()

        # clears listbox and shows in the listbox every file in "/files" that is not the total season file
        FileBox.delete(0, 'end')


        # changes cwd to "files/"
        os.chdir('files/')

        line = -1

        for file in glob.glob("*.txt"):
            if file != "Total_Season.txt":
                line += 1
                FileBox.insert(line, (' ' + file[:-4]))

        # reverts to original cwd
        os.chdir(owd)

    Refresh()

    load.mainloop()

    if window_target.get() == 'Edit':
        return Edit(gamefile_path.get())
    if window_target.get() == 'Game Mode':
        return Game_Mode()


def Game_Mode():
    # defines tkinter variable
    game_mode = Tk()
    # window title
    game_mode.title('Choose Cricket Mode')
    # window size
    game_mode.geometry('1152x648')
    game_mode.resizable(False, False)
    # variable
    window_target = StringVar()

    # lookup button
    photo1 = PhotoImage(file="images/lookup.png")
    But1 = Button(game_mode, width=384, height=648, image=photo1, compound=CENTER,
                  command=lambda: Window_Change('Lookup'))
    But1.grid(row=0, column=0)
    But1.config(relief='flat', bd=-5)

    # backarrow button
    photo = PhotoImage(file="images/backarrow.png")
    But = Button(game_mode, width=25, height=25, image=photo, compound=CENTER, command=lambda: Window_Change('Login'))
    But.place(x=1, y=1)
    But.config(relief='flat', bd=-5)

    # create button
    photo2 = PhotoImage(file="images/create.png")
    But2 = Button(game_mode, width=384, height=648, image=photo2, compound=CENTER,
                  command=lambda: Window_Change('Create'))
    But2.grid(row=0, column=1)
    But2.config(relief='flat', bd=-5)

    # load button
    photo3 = PhotoImage(file="images/load.png")
    But3 = Button(game_mode, width=384, height=648, image=photo3, compound=CENTER,
                  command=lambda: Window_Change('Load'))
    But3.grid(row=0, column=2)
    But3.config(relief='flat', bd=-2)

    def Window_Change(target):
        window_target.set(target)
        game_mode.destroy()

    game_mode.mainloop()

    if window_target.get() == 'Lookup':
        return Lookup()
    if window_target.get() == 'Create':
        return Create()
    if window_target.get() == 'Load':
        return Load()
    if window_target.get() == 'Login':
        return Login()



Login()
