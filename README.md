## Notification Service (Aiogram)

A microservice for sending notifications to Telegram. Receives events from RabbitMQ and notifies users.

## 🛠 Технологии
- Python 3.10+
- Aiogram (3.x)
- RabbitMQ (aio-pika)

## 📦 Installation
1. Clone the repository:
    ```bash
   git clone https://github.com/t1pson86/telegram-notification-service.git
   ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Interacting with other services
Accepts messages from RabbitMQ in the following format:

```json
{
  "data": "str"
}
```

## 📌 Related repositories

[Order Service (FastAPI)](https://github.com/t1pson86/orders-api-service) — the main API for working with orders.

<div align="center"> <sub>Built with ❤️ for professional Aiogram projects.</sub> </div>
