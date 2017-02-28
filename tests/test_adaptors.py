import unittest

from construct25 import Field, UBInt8
from construct25 import OneOf, NoneOf, HexDumpAdapter
from construct25 import ValidationError
from construct25.protocols.layer3.ipv4 import IpAddress


class TestHexDumpAdapter(unittest.TestCase):

    def setUp(self):
        self.hda = HexDumpAdapter(Field("hexdumpadapter", 6))

    def test_trivial(self):
        pass

    def test_parse(self):
        parsed = self.hda.parse(b"abcdef")
        self.assertEqual(parsed, b"abcdef")

    def test_build(self):
        self.assertEqual(self.hda.build(b"abcdef"), b"abcdef")

    def test_str(self):
        pretty = str(self.hda.parse(b"abcdef")).strip()

        offset, digits, ascii = [i.strip() for i in pretty.split("  ") if i]
        self.assertEqual(offset, "0000")
        self.assertEqual(digits, "61 62 63 64 65 66")
        self.assertEqual(ascii, "abcdef")

class TestNoneOf(unittest.TestCase):

    def setUp(self):
        self.n = NoneOf(UBInt8("foo"), [4, 5, 6, 7])

    def test_trivial(self):
        pass

    def test_parse(self):
        self.assertEqual(self.n.parse(b"\x08"), 8)

    def test_parse_invalid(self):
        self.assertRaises(ValidationError, self.n.parse, b"\x06")

class TestOneOf(unittest.TestCase):

    def setUp(self):
        self.o = OneOf(UBInt8("foo"), [4, 5, 6, 7])

    def test_trivial(self):
        pass

    def test_parse(self):
        self.assertEqual(self.o.parse(b"\x05"), 5)

    def test_parse_invalid(self):
        self.assertRaises(ValidationError, self.o.parse, b"\x08")

    def test_build(self):
        self.assertEqual(self.o.build(5), b"\x05")

    def test_build_invalid(self):
        self.assertRaises(ValidationError, self.o.build, 9)


class TestIpAddress(unittest.TestCase):

    def setUp(self):
        self.ipa = IpAddress("foo")

    def test_trivial(self):
        pass

    def test_parse(self):
        self.assertEqual(self.ipa.parse(b"\x7f\x80\x81\x82"), "127.128.129.130")

    def test_build(self):
        self.assertEqual(self.ipa.build("127.1.2.3"), b"\x7f\x01\x02\x03")

    def test_build_invalid(self):
        self.assertRaises(ValueError, self.ipa.build, "300.1.2.3")

