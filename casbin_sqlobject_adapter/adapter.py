from casbin import persist
from sqlobject import SQLObject, StringCol, sqlhub, connectionForURI


class CasbinRule(SQLObject):
    class sqlmeta:

        table = "casbin_rule"

    ptype = StringCol(length=255)
    v0 = StringCol(length=255, default=None)
    v1 = StringCol(length=255, default=None)
    v2 = StringCol(length=255, default=None)
    v3 = StringCol(length=255, default=None)
    v4 = StringCol(length=255, default=None)
    v5 = StringCol(length=255, default=None)

    def __str__(self):
        arr = [self.ptype]
        for v in (self.v0, self.v1, self.v2, self.v3, self.v4, self.v5):
            if v is None:
                break
            arr.append(v)
        return ", ".join(arr)

    def __repr__(self):
        return '<CasbinRule {}: "{}">'.format(self.id, str(self))


class Adapter(persist.Adapter):
    """the interface for Casbin adapters."""

    def __init__(self, connection_string):
        self._conhandler = connectionForURI(connection_string)
        sqlhub.processConnection = self._conhandler

    def load_policy(self, model):
        """loads all policy rules from the storage."""
        count = CasbinRule.select().count()
        for i in range(1, 1 + count):
            line = CasbinRule.get(i)
            persist.load_policy_line(str(line), model)

    def _save_policy_line(self, ptype, rule):
        line = CasbinRule.selectBy(ptype=ptype)
        for i, v in enumerate(rule):
            setattr(line, "v{}".format(i), v)

    def save_policy(self, model):
        """saves all policy rules to the storage."""
        for sec in ["p", "g"]:
            if sec not in model.model.keys():
                continue
            for ptype, ast in model.model[sec].items():
                for rule in ast.policy:
                    self._save_policy_line(ptype, rule)

        return True

    def add_policy(self, sec, ptype, rule):
        """adds a policy rule to the storage."""
        self._save_policy_line(ptype, rule)

    def remove_policy(self, sec, ptype, rule):
        """removes a policy rule from the storage."""
        pass

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """removes policy rules that match the filter from the storage.
        This is part of the Auto-Save feature.
        """
        pass
