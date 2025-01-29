import threading

from dao.transaction import Transaction, TransactionManager
from dao.wallet import WalletManager
from singleton import singleton


@singleton
class DigitalWalletSystem:
    def __init__(self):
        self.wallet_manager = WalletManager()
        self.transaction_manager = TransactionManager()
        self._lock = threading.Lock()

    def create_wallet(self, wallet_name: str, initial_amount: float):
        wallet = self.wallet_manager.create_wallet(wallet_name, initial_amount)
        return wallet

    def transfter_money(
        self, from_wallet_name: str, to_wallet_name: str, amount: float
    ):
        from_wallet = self.wallet_manager.get_wallet(from_wallet_name)
        to_wallet = self.wallet_manager.get_wallet(to_wallet_name)
        self.transaction_manager.process_transactions(
            Transaction(from_wallet=from_wallet, to_wallet=to_wallet, amount=amount)
        )

    def get_statement(self, wallet_name: str):
        wallet = self.wallet_manager.get_wallet(wallet_name)
        for transaction in self.transaction_manager.get_transaction_history(wallet):
            if transaction.amount < 0:
                print(
                    f"Received {abs(transaction.amount)} from {transaction.from_wallet.name}"
                )
            else:
                print(
                    f"Transferred {transaction.amount} from {transaction.to_wallet.name}"
                )

    def get_overview(self):
        for name, balance in self.wallet_manager.get_overview():
            print(f"Wallet {name}: {balance}")

    def offer_2(self):
        self.transaction_manager.apply_offer_2()
