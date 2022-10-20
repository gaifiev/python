import import1
import export
import modif
import logmod


def start():
    if modif.mod() == '1':
        info = modif.export1()
        export.export2(info)
        logmod.log(info)
    else:
        info = modif.mod2()
        import1.import2(info)
        logmod.log(info)
