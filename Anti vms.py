import pefile

def fonction_vms(filepath):
    pe = pefile.PE(filepath)

    anti_vm_strings = ["VMWARE", "VIRTUALBOX", "VBOX", "QEMU", "XEN", "HYPER-V"]

    for string in anti_vm_strings:
        for dll in pe.DIRECTORY_ENTRY_IMPORT:
            for inp in dll.imports :
                out = str(inp.name)
                if string.lower() in out.lower():
                    print(f"{string} string detected!")
                    return True 
    return False 

Resultat = fonction_vms(r"C:\Users\narimene\Downloads\Install League of Legends euw (1).exe")
print(Resultat)