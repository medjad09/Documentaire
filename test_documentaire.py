from DOCUMENTAIRE import Documentaire, Exemplaire

def test_documentaire():
    # Initial count should be 2 because DOCUMENTAIRE.py creates two instances at the bottom
    initial_count = Documentaire._count

    d1 = Documentaire("D1", "T1", "2021-01-01")
    assert d1.n_objet() == initial_count + 1

    d2 = Documentaire("D1", "T1", "2021-01-01")
    assert d2.n_objet() == initial_count + 2

    assert d1.orr(d2) == "egale"

    d3 = Documentaire("D2", "T2", "2021-01-02")
    assert d1.orr(d3) == "n egale"

    expected_ts = "Documentaire [code=D1, titre=T1, date_sortie=2021-01-01]"
    assert d1.Tostring() == expected_ts
    print("Documentaire tests passed")

def test_exemplaire():
    initial_count = Documentaire._count
    e1 = Exemplaire("E1", "T1", "2021-01-01", "N1", "2021-01-02")
    assert e1.n_objet() == initial_count + 1

    expected_ts = "Exemplaire [code=E1, titre=T1, date_sortie=2021-01-01, numero=N1, date_achat=2021-01-02]"
    assert e1.Tostring() == expected_ts

    print("Exemplaire tests passed")

if __name__ == "__main__":
    test_documentaire()
    test_exemplaire()
    print("All tests passed!")
