import sys


class Stu(object):
    def __init__(self, data):
        self.src_data = data[:-1].split(" ")
        self.first_name = self.src_data[0]
        self.last_name = self.src_data[1]
        self.id = self.src_data[2]
        self.score = int(self.src_data[3])
        self.gpa = calc_gpa(self.score)
        self.retake = is_retake(self.id)


def check_id_score(data):
    id_star = ['2022', '2021', '2020']
    id = data.split(' ')[2]
    score = data.split(' ')[3]
    if len(id) == 12 and id[:4] in id_star and (0 < int(score) <= 100):
        return True
    else:
        return False

def is_retake(id):
    if id[:4] != '2022':
        return 1
    else:
        return 0

def calc_gpa(score):
    if score >= 93:
        return "A+"
    elif score >= 85:
        return 'A'
    elif score >= 80:
        return 'B+'
    elif score >= 75:
        return 'B'
    elif score >= 70:
        return 'C+'
    elif score >= 65:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
# for line in sys.stdin:
#     print(line[:-1])

def print_stu(stu):
    print(stu.first_name, end=' ')
    print(stu.last_name, end=' ')
    print(stu.id, end=' ')
    print(stu.score, end=' ')
    print(stu.retake, end=' ')
    print(stu.gpa, end='\n')
def Add(name_f, name_l, id, score):
    pass
if __name__ == '__main__':

    stus = ['Jingyu LI 202200000000 85\n',

            'Jy LEE 202200100000 89\n',

            'Jxxxyx Leeeee 202100100000 100\n',

            'Jingyu11 LI 202200000001 85\n']
    for line in sys.stdin:
        stus.append(line)
        Add(1, 2, 3, 4)
    # for i in range(2):
    #     line = input()
    #     Add(1, 2, 3, 4)
    #     stus.append(line+'\n')
    stus = filter(check_id_score, stus)
    stus = list(map(Stu, stus))
    print('Name_f Name_l stu_id score retake GPA')
    for stu in stus:
        print_stu(stu)

    print('Total: {}'.format(len(stus)))