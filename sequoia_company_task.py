#sequoia program exercise

import sys
import re

#decorated function for finding the time taken
def time_taken(func):
    import timeit
    def inner_fun(self):
        s=timeit.timeit()
        func(self)
        execute_time=(timeit.timeit()-s)
        print("Time taken for reading the file:",execute_time)
    return inner_fun


class File_read:
    def __init__(self,file_name):
        self.file = file_name
        self.data=None

    @time_taken
    def read_file(self):
        with open(self.file) as f:
            self.data=f.read()

    def read_words(self,set_values=False):
        if set_values:
            l=set(self.data.split())
            return len(l)
        else:
            l=self.data.split()
            return len(l)

    def clean_data(self):
        val=re.findall(r'\[\d{1,4}\]',self.data)
        # print(val)
        # print(self.data)
        if val:
            writable_data=re.sub(r'\[\d{1,4}\]', "", self.data)
            with open(self.file,'a+') as f:
                f.writelines("\n------------CLEANED DATA------------\n")
                f.write(writable_data)
            return "File was cleaned successfully"


try:
    file_name=sys.argv[1]
    txt_value=(file_name.rsplit('.',1)[1])
    if txt_value=='txt':
        obj=File_read(sys.argv[1])
        data=obj.read_file()
        print("Number of words in the file:",obj.read_words())
        print("Number of Unique words in the file:",obj.read_words(set_values=True))
        print(obj.clean_data())
    else:
        print("Invalid file type")
except Exception as err:
    print(err)



