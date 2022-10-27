import zipfile
import argparse
from vshell import Vshell


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="C:\\Users\\Timothy\\Desktop\\cm_homeworks\\hw1\\workdir.zip")
    args = parser.parse_args()
    path = args.path
    img = zipfile.ZipFile(path, 'r')
    vs_obj = Vshell(img)
    vs_obj.exec()


if __name__ == "__main__":
    main()
