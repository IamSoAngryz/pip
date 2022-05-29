"""
Virtual evironments = medii virtuale izolate care permit separarea proiectelor
                    prin instalarea librariilor (packages) specifice, cu
                    versiuni specifice, la nivel de proiect (mediu de lucru)
Prin crearea unui mediu izolat de lucru (de dezvlotare) lucram cu librarii
specifice proiectului, versiuni specifice, fara a fi nevoie sa avem toate
librariile instalate global.

Pentru a lucra cu virtual evironments trebuia instalata libraria virtualenv
pip installc virtualenv

1/ Pentru a crea un mediu izolat de lucru (virtual environments):
py -m venv nume_virtual_env
ex: py -m venv mediu
sau ruland:
virtualenv nume_virtual_env
ex: virtualenv mediu2

2/ Activarea unui virtual evironment
./nume_virtual_env/Scripts/activate

Se schimba promptul in format (nume_virtual_env)cale_director

3/ Dezactivarea unui virtual evironment
deactivate
Promptul nu mai are intre paranteze rotunde numele virtual environmentului

pip freeze
afiseaza modulele si versiunea int-run format specific, outputul fiind cel 
utilizat la crearea unor fisiere de requirementes (fisiere text care contin
toate librariiile din proiect si versiunile acestora)

5/ Crearea unui fisire de requirements
pip freeze > requirements.txt

6/ La clonarea sau copierea unui proiect se pot instala toate librariile cu
comanda(dupa crearea unui mediu izolat cu comanda "virtualenv envone" si
activarea acestuia cu ".\envone\Scripts\activate"):
pip install -r requirements.txt
"""