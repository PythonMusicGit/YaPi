Pupils = []
SystemPupils = {}

class Pupil:
    def __init__(self, lastn, firstn, mark):
        self.firstn = firstn
        self.lastn = lastn
        self.mark = mark
        self.isExcellent = mark == 5

def addPupil(sn, ln, fn, m):
    SystemPupils[f'{sn}'] = Pupil(ln, fn, m)
    Pupils.append(SystemPupils[f'{sn}'])

# Add pupils
addPupil('1pupil', 'Собакин', 'П.', 1)
addPupil('2pupil', 'Єврей', 'М.', 2)
addPupil('3pupil', 'Кавала', 'К.', 3)
addPupil('4pupil', 'Пушкін', 'А.', 4)
addPupil('5pupil', 'Абриген', 'П.', 5)

# Open file once for writing with UTF-8 encoding
with open('pupils.txt', 'w', encoding='utf-8') as file:
    # Writing all pupils
    for i, SPupil in enumerate(SystemPupils.values(), 1):
        file.write(f'{SPupil.lastn} {SPupil.firstn}: {SPupil.mark}')
        if i != len(SystemPupils):
            file.write('\n')

    # Writing the list of excellent pupils
    file.write('\n\nвідмінники:')
    for SPupil in SystemPupils.values():
        if SPupil.isExcellent:
            file.write(f'\n{SPupil.lastn}')
