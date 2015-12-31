import os
import time

source = "/home/shsharma/Documents/notes"

target_dir = "/home/shsharma/Documents/backup"

target = target_dir + os.sep + \
        time.strftime('%Y%m%d%H%M%S') + ".zip"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = "zip -r {0} {1}".format(target, source)

#Run the backup
print "Zip Command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAILED!"

