class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  # baraye auto increment id
        self._members = [
            {
                "id": self._generate_id(),  # id ha baraye har member
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 2]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # in method id jadid bar asas counter misazim
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # vaghti member jadid miad, id va last_name set mishavad
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)  # ezafe kardan be list asli
        return member

    def delete_member(self, id):
        # loop baraye peyda kardan member ba id
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)  # hazf az list
                return True  # faghat vaghti hazf shod true bargardoon
        return False  # agar peyda nashod

    def get_member(self, id):
        # gashtan dar list baraye peyda kardan member
        for member in self._members:
            if member["id"] == id:
                return member
        return None  # agar vojood nadasht

    def get_all_members(self):
        # tamame member ha ra bargardoon
        return self._members