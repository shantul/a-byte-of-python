import os
import time
import zipfile

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

#Run the backup
print "Zipping using zipfile"
print "Running:"
zipf = zipfile.ZipFile(target, "w")
for root, dirs, files in os.walk(source):
    for file in files:
        zipf.write(os.path.join(root, file))

zipf.close()

print "Successful backup to", target

