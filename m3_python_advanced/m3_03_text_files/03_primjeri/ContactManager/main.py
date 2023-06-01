from OrganizationManager import OrganizationManager


file_path = "OrganizationManager/organizacije.txt"


while True:
    print("******* Stvorite novu organizaciju *******")
    name = input("Upisite ime organizacije: ")
    address = input("Upisite adresu organizacije: ")
    oib = input("Upisite oib organizacije: ")

    OrganizationManager.create_organization(name, address, oib)

    if input("Zelite li unijeti novu organizaciju? (da/ne)") != "da":
        break

OrganizationManager.write_all_organization_to_file(file_path)
