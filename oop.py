class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def srgr(self):
        if not self.grades:
            return 0
        some_arg = []
        for i in self.grades.values():
            some_arg.extend(i)
        return round(sum(some_arg) / len(some_arg), 2)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.srgr()}\n' \
              f'Курсы в процессе обучени: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() > other.srgr()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.srgr() == other.srgr()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def srgr(self):
        if not self.grades:
            return 0
        some_arg = []
        for i in self.grades.values():
            some_arg.extend(i)
        return round(sum(some_arg) / len(some_arg), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.srgr()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr() < other.srgr()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.course_name() == other.course_name()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_lecturer_1 = Lecturer('Dmitriy', 'Olenev')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Nikita', 'Nikitenko')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Aleksey', 'Alekseev')
best_lecturer_3.courses_attached += ['Python']

cool_rewiewer_1 = Reviewer('Aleksandr', 'Aleksandrov')
cool_rewiewer_1.courses_attached += ['Python']
cool_rewiewer_1.courses_attached += ['Java']

cool_rewiewer_2 = Reviewer('Nik', 'Volkov')
cool_rewiewer_2.courses_attached += ['Python']
cool_rewiewer_2.courses_attached += ['Java']

student_1 = Student('Sergey', 'Sergeev')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ctas', 'Stasov')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Ivan', 'Ivanov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Java', 5)
student_1.rate_hw(best_lecturer_2, 'Java', 7)
student_1.rate_hw(best_lecturer_2, 'Java', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 10)
student_2.rate_hw(best_lecturer_2, 'Java', 5)
student_2.rate_hw(best_lecturer_2, 'Java', 6)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

cool_rewiewer_1.rate_hw(student_1, 'Python', 8)
cool_rewiewer_1.rate_hw(student_1, 'Python', 9)
cool_rewiewer_1.rate_hw(student_1, 'Python', 10)

cool_rewiewer_2.rate_hw(student_2, 'Java', 8)
cool_rewiewer_2.rate_hw(student_2, 'Java', 7)
cool_rewiewer_2.rate_hw(student_2, 'Java', 9)

cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)
cool_rewiewer_2.rate_hw(student_3, 'Python', 8)
cool_rewiewer_2.rate_hw(student_3, 'Python', 7)
cool_rewiewer_2.rate_hw(student_3, 'Python', 9)

print(f'Перечень проверяющих:\n\n{cool_rewiewer_1}\n\n{cool_rewiewer_2}')
print()
print()

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()



print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()


student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(student_list, course_name):
    count_all = []
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            ex = stud.srgr()
            count_all.append(ex)
    return sum(count_all) / len(count_all)

def lecturer_rating(lecturer_list, course_name):
    count_all = []
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            l_ex = lect.srgr()
            count_all.append(l_ex)
    return sum(count_all) / len(count_all)


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")


print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")