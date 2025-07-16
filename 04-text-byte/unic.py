import unicodedata as u
micro = 'μ'
print(u.name(micro))

micro_cf = micro.casefold()
print(u.name(micro_cf))

print(micro, micro_cf)
print("---------")
eszett = 'ß'
print(u.name(eszett))
eszett_cf = eszett.casefold()
# print(u.name(eszett_cf))

print(eszett, eszett_cf)