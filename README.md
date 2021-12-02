## РБК

### Разработка программного решения конвертации видео в текст для рекомендательной системы РБК Xavier

Мы хотим оцифровать видео в текст и выделить в нем ключевые слова. Это сработает, т.к. практически все наши видео – это интервью и данные голосового взаимодействия. В идеале получить утилиту, которая получала бы на вход видео в любом популярном формате и возвращала бы его расшифровку в виде текста в любом стандартном формате ответа – JSON, XML и т.д.

### Установка

#### Docker

Перед установкой убедитесь в том что ваша хост машина подерживает виртуализацию, и в том что она включена.

Для Windows: убедитесь в том что у вас включен компонент Hyper-V.

Затем скачайте и установите Docker, Docker-Compose

#### Запуск

Склонируйте репорзиторий к себе!

Для запуска программы используйте:

Команду  `docker compose up --build`

Приложение доступно по адресу http://127.0.0.1:8000/

Придется чуть чуть подождать, нейронка мощная)