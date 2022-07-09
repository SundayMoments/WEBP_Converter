# Webp Converter
Python command line script to batch convert your .webp files to .png

## Features
- Apply a custom name to the new files
- Search all sub directories for mass conversion
- Place the .webp files in a custom folder

### Examples
If more than one files is being converted using the -c flag, a number will be automatically appended to the end of the file name.

Here is how that looks:

Input  | Output
------------- | -------------
-c Custom_Name  | custom_name.png
-c Custom Name  | custom_name-1.png

## Issues
- Animated .webp files are not supported
- Files and Folder names with spaces are not currently supported
- Script exits rather than skipping when an error occurs
