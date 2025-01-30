# CreateWallet Harry 100
# CreateWallet Ron 95.7
# CreateWallet Hermione 104
# CreateWallet Albus 200
# CreateWallet Draco 500
# Overview
# Harry 100
# Ron 95.7
# Hermione 104
# Albus 200
# Draco 500
# TransferMoney Albus Draco 30
# TransferMoney Hermione Harry 2
# TransferMoney Albus Ron 5
# Overview
# Harry 112
# Ron 100.7
# Hermione 112
# Albus 165
# Draco 530
# Statement Harry
# Hermione credit 2
# Offer1 credit 10
# Statement Albus
# Draco debit 30
# Ron debit 5
# Offer2
# Overview
# Harry 114
# Ron 100.7
# Hermione 112
# Albus 175
# Draco 535


from digital_wallet import DigitalWalletSystem


digital_wallet = DigitalWalletSystem()
digital_wallet.create_wallet("harry", 100)
digital_wallet.create_wallet("ron", 95.7)
digital_wallet.create_wallet("hermione", 104)
digital_wallet.create_wallet("albus", 200)
digital_wallet.create_wallet("draco", 500)

digital_wallet.get_overview()

digital_wallet.transfer_money("albus", "draco", 30)
digital_wallet.transfer_money("hermione", "harry", 2)
digital_wallet.transfer_money("albus", "ron", 5)

digital_wallet.get_overview()
digital_wallet.get_statement("harry")
digital_wallet.get_statement("albus")
digital_wallet.offer_2()
