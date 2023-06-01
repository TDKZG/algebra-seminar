from FileManager import FileManager


class Organization:
    def __init__(self, name, address, oib):
        self.name = name
        self.address = address
        self.oib = oib

    def print_organization(self):
        print(f"Naziv: {self.name}\tadresa: {self.address}\tOIB: {self.oib}")

    def convert_to_string(self):
        return f"Naziv: {self.name}\tadresa: {self.address}\tOIB: {self.oib}"

    def change_name(self, new_name):
        self.name = new_name

    def change_address(self, new_address):
        self.address = new_address


organizations = {}


def create_organization(name, address, oib):
    organization = Organization(name, address, oib)
    organizations[oib] = organization


def write_all_organization_to_file(file_path):
    file_writer = FileManager.openFilePathForWriting(file_path)

    for organization in organizations.values():
        line = organization.convert_to_string()
        FileManager.writeLineWithFileWriter(file_writer, line)

    FileManager.closeFileConnection(file_writer)
