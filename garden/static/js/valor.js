fetch('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
  .then(response => response.json())
  .then(data => {
    const precioBTC = data.price;
    const BTCUSDT = Math.floor(precioBTC);
    const elementoPrecioBTC = document.getElementById('precio-btc');
    elementoPrecioBTC.innerHTML = BTCUSDT;
  });