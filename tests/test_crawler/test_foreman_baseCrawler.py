from vaultseer.aux_dataStructures.nArea import nArea
from vaultseer.crawler.foreman_baseCrawler import ForemanBaseCrawler


def test_ForemanBaseCrawler_init():
    new_ForemanBC = ForemanBaseCrawler(
        {
            "Test1": {
                "path": "/test1/test1/test",
                "description": "This is the first test",
            },
            "Test2": {
                "path": "/test2/test2/test",
                "description": "This is the first test",
            },
        }
    )
    assert type(new_ForemanBC.newbaseDirs) is dict
    assert sorted(new_ForemanBC.newbaseDirs) == ["Test1", "Test2"]
    assert new_ForemanBC.newbaseDirs["Test1"]["path"] == "/test1/test1/test"


def test_ForemanBaseCrawler_load_base_dirs():
    new_ForemanBC = ForemanBaseCrawler()
    new_ForemanBC.load_base_dirs()
    assert "TomeHold" in new_ForemanBC.data


def test_ForemanBaseCrawler_run_crawler():
    new_ForemanBC = ForemanBaseCrawler()
    new_ForemanBC.load_base_dirs()
    tree_list = new_ForemanBC.run_crawler()
    # assert "TomeHold" in tree_list[0]
    assert type(tree_list[0]) is nArea
    assert tree_list[0].name == "TomeHold"
    assert tree_list[1].name == "Mez2Brain"
