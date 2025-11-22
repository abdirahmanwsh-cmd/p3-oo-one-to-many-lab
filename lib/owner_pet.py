class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # will be set if owner is passed

        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")

        # Assign owner if provided and validate type
        if owner:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            self.owner = owner

        # Add to class-level list of all pets
        Pet.all.append(self)
pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """
        Returns a list of Pet instances that belong to this owner.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Assigns a Pet instance to this owner.
        Raises Exception if the argument is not a Pet.
        """
        if not isinstance(pet, Pet):
            raise Exception("add_pet argument must be a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        """
        Returns a list of this owner's pets, sorted by pet name.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)
