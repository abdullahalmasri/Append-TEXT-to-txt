def append_new_line(file_name, text_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_Obj:
        # Move read cursor to the start of file.
        file_Obj.seek(0)
        # If file is not empty then append '\n'
        data = file_Obj.read(100)
        if len(data) > 0:
            file_Obj.write("\n")
            # Append text at the end of file
        file_Obj.write(text_to_append)


# Append one line to a file that does not exist
append_new_line('sample3.txt', 'This is first line')
