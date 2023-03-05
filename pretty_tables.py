from prettytable import PrettyTable


class PrettyView:
    def create_table(self, data):
        raise NotImplementedError

    def create_row(self, data):
        raise NotImplementedError


class SortView(PrettyView):
    def create_row(self, data):
        pt = PrettyTable()
        pt.field_names = ["Known extensions", "Unknown extensions"]
        pt.add_row(data)
        return pt

    def create_table(self, data):
        pass
