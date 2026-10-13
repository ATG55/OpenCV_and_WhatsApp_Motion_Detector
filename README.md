# OpenCV_and_WhatsApp_Motion_Detector
OpenCV_and_WhatsApp_Motion_Detector

[TR] Bu proje, web kamerası üzerinden hareket algıladığında WhatsApp Web aracılığıyla otomatik bildirim mesajı gönderen Python tabanlı bir güvenlik ve otomasyon sistemidir.

[EN] This project is a Python-based motion detection and automation system that monitors your webcam feed and automatically sends a notification message via WhatsApp Web whenever motion is detected.


* **TR:** Real-time (Eş zamanlı) hareket algılama (OpenCV MOG2).
* **EN:** Real-time motion detection using OpenCV's MOG2 background subtractor.
* **TR:** Otomatik WhatsApp mesaj gönderimi (PyAutoGUI ile).
* **EN:** Automated WhatsApp message delivery via PyAutoGUI.
* **TR:** Spam mesajları önlemek için bekleme süresi (Cooldown).
* **EN:** Cooldown mechanism to prevent message spam.

## Kurulum / Installation

Gerekli kütüphaneleri yüklemek için terminalde çalıştırın:
Run the following command in your terminal to install the dependencies

```bash
pip install -r requirements.txt