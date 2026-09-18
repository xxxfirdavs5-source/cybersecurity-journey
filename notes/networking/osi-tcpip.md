# OSI and TCP/IP

## OSI — 7 уровней

7. Application — HTTP, DNS, SSH
6. Presentation — формат данных, шифрование
5. Session — сеанс связи
4. Transport — TCP, UDP, порты
3. Network — IP, маршрутизация
2. Data Link — MAC, Ethernet
1. Physical — кабель, Wi-Fi, сигналы

## TCP/IP — 4 уровня

Application → OSI 5–7
Transport → OSI 4
Internet → OSI 3
Network Access → OSI 1–2

## Инкапсуляция

Данные
↓
TCP/UDP
↓
IP
↓
Ethernet
↓
Биты

При получении происходит декапсуляция:
убирается служебная информация, добавленная уровнями.

## TCP vs UDP

TCP → соединение, надёжность, порядок данных
UDP → без TCP-соединения, меньше накладных расходов, важна своевременная передача

## TCP Three-Way Handshake

SYN → «хочу установить соединение»
SYN-ACK → «получил, готов»
ACK → «подтверждаю»

## Полезная привязка

Ethernet → OSI 2
IP → OSI 3
TCP/UDP → OSI 4
HTTP/HTTPS → OSI 7

## Практика

ping -c 2 8.8.8.8
sudo tcpdump -i wlan0 -n -c 5
curl -I http://neverssl.com
