# Webp Converter
Python command line script to batch convert your .webp files to .png

## Features
- Apply a custom name to the new files
- Search all sub directories for mass conversion
- Place the .webp files in a custom folder

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
This will search all sub directories of the -d directory for .webp files, and then convert them. This is useful if you have multiple webp files scattered about.

### -l Exteded Logging
You can extend the logging to see where each file in being converted from. Here is how that looks:

The default logging looks like this:

- _>> File converted to: C:\Your_Directory\file.png_

Extended logging looks like this:

- _>>Converted from: C:\Your_Directory\origin.png_

- _>> File converted to: C:\Your_Directory\file.png_ 


## Issues
- Animated .webp files are not supported
- Files and Folder names with spaces are not currently supported
- Script exits rather than skipping when an error occurs
