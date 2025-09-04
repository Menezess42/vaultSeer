from vaultseer.crawler.baseCrawler import BaseCrawler
from pathlib import Path
import json
# GLOBALS CONSTS
AUX_FILES = Path(__file__).parent.parent / "aux_Files"

class ForemanBaseCrawler:
    def __init__(self, newBaseDirs: dict={}) -> None:
        """
        Args:
            newBaseDirs (dictionary, Optional): Dictionary containing new knowledge bases for VaultSeer to consume.
        """
        if newBaseDirs:
            self.newbaseDirs = newBaseDirs
        self.data = {}

    def load_base_dirs(self) -> None:
        """
        Read and validate the directory list from the baseDirs.json file.

        Returns a list of crawler-ready paths.
        """
        with open(f'{AUX_FILES}/baseDirs.json', 'r') as f:
            self.data = json.load(f)

    def run_crawler(self) -> list:
        """
        Runs baseCrawler, passing in the directory list.

        Returns the tree of Node objects representing the found structure.
        """
        baseCrawler = BaseCrawler(self.data)
        return baseCrawler.feedTree(returnTree=True)

    def extract_relevant_info(self):
        """
        For each node in the tree, extract the relevant information (e.g., md header, PDF metadata).

        Returns a list of processed structures.
        """
        ...

    def feed_vector_db(self) -> None:
        """
        Feeds or updates the vector database with the processed information.
        """
        ...

    def orchestrate(self) -> None:
        """
        Central method:
            Loads directories, rusn the crawler, process the tree, and feeds vectorDB.
        """

