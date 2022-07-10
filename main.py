import glob
import os
import argparse
from webptools import dwebp

def convert_webp_to_png(directory, all_dirs, custom_name, custom_folder_name, extended_logging):
    """
    Convert all webp files in a directory to png
    Note: Animated WebP files are not supported
    """
    # Change directory to the one specified by the user
    os.chdir(directory)
    
    # Get all webp files in the directory
    if all_dirs == True:
        webp_files = glob.glob(f"{directory}/**/*.webp", recursive=True)
        if extended_logging == True:
            print(webp_files)
    else:
        webp_files = glob.glob(f"{directory}/*.webp")
        if extended_logging == True:
            print(webp_files)

    # If no webp files are found, exit
    if len(webp_files) == 0:
        return print(f"No webp files found in: [{directory}]")
    else:
        print(f"\nProcessing ({len(webp_files)}) file(s) to png...")
    # If no custom folder name is specified, create a folder called 'converted_pngs'

    if custom_folder_name == None:
        if os.path.exists(directory + f'/converted_pngs/'):
            pass
        else:
            print(f"Directory [{directory + f'/converted_pngs/'}] does not exist, creating...")
            os.mkdir(directory + f'/converted_pngs/')
    else:
        if os.path.exists(directory + f'/{custom_folder_name}/'):
            pass
        else:
            print(f"Directory [{directory + f'/{custom_folder_name}/'}] does not exist, creating...")
            os.mkdir(directory + f'/{custom_folder_name}/')
    
                    
    # Convert all webp files to png. 
    # If no custom name is specified, use the original file name
    for file in webp_files:
        if custom_name == None:
            if custom_folder_name == None:
                new_file = f"{directory}/converted_pngs/{os.path.basename(file)[:-4]}png" 
            elif custom_folder_name != None:
                new_file = f"{directory}/{custom_folder_name}/{os.path.basename(file)[:-4]}png" 
            else:
            # If only one webp file is found, use the custom name specified by the user
                new_file = f"{directory}/{custom_folder_name}/{os.path.basename(file)[:-4]}png" 
        else:
            if len(webp_files) == 1:
                if custom_folder_name == None:
                    new_file = f"{directory}/converted_pngs/{custom_name}.png"
                else:
                    new_file = f"{directory}/{custom_folder_name}/{custom_name}.png"
            else:
                # If multiple webp files are found, use the custom name specified by the user and add a number to the end
                if custom_folder_name == None:
                    new_file = f"{directory}/converted_pngs/{custom_name}-{webp_files.index(file)}.png"
                else:
                    new_file = f"{directory}/{custom_folder_name}/{custom_name}-{webp_files.index(file)}.png"
        # Convert the webp file to png
        if extended_logging == True:
            print(f" >> Converting from: {file}")
        dwebp(input_image=file, output_image=new_file, option="-o", logging="-v")
        # If the file is converted, print the path
        if os.path.exists(new_file):
            print(f"  >> File converted to: {new_file}")
        else:
            # If the file is not converted, return an error
            print(F"  >> File Skipped. [{file}] Check your directory. Folders with whitepsace are not currently supported.")
            
    # Print the relative directory where the files are located
    if custom_folder_name == None:
        print(f"Converted file location: [{directory}/converted_pngs/]")
    else:
        print(f"Converted file location: [{directory}/{custom_folder_name}/]")

def main():
    parser = argparse.ArgumentParser(description="Convert webp files to png")
    parser.add_argument("-d", "--directory", help="Directory of webp files", required=False)
    parser.add_argument("-a", "--all_dirs", help="Search all sub directories for webp files", action="store_true", required=False)
    parser.add_argument("-n", "--custom_name", help="Custom name for the file", required=False)
    parser.add_argument("-f", "--custom_folder_name", help="Custom name for the folder", required=False)
    parser.add_argument("-l", "--extended_logging", help="From audit log\debugging", action="store_true", required=False)
    args = parser.parse_args()

    # If no directory is specified, print help and exit
    if args.directory == None:
        parser.print_help()
        return print("\nExample: python file.py -d /home/user/webp_files -a -n 'custom_name' -f 'custom_folder_name'\nWARNING: Folder names with spaces are not currently supported.")
        
    convert_webp_to_png(args.directory, args.all_dirs, args.custom_name, args.custom_folder_name, args.extended_logging)

if __name__ == "__main__":
    main() 