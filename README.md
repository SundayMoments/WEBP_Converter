# Webp Converter
Python command line script to batch convert your .webp files to .png

### To run this script:

Example: python_file.py -d /home/user/webp_files -a -n 'custom_name' -f 'custom_folder_name'

-a, -n, -f, and -l are optional flags. If you do not include -d before your directory, then it will output argument help.
## Features
- Apply a custom name to converted files
- Search all sub directories for .webp files to convert
- Place the .webp files in a folder with a custom name

## Flag Tips
### -f Custom Folder Name

The convertered .webp files will be placed in the -d directory, using the default folder name. 

The default folder name is: converted_pngs

You may choose a custom folder name using the -f flag

### -n Custom Name

If more than one files is being converted using the -n flag, a number will be automatically appended to the end of the file name. It looks like this:

Input  | Output
------------- | -------------
-n Custom_Name  | custom_name.png
-n Custom Name  | custom_name-1.png

### -a All Directories
This will search all sub directories of the -d directory for .webp files, and then convert them. This is useful if you have multiple .webp files scattered about.

### -l Exteded Logging
You can extend the logging to see where each file is being converted from. Additionally it will print the origin of each .webp file. Here is how that looks:

The default logging looks like this:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_>> File converted to: C:\Your_Directory\new_file.png_

Extended logging looks like this:

&nbsp;&nbsp;['origin_file-0.webp', 'origin_file-1.webp']

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_>> Converted from: C:\Your_Directory\origin.png_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_>> File converted to: C:\Your_Directory\new_file.png_ 

## Issues
- Animated .webp files are not supported
- Files and Folder names with spaces are not currently supported
- Flags must be lowercase, otherwise the script will not run
