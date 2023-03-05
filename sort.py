import argparse
from pathlib import Path
from shutil import copyfile
from multiprocessing import Pool, cpu_count


parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = args.get("source")
output = Path(args.get("output"))


def read_folder(path: Path) -> list:
    list_of_folders = []
    for el in path.iterdir():
        if el.is_dir():
            list_of_folders.append(el)
            result = read_folder(el)
            if len(result):
                list_of_folders += result

    return list_of_folders


def copy_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_path = output / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as error:
                print(error)


if __name__ == "__main__":
    print(read_folder(Path(source)))
    with Pool(cpu_count()) as pool:
        pool.map(copy_file, read_folder(Path(source)))
        pool.close()
        pool.join()
