"""FamilySearch Parents and Children submodule"""
# Python imports

# Magic

class ParentsAndChildren:
    def __init__(self):
        """https://familysearch.org/developers/docs/api/resources#parents-and-children"""
        self.child_base = self.tree_base + "child-and-parents-relationships/"
        from familysearch import FamilySearch
        FamilySearch.__bases__ += (ParentsAndChildren,)

    def get_child_relationship(self, crid):
        """Obsolete."""
        return self.get(self.child_base + crid)

    def delete_child_relationship_parent(self, crid, parent):
        """Obsolete."""
        return self.delete(self.child_base + crid + "/" + parent)

    def delete_child_relationship_conclusion(self, crid, cid, role):
        """Obsolete."""
        return self.delete(self.child_base + crid + "/" + role + "/conclusions/" + cid)

    def child_relationship_restore(self, crid):
        """Obsolete."""
        return post(self.child_base + crid + "/restore", method="POST", nojson=True)