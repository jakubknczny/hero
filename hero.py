import PySimpleGUI as Sg

Sg.theme('DarkPurple1')


# https://pysimplegui.readthedocs.io/en/latest/cookbook/
class Hero:

    def __init__(self, name="Jagoda, Python Whisperer", health=100, experience=0):
        self.name = name
        self.health = health
        self.experience = experience

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_experience(self):
        return self.experience

    def set_experience(self, experience):
        self.experience = experience


def create_main_window():
    layout = [[Sg.T('Edit Hero')],
              [Sg.B('Health -1'), Sg.B('Health +1')],
              [Sg.B('Experience -1'), Sg.B('Experience +1')],
              [Sg.Text(size=(50, 1), key='-NAME-')],
              [Sg.T('Health'), Sg.Text(size=(5, 1), justification='r', key='-HEALTH-')],
              [Sg.T('Experience'), Sg.Text(size=(5, 1), justification='r', key='-EXPERIENCE-')],
              [Sg.B('Exit')]]

    return Sg.Window('The Most Awesome Hero Editor', layout)


def main():
    window = None
    hero = Hero()

    while True:  # Event Loop
        if window is None:
            window = create_main_window().finalize()
            window.set_min_size((640, 480))
            window['-NAME-'].update(hero.get_name())
            window['-HEALTH-'].update(hero.get_health())
            window['-EXPERIENCE-'].update(hero.get_experience())

        event, values = window.read()
        if event in (Sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Health -1':
            hero.set_health(hero.get_health() - 1)
            window['-HEALTH-'].update(hero.get_health())
        if event == 'Health +1':
            hero.set_health(hero.get_health() + 1)
            window['-HEALTH-'].update(hero.get_health())
        if event == 'Experience -1':
            hero.set_experience(hero.get_experience() - 1)
            window['-EXPERIENCE-'].update(hero.get_experience())
        if event == 'Experience +1':
            hero.set_experience(hero.get_experience() + 1)
            window['-EXPERIENCE-'].update(hero.get_experience())
    window.close()


main()
