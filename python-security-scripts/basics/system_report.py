import subprocess

def run(cmd)
    rusult = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    return result.stdout.stript()
import subprocess

def run(cmd):
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

reportreport.append("=== SYSTEM REPORT ===")
