import search
import functions
import logmod
import salary
import addcard
import delete_card


def starting_module():
    a = functions.Menu()

    if a == 1:
        name = functions.Last_name()
        search.PersonSearch(name)
        logmod.log3(name)
    elif a == 2:
        job = functions.Post()
        search.PersonSearch(job)
        logmod.log4(job)
    elif a == 3:
        mon = functions.Pay()
        salary.Money(mon)
        logmod.log5(mon)
    elif a == 4:
        personal = functions.AddPersonal()
        addcard.AddWorker(personal)
        logmod.log2(personal)
    elif a == 5:
        dlt = functions.Delete()
        delete_card.DelCardWorker(dlt)
        logmod.log1(str(dlt))
    elif a == 6:
        ...
