class Students():
    def __init__(self, frist_name, last_name, std_id):
        self.first_name = frist_name
        self.last_name = last_name
        self.std_id = frist_name + "-" + last_name + '@university.sa'

    def FullName(self):
        return self.first_name + '' + self.last_name

    def GetEmail(self):
        return self.std_id


if __name__ == "__main__":
    student1 = Students('Sultan', 'Alharthi', 130505)
    print('Your name is', student1.FullName(),
          '\n Your email', student1.GetEmail())
    print('-'*20)
    student1 = Students('Mohamed', 'Saad', 110696)
    print('Your name is', student1.FullName(),
          '\n Your email', student1.GetEmail())
    print('-' * 20)
