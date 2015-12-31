import os
import time

source = "/home/shsharma/Documents/notes"

target_dir = "/home/shsharma/Documents/backup"

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime("%H%M%S")

# Take a comment from the user to
# create the name of the zip file
comment = raw_input('Enter a comment --> ')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print "Successfully created directory", today

zip_command = "zip -r {0} {1}".format(target, source)

#Run the backup
print "Zip Command is:"
print zip_command
print "Running:"
if os.system(zip_command) == 0:
    print "Successful backup to", target
else:
    print "Backup FAILED!"

