import os
import shutil

from_dir ="/Users/Afra/Downloads/PRO_1-1_C102_AtividadeDoAluno1-main"
to_dir = "/Users/Afra/Desktop/imagem baixadas"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extencion = os.path.splitext(file_name)

    if extencion == '':
        continue
    if extencion in ['.gif','.png','.jpg,', '.jpeg', '.jfif']:

        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/'+ "Arquivos_imagem"
        path3 = to_dir + '/'+ "Arquivos_imagem" + file_name

    if os.path.exists(path2):
        print("Movendo " + file_name + ".....")

        shutil.move(path1, path3)

    else:
        os.makedirs(path2)
        print("Movendo " + file_name + ".....")
        shutil.move(path1,path3)