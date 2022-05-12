class GenderChoice:
    male = 'Male'
    female = 'Female'

    @classmethod
    def choice(cls):
        return (
            (cls.male, cls.male),
            (cls.female, cls.female)
        )