import PySimpleGUI as sg

sg.theme('DarkPurple1')
# https://pysimplegui.readthedocs.io/en/latest/cookbook/
class Hero():
    
    def __init__(self, name="Jagoda, Python Whisperer", health=100, experience=0):
        self.name = name
        self.health = health
        self.experience = experience

    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    def setHealth(self, health):
        self.health = health
    
    def getExperience(self):
        return self.experience

    def setExperience(self, experience):
        self.experience = experience


def create_main_window():
    

    layout = [[sg.T('Edit Hero')],
              [sg.B('Health -1'), sg.B('Health +1')],
              [sg.B('Experience -1'), sg.B('Experience +1')],
              [sg.Text(size=(50,1), key='-NAME-')],
              [sg.T('Health') ,sg.Text(size=(5,1), justification='r', key='-HEALTH-')],
              [sg.T('Experience') ,sg.Text(size=(5,1), justification='r', key='-EXPERIENCE-')],
              [sg.B('Exit')]]

    return sg.Window('The Most Awesome Hero Editor', layout)


def main():
    window = None
    hero = Hero()

    while True:             # Event Loop
        if window is None:
           window = create_main_window().finalize()
           window.set_min_size((640,480))
           window['-NAME-'].update(hero.getName())
           window['-HEALTH-'].update(hero.getHealth())
           window['-EXPERIENCE-'].update(hero.getExperience())

        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Health -1':
           hero.setHealth(hero.getHealth() - 1)
           window['-HEALTH-'].update(hero.getHealth())
        if event == 'Health +1':
           hero.setHealth(hero.getHealth() + 1)
           window['-HEALTH-'].update(hero.getHealth())
        if event == 'Experience -1':
            hero.setExperience(hero.getExperience() - 1)
            window['-EXPERIENCE-'].update(hero.getExperience())
        if event == 'Experience +1':
            hero.setExperience(hero.getExperience() + 1)
            window['-EXPERIENCE-'].update(hero.getExperience())
    window.close()

main()
