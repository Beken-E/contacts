class ContactList(list):
    def __init__(self, my_list):
        self.my_list = my_list
    

    def search_name(self, data):
        res = []
        for i in self.my_list:
            if i == data:
                res.append(i)
            else:
                continue
        return res


all_contacts = ContactList(["Ivan", "Masha", "Jenya", "Masha"])

r = input("Enter name to find: ")

print(all_contacts.search_name(r))