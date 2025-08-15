from vaultseer.aux_dataStructures.nArea import nArea
from pathlib import Path
import json

# GLOBALS CONSTS
AUX_FILES = Path(__file__).parent.parent / "aux_Files"

class BaseCrawler:
    """A base crawler that loads directory apths from a configuration and builds a tree representation of their contentes.

    This class can read a dctionary of base directories from memory or from a JSON file, and travers them to produce hierarchical structures of files and folders using `nArea`.
    """

    def __init__(self, baseDirs: dict={}) -> None:
        """Initialize the BaseCrawler with an optional set of base directories.

        Args:
            baseDir (dict, optional): A mapping where each key is a directory identifier and each value contains directory metadata, including a "path" key pointing to the absolute directory location. Defaults to an empty dictionary.
        """
        self.vectorSize = 0
        self.rootsVector: list[nArea] = []

        if baseDirs:
            self.baseDirs = baseDirs
            self.vectorSize = len(self.baseDir)

    def read_baseDirs(self, file_path: str=f"{AUX_FILES}/baseDirs.json") -> None:
        """Load base directory configuration from a JSON file.

        Args:
            file_path (str, optional): Path to the JSON file containing base directory definitions. Defaults to "vaultSeer/aux_Files/baseDirs.json"

        Returns:
            None
        """
        with open(file_path, 'r') as f:
            self.baseDirs = json.load(f)

        self.vectorSize=len(self.baseDirs)

    def feedTree(self, returnTree: bool=False) -> None | list:
        """Traverse the base directories and build directory trees.

        Each base directory is a scanned interactive, creating an `nArea` tree
        structure representing the hierarchy of folders aand files. These root trees are stored internally in `self.rootsVector`.

        Args:
            returntree (bool, optional): If True, returns the list of generated root tree nodes instead of only storing them internally. Defaults to False.

        Returns:
            None (list): Returns a list of `nArea` objects if `returnTree` is True, otherwise returns None.
        """
        dirQueue = []
        for name in self.baseDirs:
            baseDir_path = Path(self.baseDirs[str(name)]["path"])
            dirTree = nArea(baseDir_path)
            dirQueue.append(dirTree)

            while dirQueue != []:
                cRoot = dirQueue.pop(0)
                for name in cRoot.path.iterdir():
                    newNode = nArea(name)
                    if name.is_dir() and name.name[0] != ".":
                        dirQueue.append(newNode)
                        cRoot.add_children(newNode)
                    elif name.is_file():
                        cRoot.add_child(newNode)

            if dirTree.children != []:
                self.rootsVector.append(dirTree)

        if returnTree:
            return self.rootsVector
