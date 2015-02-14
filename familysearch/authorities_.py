"""FamilySearch Authorities submodule"""
# Python imports
 
# Magic

class Authorities():
    """https://familysearch.org/developers/docs/api/resources#authorities"""
    def __init__(self):
        """https://familysearch.org/developers/docs/api/examples#authorities."""
        from . import FamilySearch
        FamilySearch.__bases__ += (Authorities,)

    def get_dates(self, dateX):
        """https://familysearch.org/developers/docs/api/dates/Date_resource."""
        return self.base + '/platform/dates?date=' + dateX