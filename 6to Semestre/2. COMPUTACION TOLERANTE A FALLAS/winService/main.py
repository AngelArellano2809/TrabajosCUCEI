import time
import subprocess
from pathlib import Path
from SMWinservice import SMWinservice

class PythonCornerExample(SMWinservice):
    _svc_name_ = "PythonService"
    _svc_display_name_ = "Python Service Actividad"
    _svc_description_ = "Servicio de pureba 1 (calcualdora)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        i = 0
        while self.isrunning:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            time.sleep(180)

if __name__ == '__main__':
    PythonCornerExample.parse_command_line()
