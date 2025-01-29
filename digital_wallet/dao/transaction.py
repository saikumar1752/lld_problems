from enum import Enum
import threading
from collections import defaultdict
from typing import Dict, List

from dao.wallet import Wallet, WalletManager
from singleton import singleton


class TransactionType(str, Enum):
    TRANSACTION: str = "transaction"
    CREDIT: str = "credit"
    DEBIT: str = "debit"


class Transaction:
    def __init__(
        self,
        from_wallet: Wallet,
        to_wallet: Wallet,
        amount: float,
        transaction_type: TransactionType,
    ):
        self.from_wallet = from_wallet
        self.to_wallet = to_wallet
        self.amount = amount
        self.transaction_type = transaction_type


@singleton
class TransactionManager:
    def __init__(self):
        self._lock = threading.Lock()
        self.transactions: Dict[str, List[Transaction]] = defaultdict(list)

    def record_transactions(self, transaction: Transaction):
        with self._lock:
            self.transactions[transaction.from_wallet.name].append(transaction)

    def get_transaction_history(self, wallet: Wallet) -> List[Transaction]:
        with self._lock:
            transactions = self.transactions.get(wallet.name, [])
        return transactions

    def process_transactions(self, transaction: Transaction):
        transaction.from_wallet.withdraw(transaction.amount)
        transaction.to_wallet.deposit(transaction.amount)
        self.record_transactions(
            Transaction(
                from_wallet=transaction.from_wallet,
                to_wallet=transaction.to_wallet,
                amount=transaction.amount,
                transaction_type=TransactionType.DEBIT,
            )
        )
        self.record_transactions(
            Transaction(
                from_wallet=transaction.to_wallet,
                to_wallet=transaction.from_wallet,
                amount=-1 * transaction.amount,
                transaction_type=TransactionType.CREDIT,
            )
        )
        with transaction.from_wallet._lock, transaction.to_wallet._lock:
            if transaction.from_wallet.balance == transaction.to_wallet.balance:
                transaction.from_wallet.deposit(10)
                transaction.to_wallet.deposit(10)

    def apply_offer_2(self):
        wallet_manager = WalletManager()
        overview = wallet_manager.get_overview()
        with self._lock():
            wallet_stats = [
                (len(self.transactions.get(name, [])), balance, name)
                for name, balance in overview
            ]
            wallet_stats.sort(key=lambda x: (-x[0], -x[1], x[2]))
            rewards = [10, 5, 2]
            for i, reward in enumerate(rewards):
                if i < len(wallet_stats):
                    wallet = wallet_manager.get_wallet(wallet_stats[i][2])
                    wallet.deposit(reward)
