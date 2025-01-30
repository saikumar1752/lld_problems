import threading
from typing import Dict, List, Tuple

from singleton import singleton


class Wallet:
    def __init__(self, name: str, balance: float):
        self.fixed_deposit: List[List[int]] = None
        self.name = name
        self.balance = balance
        self._lock = threading.Lock()

    def withdraw(self, amount: float):
        print("gotcha")
        with self._lock:
            if self.balance >= amount:
                self.balance -= amount
                if self.fixed_deposit and self.balance < self.fixed_deposit[0]:
                    self.fixed_deposit = None  # Dissolve Fixed Deposit
                elif self.fixed_deposit and self.balance >= self.fixed_deposit[0]:
                    self.fixed_deposit[1] -= 1
                elif self.fixed_deposit and self.fixed_deposit[1] == 0:
                    self.balance += 10

    def deposit(self, amount: float, alread_locked: bool = False):
        if alread_locked:
            self.balance += amount
            return
        with self._lock:
            self.balance += amount
            if self.fixed_deposit:
                self.fixed_deposit[1] -= 1
                if self.fixed_deposit[1] == 0:
                    self.balance += 10

    def start_fixed_deposit(self, amount: float):
        with self._lock:
            if self.balance >= amount:
                self.fixed_deposit = [amount, 5]
            else:
                raise ValueError("Insufficient balance")


@singleton
class WalletManager:
    def __init__(self):
        self.name_to_wallet_map: Dict[str, Wallet] = {}
        self._lock = threading.Lock()

    def get_wallet(self, name):
        with self._lock:
            if name in self.name_to_wallet_map:
                return self.name_to_wallet_map[name]
            else:
                raise ValueError("Wallet not found")

    def create_wallet(self, name, amount: float) -> Wallet:
        with self._lock:
            if name in self.name_to_wallet_map:
                raise ValueError("Wallet already exists")
            self.name_to_wallet_map[name] = Wallet(name, amount)
        return self.name_to_wallet_map[name]

    def deposit(self, wallet: Wallet, amount: float):
        wallet.deposit(amount)

    def withdraw(self, wallet: Wallet, amount: float):
        wallet.withdraw(amount)

    def start_fixed_deposit(self, wallet: Wallet, amount: float):
        wallet.start_fixed_deposit(amount)

    def get_overview(self) -> List[Tuple[str, float]]:
        overview: List[Tuple[str, float]] = []
        with self._lock:
            for name, wallet in self.name_to_wallet_map.items():
                overview.append((name, wallet.balance))
        return overview
