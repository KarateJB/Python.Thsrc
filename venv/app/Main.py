
# coding: utf-8
from Apopnd import Apopnd
from Apoload import Apoload
 


def main():
    target_file_path = Apopnd().Apopnd_Thsr()
    print(target_file_path)
    Apoload(target_file_path)

if __name__ == "__main__":
    main()

