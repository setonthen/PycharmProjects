def main():
    contacts = {"Tom": {"name": "Tom Techie",
                        "phone": "040 123546",
                        "email": "tom@tut.fi",
                        "skype": "tom_92_"},
                "Mike": {"name": "Mike Mechanic",
                         "phone": "050 123546",
                         "email": "mike@tut.fi",
                         "skype": "-Mike-M-"},
                "Archie": {"name": "Archie Architect",
                           "phone": "050 987654",
                           "email": "archie@tut.fi"}}

    contact = input("Enter the name of the contact: ")
    field = input("Enter the field name you're searching for: ")
    if contact in contacts.keys():
        Name = ("{}".format(contacts[contact]['name']))

        if field in ("{}".format(contacts[contact])):
            data = ("{}".format(contacts[contact][field]))
            print(Name, ', ', field, ': ', data, sep="")
        else:
           print('No',field,'for',Name)


    else:
        print('No contact information for',contact)
main()