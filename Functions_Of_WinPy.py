import subprocess
class restart_services():
    def restart_spooler():
        subprocess.call(['sc','stop','spooler'])
        subprocess.call(['sc','start','spooler'])
    restart_spooler()