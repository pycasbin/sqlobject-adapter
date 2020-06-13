import os
import unittest

import casbin

from casbin_sqlobject_adapter import Adapter
from casbin_sqlobject_adapter import CasbinRule


def get_fixture(path):
    dir_path = os.path.split(os.path.realpath(__file__))[0] + "/"
    return os.path.abspath(dir_path + path)


def get_enforcer():
    con_string = "sqlite:/:memory:"
    adapter = Adapter(con_string)

    CasbinRule.createTable(ifNotExists=True)
    CasbinRule(ptype="p", v0="alice", v1="data1", v2="read")
    CasbinRule(ptype="p", v0="bob", v1="data2", v2="write")
    CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="read")
    CasbinRule(ptype="p", v0="data2_admin", v1="data2", v2="write")
    CasbinRule(ptype="g", v0="alice", v1="data2_admin")

    return casbin.Enforcer(get_fixture("rbac_model.conf"), adapter)


class TestConfig(unittest.TestCase):
    def test_enforcer_basic(self):
        e = get_enforcer()

        self.assertTrue(e.enforce("alice", "data1", "read"))
        self.assertFalse(e.enforce("bob", "data1", "read"))
        self.assertTrue(e.enforce("bob", "data2", "write"))
        self.assertTrue(e.enforce("alice", "data2", "read"))
        self.assertTrue(e.enforce("alice", "data2", "write"))

    def test_add_policy(self):
        e = get_enforcer()

        self.assertFalse(e.enforce("eve", "data3", "read"))
        res = e.add_permission_for_user("eve", "data3", "read")
        self.assertTrue(res)
        self.assertTrue(e.enforce("eve", "data3", "read"))

    def test_save_policy(self):
        e = get_enforcer()
        self.assertFalse(e.enforce("alice", "data4", "read"))

        model = e.get_model()
        model.clear_policy()

        model.add_policy("p", "p", ["alice", "data4", "read"])

        adapter = e.get_adapter()
        adapter.save_policy(model)
        self.assertTrue(e.enforce("alice", "data4", "read"))

    def test_str(self):
        rule = CasbinRule(ptype="p", v0="alice", v1="data1", v2="read")
        self.assertEqual(str(rule), "p, alice, data1, read")

    def test_repr(self):
        rule = CasbinRule(ptype="p", v0="alice", v1="data1", v2="read")
        self.assertRegex(repr(rule), r'<CasbinRule \d+: "p, alice, data1, read">')
