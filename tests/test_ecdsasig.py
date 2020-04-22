#!/usr/bin/env python3

import binascii

from ledgerblue.ecWrapper import PrivateKey, PublicKey
from ledgerblue.comm import getDongle

PUBLIC_KEY="046F760E57383E3B5900F7C23B78A424E74BEBBE9B7B46316DA7C0B4B9C2C9301C0C076310EDA30506141DD47C2D0A8A1D7CA2542482926AE23B781546193B9616"

message = "76955a821a8aa04acb48203a7df7113bfd1a0f479552d9098e032fa9b1917018"

print("message=" + message)

messageBin = binascii.unhexlify(message)

apduMessage = "E003"
apdu = bytearray.fromhex(apduMessage)
apdu.extend(messageBin)

dongle = getDongle(True)
signature = dongle.exchange(apdu)
print("signature=\n" + str(binascii.hexlify(signature)))

publicKey = PublicKey(binascii.unhexlify(PUBLIC_KEY), True)
verified = publicKey.ecdsa_verify(messageBin, signature, True)
print("verified=" + str(verified))

