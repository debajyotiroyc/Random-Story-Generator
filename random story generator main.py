import random as rd
when=["Once a upon a time","A few decades ago","A year ago","Some centuries ago"]
there="there was a "
what=["King","Soldier","Poet","Bull","Lion","Fox","Mouse","Tiger"]
named=" named "
who=["Jack","Julius","Robert","Ceaser","Philip","Henry"]
lived_in=" lived in "
where=["England","India","Italy","Belgium","Mexico","Africa","Australia","Argentina"]
where2=["Egypt","Venice","Germany","Canada","Brazil","Japan"]
dream=" He dreamt of being a "
aspire=["musician","chef","drummer","minister","athlete"]
so=" so he went to "
aspire2=" to fullfill his dream."

print(rd.choice(when)+", "+there+rd.choice(what)+named+rd.choice(who)+" who"+lived_in+rd.choice(where)+"."+dream+rd.choice(aspire)+so+rd.choice(where2)+aspire2 )
