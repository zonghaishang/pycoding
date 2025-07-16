import unicodedata as u


def equal_nfc(s1, s2):
    return u.normalize('NFC', s1) == u.normalize('NFC', s2)

def equal_nfc_ignore_case(s1, s2):
    return u.normalize('NFC', s1).casefold() == u.normalize('NFC', s2).casefold()


s3 = 'Straße'
s4 = 'strasse'
print(s3, s4)
print("s3 == s4", s3 == s4)
print("equal_nfc(s3, s4)", equal_nfc(s3, s4))
print("equal_nfc_ignore_case(s3, s4)", equal_nfc_ignore_case(s3, s4))