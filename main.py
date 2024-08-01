from init import directories, files
import os
import argparse


def project_init(base_path=".", file_ext = ".ts"):

    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)

        if directory in files:
            for file in files[directory]:
                file_path = os.path.join(dir_path, f"{file}.{file_ext}")
                open(file_path, "a").close()

def main():

    parser = argparse.ArgumentParser(description="Initialize Project structure for node application")
    parser.add_argument("path", default=".", help="Base Path for the project directory")
    parser.add_argument("ext", default= ".js", help="File Extension for the files")
    args = parser.parse_args()

    project_init(base_path=args.path, file_ext=args.ext)

if __name__ == "__main__":
    main()
