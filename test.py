import os
from dotenv import load_dotenv

# files = (
#     ('in1', 'out1'),
#     ('in1', 'out1'),
#     ('in1', 'out1'),
# )


import importlib
import sys

# Путь до директории
load_dotenv(".env")

# var_name1 = os.getenv("VAR_NAME1")
path_to_package = os.getenv("TASK", "example")  # Default value

# Добавляем путь в sys.path
if path_to_package not in sys.path:
    sys.path.append(path_to_package)

# Имя пакета
package_name = "main"

# Импортируем пакет
package = importlib.import_module(package_name)



def verdict(infn, infile, expected, found):
    if expected == found:
        print(infn, 'OK')
    else:
        print(infn, 'FAIL')
        print(infile)
        print('  expected:')
        print(expected)
        print('  found:')
        print(found)


files = [f for f in os.listdir(path_to_package+'/') if os.path.isfile(f)]
infiles = sorted([f for f in files if f.startswith('in')])
outfiles = sorted([f for f in files if f.startswith('out')])
tmp = 'tmp'
print(files, infiles, outfiles)
for infn, outfn in zip(infiles, outfiles):
    with open(infn, 'r') as fin, open(tmp, 'w') as ftmp:
        sys.stdin = fin
        # print(sys.stdin)
        sys.stdout = ftmp
        # Используем пакет
        package.main()
        sys.stdout = sys.__stdout__
    with open(infn, 'r') as fin, open(outfn, 'r') as fout, open(tmp, 'r') as ftmp:
        content_in = fin.read()
        content_expected = fout.read()
        content_found = ftmp.read()
    verdict(infn, content_in, content_expected, content_found)
