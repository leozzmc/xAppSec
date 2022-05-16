def tab_print(printstr: str, expandNum: int):
    if len(printstr) < 95:
        print(("| " + printstr + "\t|").expandtabs(expandNum))
    else:
        char_count = 0
        printstr_temp = ""
        for char in printstr:
            char_count = char_count + 1
            printstr_temp = printstr_temp + char
            if char_count == 95:
                char_count = 0
                print(("| " +  printstr  + "\t|").expandtabs(expandNum))
                printstr_temp = ""
        print(("| " + printstr  + "\t|").expandtabs(expandNum))