from vaultseer.crawler.baseCrawler import BaseCrawler

class OverseerBaseCrawler:
    def __init__(self, newBaseDirs: dict={}) -> None:
        """
        Args:
            newBaseDirs (dictionary): Variable for adding new ....
        """

    def load_base_dirs(self) -> dict:
        ...

    def run_crawler(self) -> list:
        ...

    def extract_relevant_info(self):
        ...

    def feed_vector_db(self) -> None:
        ...

    def overchestrate(self) -> None:
        ...

