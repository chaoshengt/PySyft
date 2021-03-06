from syft.generic.string import String


def test_string_methods():
    """Tests some of the `String` methods which are hooked from `str`.
       more tests are to be added
    """

    # Create a string
    string = String("Hello PySyft")

    assert isinstance(string.upper(), String)
    assert isinstance(string.lower(), String)
    assert isinstance(string.title(), String)

    assert string == "Hello PySyft"
    assert string == String("Hello PySyft")

    assert string.upper() == "HELLO PYSYFT"
    assert string.upper() == String("HELLO PYSYFT")

    assert string.lower() == "hello pysyft"
    assert string.lower() == String("hello pysyft")

    assert string.title() == "Hello Pysyft"
    assert string.title() == String("Hello Pysyft")
    assert string.title() >= String("Hello Pysyft")
    assert string.title() <= String("Hello Pysyft")

    assert string.startswith("Hel") == True
    assert string.startswith(String("Hel")) == True

    assert string.endswith("Syft") == True
    assert string.endswith(String("Syft")) == True

    assert (string > "Hello PySyfa") == True
    assert (string >= "Hello PySyfa") == True

    assert (string < "Hello PySyfz") == True
    assert (string <= "Hello PySyfz") == True

    assert String(" Hello").lstrip() == "Hello"
    assert String("Hello ").rstrip() == "Hello"

    assert String("Hello").center(9) == "  Hello  "
    assert String("Hello").center(9) == String("  Hello  ")

    assert String("Hello").rjust(10) == "     Hello"
    assert String("Hello").rjust(10) == String("     Hello")

    assert String("Hello").ljust(10) == "Hello     "
    assert String("Hello").ljust(10) == String("Hello     ")

    assert string + string == "Hello PySyftHello PySyft"
    assert isinstance(string + string, String)
    assert isinstance(string + " !", String)

    assert f"{string} !" == "Hello PySyft !"

    assert String("Hello {}").format(String("PySyft")) == string
    assert String("Hello %s") % "PySyft" == string

    assert str(string) == "Hello PySyft"
