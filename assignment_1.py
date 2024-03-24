
# merge_files function takes in three files and merges them into a single file
def merge_files(file1, file2, file3):
    files = [file1, file2, file3]
    # Open a new file to write the merged files to
    with open('final_file.txt', 'w') as newfile:
        for file in files:
            # Open each file and read its contents
            with open(file) as file:
                contents = file.read()
                newfile.write(contents)
                newfile.write('\n')


#merge_files('final_ibutils2 1.html', 'final_opensm 1.html', 'final_sharp 1.html')