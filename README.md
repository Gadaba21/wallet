#  Проэкт Wallet

## О проэкте

Вертуальный Кошелек, куда ты можешь класть свои вертуальные деньги,
за раз не больше 1000, лимита на кошельке нет

## Пример запроса
POST api/v1/wallets/<WALLET_UUID>/operation
для пополнения кошелька
GET api/v1/wallets/{WALLET_UUID}
для баланса кошелька