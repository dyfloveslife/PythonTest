class Person(object):
    """
    return Person object
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        return string include person's name
        """
        return self.name


class Student(Person):
    """
    return Student Object,include name,branch,year
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
         return string include student's details
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
           return Teacher Object,use string list as arguments
           """

    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('Sanchin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['c', 'c++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
