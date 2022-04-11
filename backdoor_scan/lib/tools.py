def tab_print(printstr: str):
    if len(printstr) < 95:
        print(("| " + "\033[48;5;240m\033[38;5;220m" + printstr + "\033[0;0m"+ "\t|").expandtabs(100))
    else:
        char_count = 0
        printstr_temp = ""
        for char in printstr:
            char_count = char_count + 1
            printstr_temp = printstr_temp + char
            if char_count == 95:
                char_count = 0
                print(("| " + "\033[48;5;240m\033[38;5;220m" + printstr + "\033[0;0m" + "\t|").expandtabs(100))
                printstr_temp = ""
        print(("| " +"\033[48;5;240m\033[38;5;220m" + printstr + "\033[0;0m" + "\t|").expandtabs(100))