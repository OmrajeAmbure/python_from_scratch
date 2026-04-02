"""
 📝 File Handling in Python :-
        - File handling refers to the process of performing operations on a file, such as creating, opening, reading, writing and closing it through a programming interface.
        It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.
        📍 Why do we need File Handling
                - To store data permanently, even after the program ends.
                - To access external files like .txt, .csv, .json, etc.
                - To process large files efficiently without using much memory.
                - To automate tasks like reading configs or saving outputs.
"""
try:
        f = open('example.txt','r');
except OSError as e:
        print(e);
else:
        print(f)
        print("Filename:", f.name)
        print("Mode:", f.mode)
        print("Is Closed?", f.closed)
        print(f.read())
finally:
        f.close();
        print("Is Closed?", f.closed)

"""
📝 Writing a File
        - In Python, writing to a file is done using the mode "w". This creates a new file if it doesn’t exist, 
        or overwrites the existing file if it does. The write() method is used to add content. After writing, make sure to close the file.
        Example: Writing to a file (overwrites if file exists)
        
        Mode / Option	                                        Description
                "w"	                          Write mode: creates file if missing, truncates (erases) if it exists
                "a"                             Append mode: creates file if missing, writes data always at the end
                "x"	                          Exclusive create: creates new file, but fails with FileExistsError if it already exists
                "b"	                          Binary flag: used with other modes (e.g., "wb", "ab") for binary files
                "+"	                          Read/write flag: combine with other modes (e.g., "r+", "w+") for both reading and writing
           encoding=	                      Specify text encoding (e.g., "utf-8") when working with text files
           newline=	                      Control newline translation in text mode (e.g., "\n")
                Note: You can combine flags like "wb" (write + binary) or "a+" (append + read). 
                Always pick a mode based on whether you want to overwrite, append, or strictly create a new file.
                
"""
try:
        f = open('example.txt','a');
except OSError as e:
        print(e);
else:
        f.writelines(" i am aids student at isbm college of Eng.");
finally:
        f.close();
        print("Is Closed?", f.closed)