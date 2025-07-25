import subprocess

try:
    result = subprocess.run([r"C:\wkhtmltopdf\bin\wkhtmltopdf.exe", "--version"], capture_output=True, text=True)
    print("Return code:", result.returncode)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
except Exception as e:
    print("Exception:", e) 