import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph

# @pytest.mark.skip("TODO")
def test_breadth_first_island():
    graph = Graph()
    test = graph.add_node("Test")
    actual = graph.breadth_first(test)
    expected = ["Test"]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_breadth_first_duplicate():
    graph = Graph()
    dup1 = graph.add_node("Duplicate")
    test = graph.add_node("Test")
    dup2 = graph.add_node("Duplicate")
    graph.add_edge(dup1, test)
    graph.add_edge(test,dup1)
    graph.add_edge(test, dup2)
    graph.add_edge(dup2, test)

    actual = graph.breadth_first(dup1)
    expected = ['Duplicate', 'Test', 'Duplicate']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_breadth_first_start_mid():
    graph = Graph()
    left = graph.add_node("Left")
    mid = graph.add_node("Mid")
    right = graph.add_node("Right")
    graph.add_edge(left, mid)
    graph.add_edge(mid,left)
    graph.add_edge(mid, right)
    graph.add_edge(right, mid)

    actual = graph.breadth_first(mid)
    expected = ['Mid', 'Left', 'Right']
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_bfs(graph):
    nodes = graph.get_nodes()
    root = list(nodes)[0]
    print(f"root: {root.value}")
    actual = graph.breadth_first(root)
    expected = ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
    assert actual == expected

    # DANGER: Metroville/Monstropolis could be switched as well as Narnia/Naboo and still be valid BFS. What to do?


@pytest.fixture
def graph():

    realms = Graph()

    pandora = realms.add_node("Pandora")
    arendelle = realms.add_node("Arendelle")
    metroville = realms.add_node("Metroville")
    monstropolis = realms.add_node("Monstropolis")
    narnia = realms.add_node("Narnia")
    naboo = realms.add_node("Naboo")

    realms.add_node("Island")

    realms.add_edge(pandora, arendelle)

    realms.add_edge(arendelle, pandora)
    realms.add_edge(arendelle, metroville)
    realms.add_edge(arendelle, monstropolis)

    realms.add_edge(metroville, arendelle)
    realms.add_edge(metroville, monstropolis)
    realms.add_edge(metroville, narnia)
    realms.add_edge(metroville, naboo)

    realms.add_edge(monstropolis, arendelle)
    realms.add_edge(monstropolis, metroville)
    realms.add_edge(monstropolis, naboo)

    realms.add_edge(narnia, metroville)
    realms.add_edge(narnia, naboo)

    realms.add_edge(naboo, metroville)
    realms.add_edge(naboo, monstropolis)
    realms.add_edge(naboo, narnia)

    return realms
