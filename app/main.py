class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def create_person_list(people: list) -> list:
        person_list = []
        for person in people:
            person_list.append(person)

        for person in people:
            spouse = Person.people[person["name"]]
            if "wife" in person and person ["wife"] is not None:
                spouse.wife = person["wife"]
            if "husband" in person and person ["husband"] is not None:
                spouse.husband = person["husband"]

        return person_list

        for person in people:
            if wife in person and person [wife] is not None:

