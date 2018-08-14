import requests
import shutil
from sys import argv

passed = 0
skipped = 0
for i in range(1000, int(argv[1])):
    path = f'https://www.gstatic.com/prettyearth/assets/full/{i}.jpg'
    r = requests.head(path)
    if r.headers['content-type'] == 'image/jpeg':
        p = requests.get(path, stream=True)
        with open(f'{argv[2]}/{i}.jpg', 'wb') as f:
            shutil.copyfileobj(p.raw, f)
        passed += 1
    else:
        skipped += 1
    print(f'{passed} passed, {skipped} skipped', end="\r")
print("")
