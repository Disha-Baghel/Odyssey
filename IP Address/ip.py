import subprocess

url = input("Enter the url of website: ")

# output = subprocess.check_output(f"ping -c 1 {url}", shell=True)
output = str(subprocess.check_output(["ping", "-c", "1", url]))

print(f"IP address", output[output.find("(")+1:output.find(")"):])

# print(output)