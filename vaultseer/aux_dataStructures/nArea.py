from pathlib import Path
class nArea:
    """
    N-Area tree node class.
    """
    def __init__(self, path: Path) -> None:
        """
        Args:
            path (Path): the posix path.

        Returns:
            None.
        """

        self.name = path.name
        self.path = path
        self.is_dir = path.is_dir()
        self.is_file = path.is_file()

        if self.is_file:
            aux = self.name.split(".")
            self.file_type = aux[-1]

        self.children: list[nArea_treeNode] = []

    def add_children(self, child: "nArea_treeNode") -> None:
        """Add the children(s) of the current node.

        Args:
            child (nArea_treeNode): The node that is children of the current node.

        Returns:
                None.
        """
        self.children.append(child)
